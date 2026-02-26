"""网络分析指标计算模块。

提供公交网络的核心分析功能，包括：
    - 非直线系数（Nonline）：衡量线路弯曲程度
    - 平均站间距（avg_station）：各线路站点间平均距离
    - 重复系数（cf_all）：线路重叠程度
    - Space-L / Space-P 网络构建
    - 最大共线边 / 最多线路站点分析
    - 最近节点查找

参考标准：《城市道路交通规划设计规范 GB50220-95》

典型用法::

    from BusNetPynew.metrical import spaceL, Nonline, avg_station, cf_all

    G_L, pos = spaceL(gdf_route)
    base, cycle, fzxxs_base, fzxxs_hx = Nonline(gdf_route, 'base.csv', 'hx.csv')
"""

import math
from typing import Tuple, Optional, List, Dict, Any

import pandas as pd
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt

from .utils import (
    haversine_distance,
    extract_endpoint_coords,
    get_utm_epsg,
)


def _ensure_endpoint_coords(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """确保 GeoDataFrame 包含起止点坐标和直线距离列。

    如果 zx_dis 列不存在，自动提取起止点坐标并计算直线距离。

    Args:
        gdf: 含 LineString 几何列的 GeoDataFrame。

    Returns:
        含 lng, lat, lng_y, lat_y, zx_dis 列的 GeoDataFrame。
    """
    if 'zx_dis' not in gdf.columns:
        gdf = extract_endpoint_coords(gdf)
    return gdf


def _compute_nonline(
    gdf: gpd.GeoDataFrame,
    base_path: Optional[str] = None,
    hx_path: Optional[str] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, float, float]:
    """非直线系数核心计算逻辑。

    Args:
        gdf: 已包含 hx, zx_dis 列的投影坐标 GeoDataFrame。
        base_path: 非环线结果 CSV 保存路径。
        hx_path: 环线结果 CSV 保存路径。

    Returns:
        (base_line, fzxxs_hx, result_fzxxs_base, result_fzxxs_hx)
        分别为非环线数据、环线数据、非环线非直线系数均值、环线非直线系数均值。
    """
    gdf = _ensure_endpoint_coords(gdf)

    sum_line = gdf.groupby('name')[['hx']].sum().reset_index()
    sum_line['route_zx_dis'] = None

    for index, row in sum_line.iterrows():
        line_data = gdf[gdf['name'] == row['name']]
        if line_data.iloc[0]['id'] == line_data.iloc[0]['next_id']:
            sum_line.at[index, 'route_zx_dis'] = 0
        else:
            first_row = line_data.iloc[0]
            last_row = line_data.iloc[-1]
            sum_line.at[index, 'route_zx_dis'] = math.sqrt(
                math.pow(first_row['lng'] - last_row['lng_y'], 2)
                + math.pow(first_row['lat'] - last_row['lat_y'], 2)
            ) / 1000

    sum_line['fzxxs_base'] = sum_line.apply(
        lambda row: row['hx'] / row['route_zx_dis'] if row['route_zx_dis'] > 1 else 0,
        axis=1,
    )

    fzxxs_hx = sum_line[sum_line['fzxxs_base'] == 0].copy()

    def hx_fzx(row: pd.Series) -> float:
        line_data = gdf[gdf['name'] == row['name']]
        cs = line_data.groupby('name')['hx'].sum() / line_data.groupby('name')['zx_dis'].sum()
        return cs.iloc[0]

    if not fzxxs_hx.empty:
        fzxxs_hx['fzxxs_hx'] = fzxxs_hx.apply(hx_fzx, axis=1)

    result_fzxxs_base = sum_line[sum_line['fzxxs_base'] != 0]['fzxxs_base'].mean()
    result_fzxxs_hx = fzxxs_hx['fzxxs_hx'].mean() if not fzxxs_hx.empty else 0.0

    base_line = sum_line[sum_line['fzxxs_base'] != 0]

    if base_path:
        base_line.to_csv(base_path, encoding='utf-8')
    if hx_path:
        fzxxs_hx.to_csv(hx_path, encoding='utf-8')

    return base_line, fzxxs_hx, result_fzxxs_base, result_fzxxs_hx


def Nonline(
    gdf: gpd.GeoDataFrame,
    base_path: Optional[str] = None,
    hx_path: Optional[str] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame, float, float]:
    """计算公交线网非直线系数。

    非直线系数 = 线路实际长度 / 起终点直线距离。
    根据 GB50220-95 规范，单条线路不应大于 1.4，全网均值以 1.15～1.2 为宜。

    对于环线（起终点相同或距离极近），使用分段累计计算非直线系数。

    自动处理 WGS-84 (EPSG:4326) 坐标系的投影转换。

    Args:
        gdf: 结构化公交线网 GeoDataFrame，含 hx, name, id, next_id 等列。
        base_path: 非环线结果 CSV 保存路径，可选。
        hx_path: 环线结果 CSV 保存路径，可选。

    Returns:
        (base_line, fzxxs_hx, result_fzxxs_base, result_fzxxs_hx) 元组：
            - base_line: 非环线数据 DataFrame
            - fzxxs_hx: 环线数据 DataFrame
            - result_fzxxs_base: 非环线非直线系数均值
            - result_fzxxs_hx: 环线非直线系数均值
    """
    if gdf.crs.to_epsg() == 4326:
        gdf = gdf.to_crs(epsg=3857)

    return _compute_nonline(gdf, base_path, hx_path)


def avg_station(
    gdf: gpd.GeoDataFrame,
    file_path: Optional[str] = None,
) -> pd.DataFrame:
    """计算各线路的平均站间距。

    Args:
        gdf: 结构化公交线网 GeoDataFrame，含 hx, name 等列。
        file_path: 结果 CSV 保存路径，可选。

    Returns:
        各线路平均站间距 DataFrame，按站间距升序排列。
    """
    if gdf.crs.to_epsg() == 4326:
        gdf = gdf.to_crs(3857)

    gdf = _ensure_endpoint_coords(gdf)

    avg_sta = gdf.groupby('name')['hx'].mean().reset_index().sort_values('hx')
    if file_path:
        avg_sta.to_csv(file_path, encoding='utf-8')
    return avg_sta


def get_utm_epsg_code(longitude: float, latitude: float) -> str:
    """根据经纬度获取 UTM 投影的 EPSG 代码。

    Args:
        longitude: 经度（十进制度）。
        latitude: 纬度（十进制度）。

    Returns:
        EPSG 代码字符串。

    Examples:
        >>> get_utm_epsg_code(116.4, 39.9)
        '32650'
    """
    return get_utm_epsg(longitude, latitude)


def spaceL(
    gdf: gpd.GeoDataFrame,
) -> Tuple[nx.Graph, Dict[str, Tuple[float, float]]]:
    """构建 Space-L 拓扑网络。

    Space-L 网络中，只有相邻站点之间存在边，保留公交线路的
    地理拓扑关系。每个节点存储站名和经过的公交线路列表，
    每条边存储线段长度和经过的公交线路列表。

    Args:
        gdf: 结构化公交线网 GeoDataFrame，含 id, next_id, stationname,
             nt_stationname, lng, lat, lng_y, lat_y, name, hx 等列。

    Returns:
        (G_L, pos) 元组：
            - G_L: Space-L 网络图（NetworkX Graph）
            - pos: 节点位置字典 {node_id: (lng, lat)}

    Examples:
        >>> G_L, pos = spaceL(gdf_route)
        >>> G_L.number_of_nodes()
        120
    """
    G_L = nx.Graph()
    pos = {}

    for _, row in gdf.iterrows():
        if G_L.has_node(row['id']):
            G_L.nodes[row['id']]['bus_lines'].append(row['name'])
        else:
            G_L.add_node(
                row['id'],
                pos=(row['lng'], row['lat']),
                staname=row['stationname'],
                bus_lines=[row['name']],
            )
        pos[row['id']] = (row['lng'], row['lat'])

    for _, row in gdf.iterrows():
        if not G_L.has_node(row['next_id']):
            G_L.add_node(
                row['next_id'],
                pos=(row['lng_y'], row['lat_y']),
                staname=row['nt_stationname'],
                bus_lines=[row['name']],
            )
        else:
            if row['name'] not in G_L.nodes[row['next_id']]['bus_lines']:
                G_L.nodes[row['next_id']]['bus_lines'].append(row['name'])
        pos[row['next_id']] = (row['lng_y'], row['lat_y'])

        if G_L.has_edge(row['id'], row['next_id']):
            if row['name'] not in G_L[row['id']][row['next_id']]['bus_lines']:
                G_L[row['id']][row['next_id']]['bus_lines'].append(row['name'])
        else:
            G_L.add_edges_from([
                (row['id'], row['next_id'])
            ], length=row['hx'], bus_lines=[row['name']])

    return G_L, pos


def G_ksh(G_L: nx.Graph, pos: Dict[str, Tuple[float, float]]) -> None:
    """可视化 Space-L 网络拓扑图。

    Args:
        G_L: Space-L 网络图。
        pos: 节点位置字典 {node_id: (lng, lat)}。
    """
    plt.figure(figsize=(10, 8))
    nx.draw(G_L, pos, node_size=0.1, node_color='blue', with_labels=False)
    plt.show()


def unique_line(G_L: nx.Graph) -> List[str]:
    """查找网络中共线线路最多的站点区间。

    遍历所有边，找到经过公交线路最多的边，返回去重后的线路名称列表。

    Args:
        G_L: Space-L 网络图。

    Returns:
        共线线路名称列表（已去重、已去除正反线路标识）。
    """
    max_bus_lines = 0
    edge_with_max_bus_lines = None

    for edge in G_L.edges(data=True):
        current_bus_lines = edge[2].get('bus_lines', [])
        if len(current_bus_lines) > max_bus_lines:
            max_bus_lines = len(current_bus_lines)
            edge_with_max_bus_lines = edge

    if not edge_with_max_bus_lines:
        return []

    result_line = [item.split('(')[0] for item in edge_with_max_bus_lines[2]['bus_lines']]
    unique_list_line = list(set(result_line))

    return unique_list_line


def most_linesta(G_L: nx.Graph) -> Optional[str]:
    """查找网络中经过公交线路最多的站点。

    Args:
        G_L: Space-L 网络图。

    Returns:
        经过线路最多的站点名称，若无节点则返回 None。
    """
    max_lines_count = 0
    node_with_max_sta = None

    for node, attrs in G_L.nodes(data=True):
        bus_lines = attrs.get('bus_lines', [])
        if len(bus_lines) > max_lines_count:
            max_lines_count = len(bus_lines)
            node_with_max_sta = node

    if node_with_max_sta is None:
        return None

    return G_L.nodes[node_with_max_sta]['staname']


def cf_all(G_L: nx.Graph, gdf: gpd.GeoDataFrame) -> float:
    """计算公交线网重复系数。

    重复系数 = 实际运营总里程 / 线网拓扑总长度。
    反映线路之间的重叠程度，值越大表示线路重叠越多。

    Args:
        G_L: Space-L 网络图。
        gdf: 结构化公交线网 GeoDataFrame，含 hx 列。

    Returns:
        重复系数值。

    Examples:
        >>> cf = cf_all(G_L, gdf_route)
        >>> cf > 1.0
        True
    """
    total_length = 0
    for u, v, data in G_L.edges(data=True):
        total_length += data.get('length', 0)
    return gdf['hx'].sum() / total_length


def spacep(
    df_point: pd.DataFrame,
    gdf: gpd.GeoDataFrame,
) -> nx.Graph:
    """构建 Space-P 拓扑网络。

    Space-P 网络中，同一条线路上的任意两个站点之间都存在边，
    边权重为两站之间的实际线路距离。该模型体现了乘客的可达性。

    Args:
        df_point: 站点 DataFrame，含 lng, lat, id, 站点名称 列。
        gdf: 结构化公交线网 GeoDataFrame，含 name, id, next_id, hx 列。

    Returns:
        Space-P 网络图（NetworkX Graph）。
    """
    id_df = df_point[['lng', 'lat', 'id', '站点名称']]

    G_p = nx.Graph()

    for _, row in id_df.iterrows():
        G_p.add_node(row['id'], pos=(row['lng'], row['lat']), staname=row['站点名称'])

    for name in gdf['name'].unique():
        route = gdf[gdf['name'] == name]
        result = {}

        for index, row in route.iterrows():
            node_id = row['id']
            for index_nt, row_nt in route.iterrows():
                if index_nt >= index:
                    next_node_id = row_nt['next_id']
                    length = route.loc[index:index_nt]['hx'].sum()
                    result[(node_id, next_node_id)] = length

        for (u, v), length in result.items():
            G_p.add_edge(u, v, length=length, line_name=name)

    return G_p


def ycl_gdf(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """从 GeoDataFrame 中提取起止点坐标并计算直线距离。

    为兼容旧代码保留的接口，内部调用 utils.extract_endpoint_coords。

    Args:
        gdf: 含 LineString 几何列的 GeoDataFrame。

    Returns:
        添加了坐标和距离列的 GeoDataFrame。
    """
    return extract_endpoint_coords(gdf)


def route_to_84(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """将非 WGS-84 坐标的 GeoDataFrame 转换为 WGS-84。

    Args:
        gdf: 结构化公交线网 GeoDataFrame（任意投影坐标系）。

    Returns:
        WGS-84 坐标系的 GeoDataFrame，包含更新后的起止点坐标。
    """
    gdf = gdf.to_crs(epsg=4326)
    gdf = extract_endpoint_coords(gdf)
    return gdf


def find_nearest_node(
    G: nx.Graph,
    longitude: float,
    latitude: float,
) -> Tuple[Any, str, float]:
    """在图网络中查找距给定经纬度最近的节点。

    Args:
        G: 含 pos=(lng, lat) 和 staname 节点属性的 NetworkX 图。
        longitude: 查询点经度。
        latitude: 查询点纬度。

    Returns:
        (node_id, station_name, distance_km) 元组。

    Examples:
        >>> node_id, name, dist = find_nearest_node(G_L, 116.4, 39.9)
    """
    min_distance = float('inf')
    nearest_sta = None
    node_t = None

    for node, data in G.nodes(data=True):
        node_lat = data['pos'][1]
        node_lon = data['pos'][0]
        distance = haversine_distance(latitude, longitude, node_lat, node_lon)

        if distance < min_distance:
            min_distance = distance
            nearest_sta = data['staname'] + '站'
            node_t = node

    return node_t, nearest_sta, min_distance
