"""POI 数据联动分析模块。

将公交网络与城市兴趣点（POI）数据结合，实现：
    - 站点周边 POI 画像
    - 公共设施公交可达性分析
    - 职住通勤公交服务能力评估

支持通过高德地图 API 在线获取 POI 数据，
也支持直接传入本地 POI GeoDataFrame。

典型用法::

    from BusNetPynew.poi_bindling import (
        station_poi_profile, facility_accessibility,
        commute_analysis, fetch_pois
    )

    # 在线获取 POI 并分析
    pois = fetch_pois(api_key='KEY', city='长沙', keywords='医院')
    access = facility_accessibility(G_L, gdf_stops, pois)
"""

from typing import Any, Dict, List, Optional, Tuple

import geopandas as gpd
import networkx as nx
import numpy as np
import pandas as pd
import requests
from shapely.geometry import Point

from .utils import haversine_distance


def fetch_pois(
    api_key: str,
    city: str,
    keywords: str = '医院',
    types: str = '',
    radius_m: int = 50000,
    center: Optional[Tuple[float, float]] = None,
    max_pages: int = 20,
) -> gpd.GeoDataFrame:
    """通过高德地图 API 获取城市 POI 数据。

    Args:
        api_key: 高德 v5 API Key。
        city: 城市名称。
        keywords: 搜索关键字，如 '医院'、'学校'、'商场'。
        types: POI 类型代码（可选，如 '090100' 为医院）。
        radius_m: 搜索半径（米），默认 50000。
        center: 搜索中心点 (lng, lat)，为 None 则搜索全城。
        max_pages: 最大分页数，默认 20。

    Returns:
        POI GeoDataFrame，包含 name, type, address, lng, lat, geometry 列。

    Examples:
        >>> hospitals = fetch_pois('API_KEY', '长沙', '医院')
        >>> print(f"找到 {len(hospitals)} 家医院")
    """
    base_url = 'https://restapi.amap.com/v5/place/text'
    all_pois = []

    for page in range(1, max_pages + 1):
        params = {
            'key': api_key,
            'keywords': keywords,
            'region': city,
            'page_size': 25,
            'page_num': page,
            'show_fields': 'business',
        }
        if types:
            params['types'] = types
        if center:
            params['location'] = f"{center[0]},{center[1]}"

        try:
            resp = requests.get(base_url, params=params, timeout=10)
            data = resp.json()
        except Exception:
            break

        if data.get('status') != '1' or data.get('count', '0') == '0':
            break

        pois = data.get('pois', [])
        if not pois:
            break

        for poi in pois:
            location = poi.get('location', '')
            if ',' not in location:
                continue
            lng, lat = location.split(',')
            all_pois.append({
                'name': poi.get('name', ''),
                'type': poi.get('type', ''),
                'address': poi.get('address', ''),
                'lng': float(lng),
                'lat': float(lat),
            })

    if not all_pois:
        return gpd.GeoDataFrame(columns=['name', 'type', 'address', 'lng', 'lat', 'geometry'])

    df = pd.DataFrame(all_pois)
    geometry = [Point(row['lng'], row['lat']) for _, row in df.iterrows()]
    return gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')


def station_poi_profile(
    gdf_stops: gpd.GeoDataFrame,
    gdf_pois: gpd.GeoDataFrame,
    radius_m: float = 500.0,
    station_name_col: str = 'stationname',
) -> pd.DataFrame:
    """统计每个公交站点周边的 POI 分布画像。

    Args:
        gdf_stops: 站点 GeoDataFrame（Point 几何）。
        gdf_pois: POI GeoDataFrame（Point 几何），需含 type 列。
        radius_m: 统计半径（米），默认 500。
        station_name_col: 站名列名。

    Returns:
        DataFrame，每行为一个站点，列为各 POI 类型的数量统计，
        额外包含 total_pois 列。

    Examples:
        >>> profile = station_poi_profile(stops, hospitals, radius_m=1000)
        >>> busiest = profile.sort_values('total_pois', ascending=False).head()
    """
    stops_proj = gdf_stops.to_crs(epsg=3857)
    pois_proj = gdf_pois.to_crs(epsg=3857)

    results = []
    for idx, stop in stops_proj.iterrows():
        buffer = stop.geometry.buffer(radius_m)
        nearby = pois_proj[pois_proj.geometry.within(buffer)]

        row = {
            station_name_col: gdf_stops.loc[idx].get(station_name_col, ''),
            'lng': gdf_stops.loc[idx].get('lng', stop.geometry.x),
            'lat': gdf_stops.loc[idx].get('lat', stop.geometry.y),
            'total_pois': len(nearby),
        }

        if 'type' in nearby.columns and not nearby.empty:
            type_counts = nearby['type'].value_counts().to_dict()
            row.update(type_counts)

        results.append(row)

    df = pd.DataFrame(results).fillna(0)
    return df.sort_values('total_pois', ascending=False).reset_index(drop=True)


