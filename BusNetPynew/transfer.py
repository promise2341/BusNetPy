"""换乘分析模块。

提供公交换乘相关的深度分析功能：
    - 换乘站点识别与评级
    - 直达率 / 一次换乘可达率分析
    - 换乘方案详情提取
    - 线路衔接关系分析

典型用法::

    from BusNetPynew.transfer import (
        identify_transfer_stations, direct_reach_rate,
        transfer_connectivity, line_connection_matrix
    )

    transfers = identify_transfer_stations(G_L)
    rates = direct_reach_rate(G_L, G_P)
    matrix = line_connection_matrix(G_L)
"""

from typing import Any, Dict

import networkx as nx
import pandas as pd


def identify_transfer_stations(
    G_L: nx.Graph,
    min_lines: int = 2,
) -> pd.DataFrame:
    """识别换乘站点并评级。

    找出被两条及以上线路经过的站点，并按线路数量评级。

    Args:
        G_L: Space-L 网络图。
        min_lines: 最少经过线路数（去重后）才算换乘站，默认 2。

    Returns:
        DataFrame，包含：
            - node_id: 站点 ID
            - staname: 站点名称
            - line_count: 经过的线路数（去重后）
            - lines: 经过的线路名称列表
            - lng / lat: 坐标
            - level: 等级（'一般换乘站' / '重要换乘站' / '枢纽站'）
        按 line_count 降序排列。

    Examples:
        >>> df = identify_transfer_stations(G_L)
        >>> hub_stations = df[df['level'] == '枢纽站']
    """
    stations = []
    for node, data in G_L.nodes(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = list(set(line.split('(')[0] for line in bus_lines))

        if len(unique_lines) >= min_lines:
            count = len(unique_lines)
            if count >= 8:
                level = '枢纽站'
            elif count >= 4:
                level = '重要换乘站'
            else:
                level = '一般换乘站'

            pos = data.get('pos', (0, 0))
            stations.append({
                'node_id': node,
                'staname': data.get('staname', ''),
                'line_count': count,
                'lines': unique_lines,
                'lng': pos[0],
                'lat': pos[1],
                'level': level,
            })

    df = pd.DataFrame(stations)
    if not df.empty:
        df = df.sort_values('line_count', ascending=False).reset_index(drop=True)
    return df


def direct_reach_rate(
    G_L: nx.Graph,
) -> Dict[str, Any]:
    """计算公交线网的直达率和换乘分布。

    分析网络中任意两站之间的可达性：
    - 直达率：不换乘即可到达的站点对比例
    - 一次换乘可达率：最多换乘一次可达的比例

    直达的定义：两个站点存在共同经过的线路。

    Args:
        G_L: Space-L 网络图。

    Returns:
        字典，包含：
            - total_pairs: 总站点对数
            - direct_pairs: 直达站点对数
            - direct_rate: 直达率
            - one_transfer_pairs: 一次换乘可达的站点对数
            - one_transfer_rate: 一次换乘可达率（含直达）
            - unreachable_pairs: 不可达站点对数
            - connected_rate: 总可达率

    Examples:
        >>> rates = direct_reach_rate(G_L)
        >>> print(f"直达率: {rates['direct_rate']:.1%}")
    """
    nodes = list(G_L.nodes())
    n = len(nodes)
    total_pairs = n * (n - 1) // 2

    node_lines = {}
    for node, data in G_L.nodes(data=True):
        bus_lines = data.get('bus_lines', [])
        node_lines[node] = set(line.split('(')[0] for line in bus_lines)

    line_stations = {}
    for node, lines in node_lines.items():
        for line in lines:
            if line not in line_stations:
                line_stations[line] = set()
            line_stations[line].add(node)

    direct_pairs = 0
    direct_set = set()
    for line, stations in line_stations.items():
        station_list = sorted(stations)
        for i in range(len(station_list)):
            for j in range(i + 1, len(station_list)):
                pair = (station_list[i], station_list[j])
                if pair not in direct_set:
                    direct_set.add(pair)
                    direct_pairs += 1

    one_transfer_set = set(direct_set)
    lines_list = list(line_stations.keys())
    for i in range(len(lines_list)):
        for j in range(i + 1, len(lines_list)):
            shared = line_stations[lines_list[i]] & line_stations[lines_list[j]]
            if shared:
                for s_a in line_stations[lines_list[i]]:
                    for s_b in line_stations[lines_list[j]]:
                        if s_a != s_b:
                            pair = tuple(sorted([s_a, s_b]))
                            one_transfer_set.add(pair)

    one_transfer_pairs = len(one_transfer_set)

    connected_components = nx.number_connected_components(G_L)
    if connected_components == 1:
        unreachable = 0
    else:
        reachable = 0
        for comp in nx.connected_components(G_L):
            comp_size = len(comp)
            reachable += comp_size * (comp_size - 1) // 2
        unreachable = total_pairs - reachable

    return {
        'total_pairs': total_pairs,
        'direct_pairs': direct_pairs,
        'direct_rate': direct_pairs / total_pairs if total_pairs > 0 else 0,
        'one_transfer_pairs': one_transfer_pairs,
        'one_transfer_rate': one_transfer_pairs / total_pairs if total_pairs > 0 else 0,
        'unreachable_pairs': unreachable,
        'connected_rate': 1 - unreachable / total_pairs if total_pairs > 0 else 0,
    }


def transfer_connectivity(
    G_L: nx.Graph,
) -> pd.DataFrame:
    """分析各换乘站的换乘连通性。

    对每个换乘站，统计它连接了哪些线路对之间的换乘。

    Args:
        G_L: Space-L 网络图。

    Returns:
        DataFrame，每行代表一个可换乘的线路对，包含：
            - transfer_station: 换乘站名
            - line_a / line_b: 换乘线路对
            - node_id: 换乘站 ID
    """
    connections = []
    for node, data in G_L.nodes(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = sorted(set(line.split('(')[0] for line in bus_lines))

        if len(unique_lines) >= 2:
            for i in range(len(unique_lines)):
                for j in range(i + 1, len(unique_lines)):
                    connections.append({
                        'transfer_station': data.get('staname', ''),
                        'node_id': node,
                        'line_a': unique_lines[i],
                        'line_b': unique_lines[j],
                    })

    return pd.DataFrame(connections)


def line_connection_matrix(
    G_L: nx.Graph,
) -> pd.DataFrame:
    """生成线路换乘关联矩阵。

    矩阵中每个单元格 [A, B] 的值表示 A 路和 B 路之间有多少个换乘站。

    Args:
        G_L: Space-L 网络图。

    Returns:
        方阵 DataFrame，行列均为线路名，值为共有换乘站数量。

    Examples:
        >>> matrix = line_connection_matrix(G_L)
        >>> print(f"1路和2路有 {matrix.loc['1路', '2路']} 个换乘站")
    """
    all_lines = set()
    for _, data in G_L.nodes(data=True):
        bus_lines = data.get('bus_lines', [])
        for line in bus_lines:
            all_lines.add(line.split('(')[0])

    all_lines = sorted(all_lines)
    matrix = pd.DataFrame(0, index=all_lines, columns=all_lines)

    for _, data in G_L.nodes(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = sorted(set(line.split('(')[0] for line in bus_lines))

        for i in range(len(unique_lines)):
            for j in range(i + 1, len(unique_lines)):
                matrix.loc[unique_lines[i], unique_lines[j]] += 1
                matrix.loc[unique_lines[j], unique_lines[i]] += 1

    return matrix


def transfer_summary(G_L: nx.Graph) -> Dict[str, Any]:
    """生成换乘分析综合摘要。

    Args:
        G_L: Space-L 网络图。

    Returns:
        字典，包含换乘站点统计、线路关联度等综合指标。
    """
    transfer_df = identify_transfer_stations(G_L, min_lines=2)
    reach = direct_reach_rate(G_L)

    total_nodes = G_L.number_of_nodes()
    transfer_count = len(transfer_df)

    level_counts = {}
    if not transfer_df.empty:
        level_counts = transfer_df['level'].value_counts().to_dict()

    avg_lines = transfer_df['line_count'].mean() if not transfer_df.empty else 0
    max_lines = transfer_df['line_count'].max() if not transfer_df.empty else 0

    return {
        'total_stations': total_nodes,
        'transfer_stations': transfer_count,
        'transfer_ratio': transfer_count / total_nodes if total_nodes > 0 else 0,
        'hub_count': level_counts.get('枢纽站', 0),
        'major_transfer_count': level_counts.get('重要换乘站', 0),
        'minor_transfer_count': level_counts.get('一般换乘站', 0),
        'avg_lines_per_transfer': round(avg_lines, 2),
        'max_lines_at_station': max_lines,
        'direct_rate': reach['direct_rate'],
        'one_transfer_rate': reach['one_transfer_rate'],
    }
