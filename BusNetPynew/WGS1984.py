"""GCJ-02 与 WGS-84 坐标系互转模块。

中国使用 GCJ-02 坐标系（国测局坐标），高德地图等国内地图服务返回此坐标。
WGS-84 为国际通用 GPS 坐标系。本模块提供两者之间的相互转换。

典型用法::

    from BusNetPynew.WGS1984 import gcj02towgs84, wgs84togcj02

    # GCJ-02 转 WGS-84
    wgs_lng, wgs_lat = gcj02towgs84(116.397428, 39.90923)

    # WGS-84 转 GCJ-02
    gcj_lng, gcj_lat = wgs84togcj02(116.391184, 39.907826)
"""

import math
from typing import List

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率


def wgs84togcj02(lng: float, lat: float) -> List[float]:
    """将 WGS-84 坐标转换为 GCJ-02 坐标。

    Args:
        lng: WGS-84 经度。
        lat: WGS-84 纬度。

    Returns:
        [gcj_lng, gcj_lat] GCJ-02 坐标列表。

    Examples:
        >>> result = wgs84togcj02(116.391184, 39.907826)
        >>> round(result[0], 4)
        116.3974
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def gcj02towgs84(lng: float, lat: float) -> List[float]:
    """将 GCJ-02 坐标转换为 WGS-84 坐标。

    Args:
        lng: GCJ-02 经度。
        lat: GCJ-02 纬度。

    Returns:
        [wgs_lng, wgs_lat] WGS-84 坐标列表。

    Examples:
        >>> result = gcj02towgs84(116.397428, 39.90923)
        >>> round(result[0], 4)
        116.3912
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


def _transformlat(lng: float, lat: float) -> float:
    """纬度转换辅助函数。"""
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
        0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng: float, lat: float) -> float:
    """经度转换辅助函数。"""
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
        0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng: float, lat: float) -> bool:
    """判断坐标是否在中国境外。

    Args:
        lng: 经度。
        lat: 纬度。

    Returns:
        True 表示在中国境外，不需要坐标偏移。
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False


def main(lng: float, lat: float) -> List[float]:
    """将 GCJ-02 坐标转换为 WGS-84 坐标（便捷接口）。

    Args:
        lng: GCJ-02 经度（可为字符串，会自动转为 float）。
        lat: GCJ-02 纬度（可为字符串，会自动转为 float）。

    Returns:
        [wgs_lng, wgs_lat] WGS-84 坐标列表。

    Examples:
        >>> result = main(112.917724, 28.230401)
        >>> len(result)
        2
    """
    lng = float(lng)
    lat = float(lat)
    return gcj02towgs84(lng, lat)


if __name__ == '__main__':
    main(112.917724, 28.230401)