def facility_accessibility(
    G_L: nx.Graph,
    gdf_stops: gpd.GeoDataFrame,
    gdf_facilities: gpd.GeoDataFrame,
    speed_kmh: float = 20.0,
    walk_speed_kmh: float = 5.0,
    max_walk_km: float = 0.5,
) -> pd.DataFrame:
    """分析公共设施的公交可达性。

    计算每个站点到最近设施的公交出行时间（包含步行接驳）。

    Args:
        G_L: Space-L 网络图。
        gdf_stops: 站点 GeoDataFrame。
        gdf_facilities: 设施 GeoDataFrame（如医院、学校）。
        speed_kmh: 公交平均速度（千米/小时）。
        walk_speed_kmh: 步行速度（千米/小时）。
        max_walk_km: 最大步行接驳距离（千米）。

    Returns:
        DataFrame，每行为一个站点，包含：
            - staname: 站点名
            - nearest_facility: 最近设施名
            - walk_distance_km: 从最近站点到设施的步行距离
            - total_time_min: 总出行时间（分钟）
            - has_access: 是否在可达范围内
    """
    facility_nearest_nodes = {}
    for f_idx, facility in gdf_facilities.iterrows():
        f_lng = facility.get('lng', facility.geometry.x)
        f_lat = facility.get('lat', facility.geometry.y)

        min_dist = float('inf')
        nearest_node = None
        for node, data in G_L.nodes(data=True):
            pos = data.get('pos', (0, 0))
            dist = haversine_distance(f_lat, f_lng, pos[1], pos[0])
            if dist < min_dist:
                min_dist = dist
                nearest_node = node

        if nearest_node and min_dist <= max_walk_km:
            facility_nearest_nodes[f_idx] = {
                'node': nearest_node,
                'walk_dist': min_dist,
                'name': facility.get('name', ''),
            }

    results = []
    for node, data in G_L.nodes(data=True):
        best_time = float('inf')
        best_facility = ''
        best_walk = 0

        try:
            lengths = nx.single_source_dijkstra_path_length(G_L, node, weight='length')
        except nx.NodeNotFound:
            continue

        for f_idx, f_info in facility_nearest_nodes.items():
            f_node = f_info['node']
            if f_node in lengths:
                bus_time = (lengths[f_node] / speed_kmh) * 60
                walk_time = (f_info['walk_dist'] / walk_speed_kmh) * 60
                total = bus_time + walk_time

                if total < best_time:
                    best_time = total
                    best_facility = f_info['name']
                    best_walk = f_info['walk_dist']

        results.append({
            'node_id': node,
            'staname': data.get('staname', ''),
            'nearest_facility': best_facility,
            'walk_distance_km': round(best_walk, 3),
            'total_time_min': round(best_time, 1) if best_time < float('inf') else None,
            'has_access': best_time < float('inf'),
        })

    df = pd.DataFrame(results)
    return df.sort_values('total_time_min', na_position='last').reset_index(drop=True)


def commute_analysis(
    G_L: nx.Graph,
    residential_nodes: List[Any],
    work_nodes: List[Any],
    speed_kmh: float = 20.0,
) -> Dict[str, Any]:
    """分析职住区域之间的公交通勤服务能力。

    Args:
        G_L: Space-L 网络图。
        residential_nodes: 居住区附近的站点 ID 列表。
        work_nodes: 工作区附近的站点 ID 列表。
        speed_kmh: 公交平均速度（千米/小时）。

    Returns:
        字典，包含：
            - avg_commute_min: 平均通勤时间（分钟）
            - median_commute_min: 中位数通勤时间
            - max_commute_min: 最长通勤时间
            - min_commute_min: 最短通勤时间
            - within_30min: 30 分钟内可达的比例
            - within_60min: 60 分钟内可达的比例
            - detail_matrix: 详细的通勤时间矩阵 DataFrame
    """
    times = []
    matrix_data = {}

    for r_node in residential_nodes:
        try:
            lengths = nx.single_source_dijkstra_path_length(G_L, r_node, weight='length')
        except nx.NodeNotFound:
            continue

        row = {}
        for w_node in work_nodes:
            if w_node in lengths:
                t = (lengths[w_node] / speed_kmh) * 60
                times.append(t)
                row[w_node] = round(t, 1)
            else:
                row[w_node] = None
        matrix_data[r_node] = row

    detail_matrix = pd.DataFrame(matrix_data).T

    if not times:
        return {
            'avg_commute_min': None,
            'median_commute_min': None,
            'max_commute_min': None,
            'min_commute_min': None,
            'within_30min': 0,
            'within_60min': 0,
            'detail_matrix': detail_matrix,
        }

    times_arr = np.array(times)
    return {
        'avg_commute_min': round(float(np.mean(times_arr)), 1),
        'median_commute_min': round(float(np.median(times_arr)), 1),
        'max_commute_min': round(float(np.max(times_arr)), 1),
        'min_commute_min': round(float(np.min(times_arr)), 1),
        'within_30min': round(float(np.mean(times_arr <= 30)), 3),
        'within_60min': round(float(np.mean(times_arr <= 60)), 3),
        'detail_matrix': detail_matrix,
    }


def nearby_stations(
    gdf_stops: gpd.GeoDataFrame,
    lng: float,
    lat: float,
    radius_m: float = 1000.0,
    name_col: str = 'stationname',
) -> gpd.GeoDataFrame:
    """查找指定坐标附近的公交站点。

    Args:
        gdf_stops: 站点 GeoDataFrame。
        lng: 查询点经度。
        lat: 查询点纬度。
        radius_m: 搜索半径（米），默认 1000。
        name_col: 站名列名。

    Returns:
        在搜索半径内的站点 GeoDataFrame，按距离升序排列。
    """
    stops_proj = gdf_stops.to_crs(epsg=3857)
    query_point = gpd.GeoSeries(
        [Point(lng, lat)], crs='EPSG:4326'
    ).to_crs(epsg=3857).iloc[0]

    stops_proj['_dist'] = stops_proj.geometry.distance(query_point)
    nearby = stops_proj[stops_proj['_dist'] <= radius_m].copy()
    nearby['distance_m'] = nearby['_dist'].round(1)
    nearby = nearby.drop(columns='_dist')
    nearby = nearby.sort_values('distance_m').to_crs(epsg=4326)
    return nearby.reset_index(drop=True)
