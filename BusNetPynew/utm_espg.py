"""UTM 投影带号计算与坐标变换工具模块。

提供经纬度与 UTM 投影坐标之间的互转功能，以及基于 UTM 和
Haversine 公式的距离计算，和在图网络中查找最近节点的功能。

典型用法::

    from BusNetPynew.utm_espg import latlon_to_utm, haversine_distance

    epsg, utm_x, utm_y = latlon_to_utm(116.4, 39.9)
    dist = haversine_distance(39.9, 116.4, 31.2, 121.5)
"""

import math
from typing import Tuple

import networkx as nx
import pyproj

from .utils import get_utm_zone, get_utm_epsg as _get_utm_epsg


def get_utm_zone_and_hemisphere(
    longitude: float, latitude: float
) -> Tuple[int, str]:
    """根据经纬度确定 UTM 带号和半球。

    Args:
        longitude: 经度（十进制度）。
        latitude: 纬度（十进制度）。

    Returns:
        (带号, 半球标识) 元组，半球标识为 'N' 或 'S'。

    Examples:
        >>> get_utm_zone_and_hemisphere(116.4, 39.9)
        (50, 'N')
    """
    return get_utm_zone(longitude, latitude)


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
    return _get_utm_epsg(longitude, latitude)


def latlon_to_utm(
    longitude: float, latitude: float
) -> Tuple[str, float, float]:
    """将经纬度坐标转换为 UTM 投影坐标。

    Args:
        longitude: 经度（十进制度）。
        latitude: 纬度（十进制度）。

    Returns:
        (epsg_code, utm_x, utm_y) 元组。

    Examples:
        >>> epsg, x, y = latlon_to_utm(116.4, 39.9)
        >>> epsg
        '32650'
    """
    epsg_code = get_utm_epsg(longitude, latitude)
    transformer = pyproj.Transformer.from_crs("epsg:4326", f"epsg:{epsg_code}")
    utm_y, utm_x = transformer.transform(latitude, longitude)
    return epsg_code, utm_x, utm_y


def utm_to_latlon(
    utm_x: float, utm_y: float, epsg_code: str
) -> Tuple[float, float]:
    """将 UTM 投影坐标转换为经纬度坐标。

    Args:
        utm_x: UTM x 坐标（东向）。
        utm_y: UTM y 坐标（北向）。
        epsg_code: UTM 投影的 EPSG 代码。

    Returns:
        (latitude, longitude) 元组。
    """
    transformer = pyproj.Transformer.from_crs(f"epsg:{epsg_code}", "epsg:4326")
    latitude, longitude = transformer.transform(utm_y, utm_x)
    return latitude, longitude


def utm_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """计算两个 UTM 坐标点之间的欧氏距离。

    Args:
        x1: 第一个点的 x 坐标（米）。
        y1: 第一个点的 y 坐标（米）。
        x2: 第二个点的 x 坐标（米）。
        y2: 第二个点的 y 坐标（米）。

    Returns:
        两点之间的距离，单位：米。

    Examples:
        >>> utm_distance(0, 0, 3000, 4000)
        5000.0
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


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
    R = 6371
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def find_nearest_node(
    G: nx.Graph, longitude: float, latitude: float
) -> Tuple[str, float]:
    """在图网络中查找距给定经纬度最近的节点。

    遍历图中所有节点，使用 Haversine 公式计算距离，
    返回最近节点的站名和距离。

    Args:
        G: 含有 pos=(lng, lat) 和 staname 节点属性的 NetworkX 图。
        longitude: 查询点经度。
        latitude: 查询点纬度。

    Returns:
        (nearest_staname, min_distance_km) 元组。

    Examples:
        >>> import networkx as nx
        >>> G = nx.Graph()
        >>> G.add_node("s1", pos=(116.4, 39.9), staname="天安门")
        >>> name, dist = find_nearest_node(G, 116.41, 39.91)
        >>> name
        '天安门站'
    """
    min_distance = float('inf')
    nearest_sta = None

    for node, data in G.nodes(data=True):
        node_lat = data['pos'][1]
        node_lon = data['pos'][0]
        distance = haversine_distance(latitude, longitude, node_lat, node_lon)

        if distance < min_distance:
            min_distance = distance
            nearest_sta = data['staname'] + '站'

    return nearest_sta, min_distance
