"""网络韧性与脆弱性分析模块。

分析公交网络在站点或线路中断时的抗风险能力：
    - 关键节点识别：找出瘫痪后影响最大的站点
    - 失效模拟：模拟站点/线路关闭对网络连通性的影响
    - 冗余度分析：识别仅被单条线路服务的脆弱区域
    - 网络拓扑指标：综合评估网络结构的健壮性

典型用法::

    from BusNetPynew.resilience import (
        critical_nodes, simulate_node_failure,
        redundancy_analysis, network_robustness
    )

    ranking = critical_nodes(G_L)
    impact = simulate_node_failure(G_L, ['s1', 's2'])
    weak = redundancy_analysis(G_L)
"""

from typing import Any, Dict, List

import networkx as nx
import numpy as np
import pandas as pd


def critical_nodes(
    G_L: nx.Graph,
    top_n: int = 20,
) -> pd.DataFrame:
    """识别网络中的关键节点（站点）。

    综合使用介数中心性、度中心性和接近中心性来评估每个站点的
    关键程度。关键节点一旦瘫痪，对网络连通性影响最大。

    Args:
        G_L: Space-L 网络图。
        top_n: 返回前 N 个最关键节点，默认 20。

    Returns:
        DataFrame，包含：
            - node_id: 站点 ID
            - staname: 站点名称
            - betweenness: 介数中心性（越高越关键）
            - degree: 度中心性
            - closeness: 接近中心性
            - line_count: 经过线路数
            - critical_score: 综合关键度评分（0~100）
        按 critical_score 降序排列。

    Examples:
        >>> df = critical_nodes(G_L, top_n=10)
        >>> print("最关键站点:", df.iloc[0]['staname'])
    """
    betweenness = nx.betweenness_centrality(G_L, weight='length')
    degree = nx.degree_centrality(G_L)
    closeness = nx.closeness_centrality(G_L, distance='length')

    rows = []
    for node, data in G_L.nodes(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = set(line.split('(')[0] for line in bus_lines)

        b = betweenness.get(node, 0)
        d = degree.get(node, 0)
        c = closeness.get(node, 0)

        score = b * 50 + d * 30 + c * 20

        rows.append({
            'node_id': node,
            'staname': data.get('staname', ''),
            'betweenness': round(b, 6),
            'degree': round(d, 6),
            'closeness': round(c, 6),
            'line_count': len(unique_lines),
            'critical_score': round(score * 100, 2),
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        max_score = df['critical_score'].max()
        if max_score > 0:
            df['critical_score'] = (df['critical_score'] / max_score * 100).round(2)
        df = df.sort_values('critical_score', ascending=False).reset_index(drop=True)

    return df.head(top_n)


def simulate_node_failure(
    G_L: nx.Graph,
    failed_nodes: List[Any],
) -> Dict[str, Any]:
    """模拟站点失效对网络的影响。

    移除指定站点后，分析网络连通性的变化。

    Args:
        G_L: Space-L 网络图。
        failed_nodes: 模拟失效的站点 ID 列表。

    Returns:
        字典，包含：
            - original_components: 原始连通分量数
            - after_components: 失效后连通分量数
            - component_increase: 连通分量增加数
            - original_largest: 原始最大连通分量大小
            - after_largest: 失效后最大连通分量大小
            - largest_shrink_ratio: 最大连通分量缩减比例
            - isolated_nodes: 因失效而孤立的站点列表
            - affected_lines: 受影响的线路列表
            - severity: 影响严重程度评级

    Examples:
        >>> impact = simulate_node_failure(G_L, ['s1'])
        >>> print(f"严重程度: {impact['severity']}")
    """
    original_components = nx.number_connected_components(G_L)
    original_largest = max(len(c) for c in nx.connected_components(G_L))

    affected_lines = set()
    for node in failed_nodes:
        if node in G_L.nodes:
            lines = G_L.nodes[node].get('bus_lines', [])
            for line in lines:
                affected_lines.add(line.split('(')[0])

    G_after = G_L.copy()
    for node in failed_nodes:
        if node in G_after.nodes:
            G_after.remove_node(node)

    if G_after.number_of_nodes() == 0:
        return {
            'original_components': original_components,
            'after_components': 0,
            'component_increase': -original_components,
            'original_largest': original_largest,
            'after_largest': 0,
            'largest_shrink_ratio': 1.0,
            'isolated_nodes': [],
            'affected_lines': sorted(affected_lines),
            'severity': '灾难性',
        }

    after_components = nx.number_connected_components(G_after)
    after_largest = max(len(c) for c in nx.connected_components(G_after))

    isolated = [
        n for n in G_after.nodes()
        if G_after.degree(n) == 0
    ]

    shrink = 1 - after_largest / original_largest if original_largest > 0 else 0

    if shrink > 0.5:
        severity = '严重'
    elif shrink > 0.2:
        severity = '较大'
    elif after_components > original_components:
        severity = '中等'
    else:
        severity = '轻微'

    return {
        'original_components': original_components,
        'after_components': after_components,
        'component_increase': after_components - original_components,
        'original_largest': original_largest,
        'after_largest': after_largest,
        'largest_shrink_ratio': round(shrink, 4),
        'isolated_nodes': isolated,
        'affected_lines': sorted(affected_lines),
        'severity': severity,
    }


def simulate_line_failure(
    G_L: nx.Graph,
    failed_line: str,
) -> Dict[str, Any]:
    """模拟整条线路停运对网络的影响。

    移除仅被该线路服务的边后，分析网络连通性变化。

    Args:
        G_L: Space-L 网络图。
        failed_line: 停运的线路名称（如 '1路'）。

    Returns:
        与 simulate_node_failure 相同格式的影响评估字典，
        额外包含 removed_edges 字段。
    """
    original_components = nx.number_connected_components(G_L)
    original_largest = max(len(c) for c in nx.connected_components(G_L))

    G_after = G_L.copy()
    edges_to_remove = []

    for u, v, data in G_after.edges(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = set(line.split('(')[0] for line in bus_lines)
        remaining = unique_lines - {failed_line}
        if not remaining:
            edges_to_remove.append((u, v))

    G_after.remove_edges_from(edges_to_remove)

    isolated = [n for n in G_after.nodes() if G_after.degree(n) == 0]

    if G_after.number_of_edges() == 0 and G_after.number_of_nodes() > 0:
        after_components = G_after.number_of_nodes()
        after_largest = 1
    else:
        after_components = nx.number_connected_components(G_after)
        after_largest = max(len(c) for c in nx.connected_components(G_after)) if G_after.number_of_nodes() > 0 else 0

    shrink = 1 - after_largest / original_largest if original_largest > 0 else 0

    if shrink > 0.5:
        severity = '严重'
    elif shrink > 0.2:
        severity = '较大'
    elif after_components > original_components:
        severity = '中等'
    else:
        severity = '轻微'

    return {
        'failed_line': failed_line,
        'removed_edges': len(edges_to_remove),
        'original_components': original_components,
        'after_components': after_components,
        'component_increase': after_components - original_components,
        'original_largest': original_largest,
        'after_largest': after_largest,
        'largest_shrink_ratio': round(shrink, 4),
        'isolated_nodes': isolated,
        'severity': severity,
    }


def redundancy_analysis(
    G_L: nx.Graph,
) -> Dict[str, Any]:
    """分析网络冗余度，识别脆弱路段和站点。

    找出仅被单条线路服务的边（一旦该线路中断即断联）
    和桥边/割点（移除后网络断裂）。

    Args:
        G_L: Space-L 网络图。

    Returns:
        字典，包含：
            - single_line_edges: 仅被一条线路服务的边列表
            - single_line_ratio: 单线路服务边的比例
            - bridges: 桥边列表（移除后网络断裂的边）
            - bridge_count: 桥边数量
            - articulation_points: 割点列表（移除后网络断裂的节点）
            - articulation_count: 割点数量
            - avg_redundancy: 平均冗余度（每条边的平均服务线路数）
    """
    single_line_edges = []
    total_line_counts = []

    for u, v, data in G_L.edges(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = set(line.split('(')[0] for line in bus_lines)
        count = len(unique_lines)
        total_line_counts.append(count)

        if count == 1:
            single_line_edges.append({
                'from_id': u,
                'to_id': v,
                'from_station': G_L.nodes[u].get('staname', ''),
                'to_station': G_L.nodes[v].get('staname', ''),
                'line': list(unique_lines)[0],
            })

    bridges = list(nx.bridges(G_L))
    bridge_details = []
    for u, v in bridges:
        bridge_details.append({
            'from_id': u,
            'to_id': v,
            'from_station': G_L.nodes[u].get('staname', ''),
            'to_station': G_L.nodes[v].get('staname', ''),
        })

    articulation = list(nx.articulation_points(G_L))
    articulation_details = [
        {'node_id': n, 'staname': G_L.nodes[n].get('staname', '')}
        for n in articulation
    ]

    total_edges = G_L.number_of_edges()
    avg_redundancy = np.mean(total_line_counts) if total_line_counts else 0

    return {
        'single_line_edges': pd.DataFrame(single_line_edges),
        'single_line_ratio': len(single_line_edges) / total_edges if total_edges > 0 else 0,
        'bridges': pd.DataFrame(bridge_details),
        'bridge_count': len(bridges),
        'articulation_points': pd.DataFrame(articulation_details),
        'articulation_count': len(articulation),
        'avg_redundancy': round(avg_redundancy, 2),
    }


def network_robustness(
    G_L: nx.Graph,
    attack_mode: str = 'targeted',
    max_removals: int = None,
) -> pd.DataFrame:
    """评估网络在渐进式攻击下的健壮性。

    逐步移除节点，记录网络最大连通分量的衰减过程。

    Args:
        G_L: Space-L 网络图。
        attack_mode: 攻击模式：
            - 'targeted': 按介数中心性从高到低移除（恶意攻击）
            - 'random': 随机移除（随机故障）
        max_removals: 最大移除节点数，默认为节点数的 30%。

    Returns:
        DataFrame，记录每步移除后的网络状态：
            - step: 步数
            - removed_node: 移除的节点
            - removed_station: 移除的站名
            - remaining_nodes: 剩余节点数
            - largest_component: 最大连通分量大小
            - largest_ratio: 最大连通分量占比
            - components: 连通分量数
    """
    G = G_L.copy()
    n = G.number_of_nodes()

    if max_removals is None:
        max_removals = max(1, int(n * 0.3))

    results = [{
        'step': 0,
        'removed_node': None,
        'removed_station': '',
        'remaining_nodes': n,
        'largest_component': max(len(c) for c in nx.connected_components(G)),
        'largest_ratio': 1.0,
        'components': nx.number_connected_components(G),
    }]

    for step in range(1, max_removals + 1):
        if G.number_of_nodes() == 0:
            break

        if attack_mode == 'targeted':
            bc = nx.betweenness_centrality(G, weight='length')
            target = max(bc, key=bc.get)
        else:
            target = np.random.choice(list(G.nodes()))

        sta_name = G.nodes[target].get('staname', '')
        G.remove_node(target)

        if G.number_of_nodes() == 0:
            largest = 0
            components = 0
        else:
            largest = max(len(c) for c in nx.connected_components(G))
            components = nx.number_connected_components(G)

        results.append({
            'step': step,
            'removed_node': target,
            'removed_station': sta_name,
            'remaining_nodes': G.number_of_nodes(),
            'largest_component': largest,
            'largest_ratio': round(largest / n, 4),
            'components': components,
        })

    return pd.DataFrame(results)
