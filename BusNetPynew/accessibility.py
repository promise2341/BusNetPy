"""公交可达性分析模块。

提供基于公交网络的可达性分析功能：
    - 等时圈分析：给定起点和时间阈值，计算公交可达范围
    - 站点覆盖率：城市中公交站点的空间覆盖情况
    - 出行时间矩阵：任意站点对之间的出行时间

典型用法::

    from BusNetPynew.accessibility import isochrone, coverage_rate, travel_time_matrix

    reachable = isochrone(G_L, start_node='s1', time_limit=30)
    rate = coverage_rate(gdf_stops, boundary, radius_m=500)
    matrix = travel_time_matrix(G_L, speed_kmh=20)
"""

from typing import Dict, List, Any

import geopandas as gpd
import networkx as nx
import pandas as pd
from shapely.geometry import MultiPoint, Point
from shapely.ops import unary_union


def isochrone(
    G: nx.Graph,
    start_node: Any,
    time_limit: float = 30.0,
    speed_kmh: float = 20.0,
    walk_speed_kmh: float = 5.0,
    walk_radius_km: float = 0.5,
) -> Dict[str, Any]:
    """等时圈分析：计算从起点出发在指定时间内可达的站点集合。

    基于 Dijkstra 算法，以时间为权重搜索可达节点。
    线路上按公交速度计算，步行接驳按步行速度计算。

    Args:
        G: Space-L 网络图，边需含 length（千米）属性。
        start_node: 起始站点节点 ID。
        time_limit: 时间阈值（分钟），默认 30。
        speed_kmh: 公交平均速度（千米/小时），默认 20。
        walk_speed_kmh: 步行速度（千米/小时），默认 5。
        walk_radius_km: 起终点步行接驳半径（千米），默认 0.5。

    Returns:
        字典，包含：
            - reachable_nodes: 可达节点 ID 列表
            - reachable_details: DataFrame，含节点 ID、站名、到达时间（分钟）
            - coverage_polygon: 可达范围凸包多边形（Shapely Polygon），可能为 None
            - total_reachable: 可达站点数量
            - time_limit: 使用的时间阈值

    Examples:
        >>> result = isochrone(G_L, 's1', time_limit=30)
        >>> print(f"30 分钟内可达 {result['total_reachable']} 个站点")
    """
    walk_time = (walk_radius_km / walk_speed_kmh) * 60
    available_time = time_limit - walk_time

    if available_time <= 0:
        return {
            'reachable_nodes': [start_node],
            'reachable_details': pd.DataFrame(),
            'coverage_polygon': None,
            'total_reachable': 1,
            'time_limit': time_limit,
        }

    time_weight = {}
    for u, v, data in G.edges(data=True):
        dist_km = data.get('length', 0)
        travel_min = (dist_km / speed_kmh) * 60 if speed_kmh > 0 else float('inf')
        time_weight[(u, v)] = travel_min

    nx.set_edge_attributes(G, {(u, v): w for (u, v), w in time_weight.items()}, '_travel_time')

    try:
        lengths = nx.single_source_dijkstra_path_length(
            G, start_node, cutoff=available_time, weight='_travel_time'
        )
    except nx.NodeNotFound:
        return {
            'reachable_nodes': [],
            'reachable_details': pd.DataFrame(),
            'coverage_polygon': None,
            'total_reachable': 0,
            'time_limit': time_limit,
        }

    details = []
    points = []
    for node, travel_time in lengths.items():
        node_data = G.nodes[node]
        total_time = travel_time + walk_time
        if total_time <= time_limit:
            details.append({
                'node_id': node,
                'staname': node_data.get('staname', ''),
                'travel_time_min': round(total_time, 2),
                'lng': node_data.get('pos', (0, 0))[0],
                'lat': node_data.get('pos', (0, 0))[1],
            })
            pos = node_data.get('pos')
            if pos:
                points.append(Point(pos[0], pos[1]))

    df = pd.DataFrame(details)
    if not df.empty:
        df = df.sort_values('travel_time_min').reset_index(drop=True)

    polygon = None
    if len(points) >= 3:
        polygon = MultiPoint(points).convex_hull
    elif len(points) == 2:
        polygon = MultiPoint(points).convex_hull
    elif len(points) == 1:
        polygon = points[0].buffer(0.005)

    return {
        'reachable_nodes': [d['node_id'] for d in details],
        'reachable_details': df,
        'coverage_polygon': polygon,
        'total_reachable': len(details),
        'time_limit': time_limit,
    }


