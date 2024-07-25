import networkx as nx
from math import radians, sin, cos, sqrt, atan2
from pyproj import Transformer, CRS
import pyproj
import math



# 确定半球和带号
def get_utm_zone_and_hemisphere(longitude, latitude):
    # 确定带号
    zone_number = int((longitude + 180) / 6) + 1
    
    # 确定半球
    hemisphere = 'N' if latitude >= 0 else 'S'
    
    return zone_number, hemisphere



# 获取带号
def get_utm_epsg(longitude, latitude):
    zone_number, hemisphere = get_utm_zone_and_hemisphere(longitude, latitude)
    
    # 确定EPSG代码
    if hemisphere == 'N':
        epsg_code = f"326{zone_number:02d}"  # 北半球
    else:
        epsg_code = f"327{zone_number:02d}"  # 南半球
    print(f'带号为:{zone_number}')
    return epsg_code




def latlon_to_utm(longitude, latitude):

    """
    经纬度转utm

    参数:
    x1, y1: 第一个点的UTM坐标
    x2, y2: 第二个点的UTM坐标

    返回:
    两个点之间的距离（米）
    """

    epsg_code = get_utm_epsg(longitude, latitude)
    transformer = pyproj.Transformer.from_crs("epsg:4326", f"epsg:{epsg_code}")
    utm_y, utm_x = transformer.transform(latitude, longitude)
    return epsg_code, utm_x, utm_y

# utm转经纬度
def utm_to_latlon(utm_x, utm_y, epsg_code):
    transformer = pyproj.Transformer.from_crs(f"epsg:{epsg_code}", "epsg:4326")
    latitude, longitude = transformer.transform(utm_y, utm_x)
    return latitude, longitude



def utm_distance(x1, y1, x2, y2):
    """
    计算两个UTM坐标点之间的距离

    参数:
    x1, y1: 第一个点的UTM坐标
    x2, y2: 第二个点的UTM坐标

    返回:
    两个点之间的距离（米）
    """
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance



def haversine_distance(lat1, lon1, lat2, lon2):
    """
    计算两个UTM坐标点之间的距离

    参数:
    x1, y1: 第一个点的gps坐标
    x2, y2: 第二个点的gps坐标

    返回:
    两个点之间的距离km
    """

    R = 6371  # 地球半径（单位：公里）

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance



def find_nearest_node(G,longitude, latitude):
    nearest_node = None
    min_distance = float('inf')
    # _, longitude ,latitude = latlon_to_utm(longitude, latitude)
    print(longitude,latitude)
    for node, data in G.nodes(data=True):
        node_lat = data['pos'][1]
        node_lon = data['pos'][0]
        distance = haversine_distance(latitude, longitude, node_lat, node_lon)
        # distance = utm_distance(longitude,latitude, node_lon, node_lat)

        
        if distance < min_distance:
            min_distance = distance
            nearest_node = data['staname']+'站'

    return nearest_node, min_distance

