"""公共工具函数模块。

提供坐标提取、距离计算等在多个模块中复用的基础功能函数。
"""

import math
from typing import Optional, Tuple

import geopandas as gpd
from shapely.geometry import LineString


def get_last_coord(geometry: LineString) -> Optional[Tuple[float, float]]:
    """从 LineString 几何对象中提取最后一个坐标点。

    Args:
        geometry: Shapely LineString 几何对象。

    Returns:
        最后一个坐标点的 (x, y) 元组，若非 LineString 则返回 None。

    Examples:
        >>> from shapely.geometry import LineString
        >>> line = LineString([(0, 0), (1, 1), (2, 2)])
        >>> get_last_coord(line)
        (2.0, 2.0)
    """
    if isinstance(geometry, LineString):
        return list(geometry.coords)[-1]
    return None


def get_first_coord(geometry: LineString) -> Optional[Tuple[float, float]]:
    """从 LineString 几何对象中提取第一个坐标点。

    Args:
        geometry: Shapely LineString 几何对象。

    Returns:
        第一个坐标点的 (x, y) 元组，若非 LineString 则返回 None。

    Examples:
        >>> from shapely.geometry import LineString
        >>> line = LineString([(0, 0), (1, 1), (2, 2)])
        >>> get_first_coord(line)
        (0.0, 0.0)
    """
    if isinstance(geometry, LineString):
        return list(geometry.coords)[0]
    return None


def euclidean_distance_km(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    """计算两个投影坐标点之间的欧氏距离（千米）。

    适用于已投影到平面坐标系（如 EPSG:3857、UTM 等）的坐标。

    Args:
        x1: 第一个点的 x 坐标（米）。
        y1: 第一个点的 y 坐标（米）。
        x2: 第二个点的 x 坐标（米）。
        y2: 第二个点的 y 坐标（米）。

    Returns:
        两点之间的距离，单位：千米。

    Examples:
        >>> euclidean_distance_km(0, 0, 3000, 4000)
        5.0
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / 1000


def haversine_distance(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    """使用 Haversine 公式计算两个 WGS-84 坐标点的大圆距离。

    Args:
        lat1: 第一个点的纬度（十进制度）。
        lon1: 第一个点的经度（十进制度）。
        lat2: 第二个点的纬度（十进制度）。
        lon2: 第二个点的经度（十进制度）。

    Returns:
        两点之间的距离，单位：千米。

    Examples:
        >>> round(haversine_distance(39.9, 116.4, 31.2, 121.5), 1)
        1071.3
    """
    R = 6371  # 地球半径（千米）
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def extract_endpoint_coords(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """从 GeoDataFrame 的 LineString 几何列中提取起止点坐标。

    为 GeoDataFrame 添加 lng, lat（起点）和 lng_y, lat_y（终点）四列。
    同时根据坐标系类型计算直线距离 zx_dis 列。

    Args:
        gdf: 含 LineString 几何列的 GeoDataFrame。

    Returns:
        添加了 lng, lat, lng_y, lat_y, zx_dis 列的 GeoDataFrame。
    """
    gdf = gdf.copy()
    gdf['lng_y'], gdf['lat_y'] = zip(*gdf['geometry'].apply(get_last_coord))
    gdf['lng'], gdf['lat'] = zip(*gdf['geometry'].apply(get_first_coord))

    if gdf.crs is not None and gdf.crs.to_epsg() != 4326:
        gdf['zx_dis'] = gdf.apply(
            lambda row: euclidean_distance_km(row['lng'], row['lat'], row['lng_y'], row['lat_y']),
            axis=1,
        )
    else:
        gdf['zx_dis'] = gdf.apply(
            lambda row: haversine_distance(row['lat'], row['lng'], row['lat_y'], row['lng_y']),
            axis=1,
        )
    return gdf


def get_utm_zone(longitude: float, latitude: float) -> Tuple[int, str]:
    """根据经纬度确定 UTM 带号和半球。

    Args:
        longitude: 经度（十进制度）。
        latitude: 纬度（十进制度）。

    Returns:
        (带号, 半球标识) 元组，半球标识为 'N'（北半球）或 'S'（南半球）。

    Examples:
        >>> get_utm_zone(116.4, 39.9)
        (50, 'N')
    """
    zone_number = int((longitude + 180) / 6) + 1
    hemisphere = 'N' if latitude >= 0 else 'S'
    return zone_number, hemisphere


def get_utm_epsg(longitude: float, latitude: float) -> str:
    """根据经纬度获取 UTM 投影的 EPSG 代码。

    Args:
        longitude: 经度（十进制度）。
        latitude: 纬度（十进制度）。

    Returns:
        EPSG 代码字符串，如 "32650"。

    Examples:
        >>> get_utm_epsg(116.4, 39.9)
        '32650'
    """
    zone_number, hemisphere = get_utm_zone(longitude, latitude)
    if hemisphere == 'N':
        return f"326{zone_number:02d}"
    return f"327{zone_number:02d}"
