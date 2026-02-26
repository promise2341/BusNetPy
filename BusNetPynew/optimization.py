"""线网优化建议模块。

基于公交网络数据提供线路优化分析功能：
    - 重复路段识别：发现过度重叠的路段
    - 覆盖盲区检测：找出缺乏公交服务的区域
    - 站间距异常检测：发现站间距过长或过短的路段
    - 线路效率评估：综合评估各线路的运营效率
    - 末端延伸建议：分析线路终点的延伸潜力

典型用法::

    from BusNetPynew.optimization import (
        find_redundant_segments, detect_coverage_gaps,
        detect_spacing_anomalies, evaluate_route_efficiency
    )

    redundant = find_redundant_segments(G_L, threshold=5)
    gaps = detect_coverage_gaps(gdf_stops, boundary, grid_size=0.01)
    anomalies = detect_spacing_anomalies(gdf_route, min_km=0.2, max_km=2.0)
"""

from typing import Dict

import geopandas as gpd
import networkx as nx
import pandas as pd
from shapely.geometry import box
from shapely.ops import unary_union


def find_redundant_segments(
    G_L: nx.Graph,
    threshold: int = 5,
) -> pd.DataFrame:
    """识别公交线路过度重叠的路段。

    找出经过公交线路数量超过阈值的边（路段），这些路段可能
    存在资源浪费，可考虑优化调整。

    Args:
        G_L: Space-L 网络图。
        threshold: 重叠线路数量阈值，默认 5。

    Returns:
        DataFrame，包含：
            - from_station / to_station: 起止站名
            - from_id / to_id: 起止站 ID
            - line_count: 经过的线路数量（去重后）
            - lines: 经过的线路名称列表
            - length_km: 路段长度
        按 line_count 降序排列。

    Examples:
        >>> df = find_redundant_segments(G_L, threshold=5)
        >>> print(f"有 {len(df)} 个路段经过 5 条以上线路")
    """
    rows = []
    for u, v, data in G_L.edges(data=True):
        bus_lines = data.get('bus_lines', [])
        unique_lines = list(set(line.split('(')[0] for line in bus_lines))
        if len(unique_lines) >= threshold:
            rows.append({
                'from_id': u,
                'to_id': v,
                'from_station': G_L.nodes[u].get('staname', ''),
                'to_station': G_L.nodes[v].get('staname', ''),
                'line_count': len(unique_lines),
                'lines': unique_lines,
                'length_km': data.get('length', 0),
            })

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values('line_count', ascending=False).reset_index(drop=True)
    return df


def detect_coverage_gaps(
    gdf_stops: gpd.GeoDataFrame,
    boundary: gpd.GeoDataFrame,
    grid_size: float = 0.005,
    radius_m: float = 500.0,
) -> gpd.GeoDataFrame:
    """检测公交覆盖盲区。

    将城市范围网格化，找出没有被公交站点服务半径覆盖的网格单元。

    Args:
        gdf_stops: 站点 GeoDataFrame（Point 几何）。
        boundary: 城市边界 GeoDataFrame（Polygon 几何）。
        grid_size: 网格大小（经纬度单位），默认 0.005（约 500 米）。
        radius_m: 站点服务半径（米），默认 500。

    Returns:
        GeoDataFrame，表示未被覆盖的网格区域，含：
            - geometry: 网格多边形
            - center_lng / center_lat: 网格中心坐标

    Examples:
        >>> gaps = detect_coverage_gaps(stops, boundary)
        >>> print(f"发现 {len(gaps)} 个覆盖盲区网格")
    """
    city_bounds = boundary.total_bounds
    min_lng, min_lat, max_lng, max_lat = city_bounds

    stops_proj = gdf_stops.to_crs(epsg=3857)
    buffers = stops_proj.geometry.buffer(radius_m)
    covered = unary_union(buffers)

    covered_4326 = gpd.GeoSeries([covered], crs='EPSG:3857').to_crs('EPSG:4326').iloc[0]

    city_polygon = unary_union(boundary.geometry)

    gap_cells = []
    lng = min_lng
    while lng < max_lng:
        lat = min_lat
        while lat < max_lat:
            cell = box(lng, lat, lng + grid_size, lat + grid_size)
            center = cell.centroid

            if city_polygon.contains(center) and not covered_4326.contains(center):
                gap_cells.append({
                    'geometry': cell,
                    'center_lng': center.x,
                    'center_lat': center.y,
                })
            lat += grid_size
        lng += grid_size

    if not gap_cells:
        return gpd.GeoDataFrame(
            columns=['geometry', 'center_lng', 'center_lat'],
            crs='EPSG:4326',
        )

    return gpd.GeoDataFrame(gap_cells, crs='EPSG:4326')