def multi_isochrone(
    G: nx.Graph,
    start_node: Any,
    time_limits: List[float] = None,
    speed_kmh: float = 20.0,
) -> gpd.GeoDataFrame:
    """多级等时圈分析：同时计算多个时间阈值的可达范围。

    Args:
        G: Space-L 网络图。
        start_node: 起始站点节点 ID。
        time_limits: 时间阈值列表（分钟），默认 [15, 30, 45, 60]。
        speed_kmh: 公交平均速度（千米/小时）。

    Returns:
        GeoDataFrame，每行对应一个时间等级的等时圈多边形。

    Examples:
        >>> gdf = multi_isochrone(G_L, 's1', [15, 30, 60])
        >>> gdf.explore(column='time_limit', cmap='RdYlGn_r')
    """
    if time_limits is None:
        time_limits = [15, 30, 45, 60]

    rows = []
    for t in sorted(time_limits):
        result = isochrone(G, start_node, time_limit=t, speed_kmh=speed_kmh)
        poly = result['coverage_polygon']
        if poly is not None:
            rows.append({
                'time_limit': t,
                'reachable_count': result['total_reachable'],
                'geometry': poly,
            })

    if not rows:
        return gpd.GeoDataFrame(columns=['time_limit', 'reachable_count', 'geometry'])

    return gpd.GeoDataFrame(rows, crs='EPSG:4326')


def coverage_rate(
    gdf_stops: gpd.GeoDataFrame,
    boundary: gpd.GeoDataFrame,
    radius_m: float = 500.0,
) -> Dict[str, Any]:
    """计算公交站点在城市范围内的空间覆盖率。

    以每个站点为中心画圆（半径 radius_m），计算站点服务区域
    占城市总面积的比例。

    Args:
        gdf_stops: 站点 GeoDataFrame（Point 几何，EPSG:4326）。
        boundary: 城市边界 GeoDataFrame（Polygon 几何，EPSG:4326）。
        radius_m: 站点服务半径（米），默认 500。

    Returns:
        字典，包含：
            - coverage_ratio: 覆盖率（0~1）
            - covered_area_km2: 覆盖面积（平方千米）
            - total_area_km2: 城市总面积（平方千米）
            - coverage_geometry: 覆盖区域的几何对象
            - uncovered_geometry: 未覆盖区域的几何对象

    Examples:
        >>> result = coverage_rate(stops_gdf, city_boundary, radius_m=500)
        >>> print(f"覆盖率: {result['coverage_ratio']:.1%}")
    """
    stops_proj = gdf_stops.to_crs(epsg=3857)
    boundary_proj = boundary.to_crs(epsg=3857)

    buffers = stops_proj.geometry.buffer(radius_m)
    covered = unary_union(buffers)
    city_area = unary_union(boundary_proj.geometry)

    covered_in_city = covered.intersection(city_area)

    covered_area = covered_in_city.area / 1e6
    total_area = city_area.area / 1e6
    ratio = covered_area / total_area if total_area > 0 else 0

    uncovered = city_area.difference(covered_in_city)

    return {
        'coverage_ratio': ratio,
        'covered_area_km2': round(covered_area, 2),
        'total_area_km2': round(total_area, 2),
        'coverage_geometry': covered_in_city,
        'uncovered_geometry': uncovered,
    }


def travel_time_matrix(
    G: nx.Graph,
    speed_kmh: float = 20.0,
    nodes: List[Any] = None,
) -> pd.DataFrame:
    """计算站点之间的公交出行时间矩阵。

    基于 Space-L 网络的最短路径长度，转换为出行时间。

    Args:
        G: Space-L 网络图，边需含 length 属性。
        speed_kmh: 公交平均速度（千米/小时），默认 20。
        nodes: 需要计算的节点列表，默认 None 表示全部节点。

    Returns:
        出行时间矩阵 DataFrame（单位：分钟），行和列均为节点 ID。

    Examples:
        >>> matrix = travel_time_matrix(G_L, speed_kmh=20)
        >>> print(f"s1 到 s5 的出行时间: {matrix.loc['s1', 's5']:.1f} 分钟")
    """
    if nodes is None:
        nodes = list(G.nodes())

    matrix_data = {}
    for source in nodes:
        try:
            lengths = nx.single_source_dijkstra_path_length(G, source, weight='length')
            times = {
                target: (dist / speed_kmh) * 60
                for target, dist in lengths.items()
                if target in nodes
            }
            matrix_data[source] = times
        except nx.NodeNotFound:
            matrix_data[source] = {}

    df = pd.DataFrame(matrix_data).T
    df = df.reindex(index=nodes, columns=nodes)
    df = df.fillna(float('inf'))
    for n in nodes:
        if n in df.index and n in df.columns:
            df.loc[n, n] = 0.0

    return df.round(2)


def station_service_area(
    gdf_stops: gpd.GeoDataFrame,
    radius_m: float = 500.0,
    name_col: str = 'stationname',
) -> gpd.GeoDataFrame:
    """计算每个站点的服务区域（缓冲区）。

    Args:
        gdf_stops: 站点 GeoDataFrame。
        radius_m: 服务半径（米），默认 500。
        name_col: 站名列名。

    Returns:
        GeoDataFrame，几何列为缓冲区多边形。
    """
    stops_proj = gdf_stops.to_crs(epsg=3857)
    result = stops_proj.copy()
    result['geometry'] = result.geometry.buffer(radius_m)
    result['area_km2'] = result.geometry.area / 1e6
    return result.to_crs(epsg=4326)
