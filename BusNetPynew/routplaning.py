"""公交路径规划模块。

基于 Space-P 和 Space-L 网络的公交出行最短路径规划，
支持换乘方案计算和路径几何提取。

典型用法::

    from BusNetPynew.routplaning import bus_route_planning
    from BusNetPynew.metrical import find_nearest_node

    node1, _, _ = find_nearest_node(G_L, 112.97, 28.23)
    node2, _, _ = find_nearest_node(G_L, 113.02, 28.19)
    stations, path_gdf, length = bus_route_planning(G_P, G_L, node1, node2, gdf)
"""

from typing import List, Tuple, Any

import geopandas as gpd
import networkx as nx
import pandas as pd


def GP_planning(G_P: nx.Graph, node1: Any, node2: Any) -> List[Any]:
    """使用 Space-P 网络进行公交路径规划。

    采用自定义权重函数，在边权重基础上为换乘（站点名称不同的节点间切换）
    增加惩罚值，从而优化换乘次数。

    Args:
        G_P: Space-P 网络图。
        node1: 起始节点 ID。
        node2: 目标节点 ID。

    Returns:
        最短路径上的节点 ID 列表。

    Raises:
        nx.NetworkXNoPath: 当起终点之间不存在路径时。
    """
    def custom_weight(u: Any, v: Any, d: dict) -> float:
        edge_weight = G_P[u][v].get('length', 1)
        u_name = G_P.nodes[u].get('staname')
        v_name = G_P.nodes[v].get('staname')
        switch_penalty = 3 if u_name != v_name else 0
        return edge_weight + switch_penalty

    try:
        nodes = nx.shortest_path(G_P, source=node1, target=node2, weight=custom_weight)
    except nx.NetworkXNoPath:
        raise nx.NetworkXNoPath(f"从节点 {node1} 到节点 {node2} 没有路径。")
    return nodes


def route_sta_analy(G_P: nx.Graph, nodes: List[Any]) -> List[str]:
    """提取路径上经过的站点名称列表。

    Args:
        G_P: Space-P 网络图。
        nodes: 路径节点 ID 列表。

    Returns:
        站点名称列表。
    """
    staname_list = []
    for node in nodes:
        attrs = G_P.nodes[node]
        staname = attrs.get('staname')
        if staname:
            staname_list.append(staname)
    return staname_list


def route_linena_analy(G_P: nx.Graph, nodes: List[Any]) -> List[str]:
    """提取路径上经过的线路名称列表。

    Args:
        G_P: Space-P 网络图。
        nodes: 路径节点 ID 列表。

    Returns:
        线路名称列表（与路径边一一对应）。
    """
    linename_list = []
    for i in range(len(nodes) - 1):
        start_node = nodes[i]
        end_node = nodes[i + 1]
        edge_attributes = G_P.edges[start_node, end_node]
        line_name = edge_attributes.get('line_name')
        if line_name:
            linename_list.append(line_name)
    return linename_list


def filtered_edges(G_L: nx.Graph, linename_list: List[str]) -> nx.Graph:
    """从 Space-L 网络中筛选指定线路的子图。

    Args:
        G_L: Space-L 网络图。
        linename_list: 需要保留的线路名称列表。

    Returns:
        仅包含指定线路边的子图。
    """
    G_filtered = nx.Graph()

    for u, v, data in G_L.edges(data=True):
        bus_lines = data.get('bus_lines', [])
        for line_name in bus_lines:
            if line_name in linename_list:
                G_filtered.add_edge(u, v, **data)
                break

    return G_filtered


def busroute_result(
    G_filtered: nx.Graph,
    node1: Any,
    node2: Any,
    gdf: gpd.GeoDataFrame,
    linename_list: List[str],
) -> Tuple[gpd.GeoDataFrame, float]:
    """从筛选后的网络中提取最终路径几何。

    Args:
        G_filtered: 筛选后的 Space-L 子图。
        node1: 起始节点 ID。
        node2: 目标节点 ID。
        gdf: 结构化公交线网 GeoDataFrame。
        linename_list: 路径涉及的线路名称列表。

    Returns:
        (path_gdf, length) 元组：
            - path_gdf: 路径段 GeoDataFrame，含 stationname, nt_stationname, geometry。
            - length: 路径加权总长度。
    """
    shortest_path_nodes = nx.shortest_path(G_filtered, source=node1, target=node2)
    length = nx.shortest_path_length(G_filtered, source=node1, target=node2, weight='length')

    segments = []
    for i in range(len(shortest_path_nodes) - 1):
        sub_path = nx.shortest_path(
            G_filtered, source=shortest_path_nodes[i], target=shortest_path_nodes[i + 1]
        )
        for j in range(len(sub_path) - 1):
            start_node = sub_path[j]
            end_node = sub_path[j + 1]

            segment = gdf[
                (gdf['name'].isin(linename_list))
                & (gdf['id'] == start_node)
                & (gdf['next_id'] == end_node)
            ]
            if not segment.empty:
                segments.append(segment.iloc[:1])
            else:
                segment = gdf[
                    (gdf['next_id'] == start_node) & (gdf['id'] == end_node)
                ]
                if not segment.empty:
                    segments.append(segment.iloc[:1])

    path_gdf = gpd.GeoDataFrame(pd.concat(segments, ignore_index=True))
    path_gdf = path_gdf[['stationname', 'nt_stationname', 'geometry']]
    return path_gdf, length


def bus_route_planning(
    G_P: nx.Graph,
    G_L: nx.Graph,
    node1: Any,
    node2: Any,
    gdf: gpd.GeoDataFrame,
) -> Tuple[List[str], gpd.GeoDataFrame, float]:
    """完整的公交路径规划流程。

    整合 Space-P 路径搜索、线路筛选和几何提取，输出完整的
    公交出行方案。

    Args:
        G_P: Space-P 网络图。
        G_L: Space-L 网络图。
        node1: 起始节点 ID。
        node2: 目标节点 ID。
        gdf: 结构化公交线网 GeoDataFrame。

    Returns:
        (staname_list, path_gdf, length) 元组：
            - staname_list: 经过的站点名称列表
            - path_gdf: 路径几何 GeoDataFrame
            - length: 路径总长度（千米）

    Examples:
        >>> stations, path, dist = bus_route_planning(G_P, G_L, "s1", "s10", gdf)
    """
    nodes = GP_planning(G_P, node1, node2)
    staname_list = route_sta_analy(G_P, nodes)
    linename_list = route_linena_analy(G_P, nodes)
    G_filtered = filtered_edges(G_L, linename_list)
    path_gdf, length = busroute_result(G_filtered, node1, node2, gdf, linename_list)
    return staname_list, path_gdf, length