def detect_spacing_anomalies(
    gdf: gpd.GeoDataFrame,
    min_km: float = 0.2,
    max_km: float = 2.0,
    hx_col: str = 'hx',
) -> Dict[str, pd.DataFrame]:
    """检测站间距异常的路段。

    找出站间距过短（< min_km）或过长（> max_km）的路段。

    Args:
        gdf: 结构化公交线网 GeoDataFrame，含 hx 列。
        min_km: 最小合理站间距（千米），默认 0.2。
        max_km: 最大合理站间距（千米），默认 2.0。
        hx_col: 段长列名。

    Returns:
        字典，包含：
            - too_short: 站间距过短的路段 DataFrame
            - too_long: 站间距过长的路段 DataFrame
            - stats: 全网站间距统计摘要

    Examples:
        >>> result = detect_spacing_anomalies(gdf, min_km=0.2, max_km=2.0)
        >>> print(f"过短: {len(result['too_short'])} 段")
    """
    cols = ['stationname', 'nt_stationname', 'name', hx_col]
    available_cols = [c for c in cols if c in gdf.columns]

    too_short = gdf[gdf[hx_col] < min_km][available_cols].copy()
    too_long = gdf[gdf[hx_col] > max_km][available_cols].copy()

    stats = {
        'mean_km': round(gdf[hx_col].mean(), 4),
        'median_km': round(gdf[hx_col].median(), 4),
        'std_km': round(gdf[hx_col].std(), 4),
        'min_km': round(gdf[hx_col].min(), 4),
        'max_km': round(gdf[hx_col].max(), 4),
        'too_short_count': len(too_short),
        'too_long_count': len(too_long),
        'total_segments': len(gdf),
        'anomaly_ratio': round((len(too_short) + len(too_long)) / len(gdf), 4) if len(gdf) > 0 else 0,
    }

    return {
        'too_short': too_short.reset_index(drop=True),
        'too_long': too_long.reset_index(drop=True),
        'stats': stats,
    }


def evaluate_route_efficiency(
    gdf: gpd.GeoDataFrame,
    G_L: nx.Graph,
) -> pd.DataFrame:
    """综合评估各线路的运营效率。

    为每条线路计算多维指标，包括非直线系数、平均站间距、
    站点数量、线路长度、与其他线路的重复程度。

    Args:
        gdf: 结构化公交线网 GeoDataFrame。
        G_L: Space-L 网络图。

    Returns:
        各线路的效率评估 DataFrame，包含：
            - name: 线路名
            - total_length_km: 线路总长
            - station_count: 站点数
            - avg_spacing_km: 平均站间距
            - max_spacing_km: 最大站间距
            - nonline_coeff: 非直线系数（若可计算）
            - shared_ratio: 与其他线路共用路段的比例
            - efficiency_score: 综合效率评分（0~100）
    """
    results = []

    for route_name in gdf['name'].unique():
        route = gdf[gdf['name'] == route_name]
        total_length = route['hx'].sum()
        station_count = len(route) + 1
        avg_spacing = route['hx'].mean()
        max_spacing = route['hx'].max()

        shared_edges = 0
        total_edges = 0
        for _, row in route.iterrows():
            if G_L.has_edge(row['id'], row['next_id']):
                edge_data = G_L[row['id']][row['next_id']]
                lines_on_edge = edge_data.get('bus_lines', [])
                total_edges += 1
                if len(set(ln.split('(')[0] for ln in lines_on_edge)) > 1:
                    shared_edges += 1

        shared_ratio = shared_edges / total_edges if total_edges > 0 else 0

        spacing_score = max(0, 100 - abs(avg_spacing - 0.8) * 100)
        shared_penalty = shared_ratio * 30
        length_score = min(total_length / 15 * 50, 50)

        efficiency = max(0, min(100, spacing_score - shared_penalty + length_score))

        results.append({
            'name': route_name,
            'total_length_km': round(total_length, 2),
            'station_count': station_count,
            'avg_spacing_km': round(avg_spacing, 3),
            'max_spacing_km': round(max_spacing, 3),
            'shared_ratio': round(shared_ratio, 3),
            'efficiency_score': round(efficiency, 1),
        })

    df = pd.DataFrame(results)
    if not df.empty:
        df = df.sort_values('efficiency_score', ascending=False).reset_index(drop=True)
    return df


def suggest_new_stops(
    gdf: gpd.GeoDataFrame,
    max_spacing_km: float = 2.0,
) -> gpd.GeoDataFrame:
    """建议在站间距过长的路段增设站点。

    对于超过阈值的路段，在中点位置建议新增站点。

    Args:
        gdf: 结构化线网 GeoDataFrame。
        max_spacing_km: 触发建议的最大站间距（千米），默认 2.0。

    Returns:
        GeoDataFrame，建议新增站点的位置和原因。
    """
    suggestions = []
    for _, row in gdf.iterrows():
        if row['hx'] > max_spacing_km:
            geom = row['geometry']
            midpoint = geom.interpolate(0.5, normalized=True)
            suggestions.append({
                'suggested_lng': midpoint.x,
                'suggested_lat': midpoint.y,
                'between_stations': f"{row.get('stationname', '')} → {row.get('nt_stationname', '')}",
                'route_name': row.get('name', ''),
                'current_spacing_km': round(row['hx'], 3),
                'geometry': midpoint,
            })

    if not suggestions:
        return gpd.GeoDataFrame(columns=['geometry', 'between_stations', 'route_name'])

    return gpd.GeoDataFrame(suggestions, crs=gdf.crs)
