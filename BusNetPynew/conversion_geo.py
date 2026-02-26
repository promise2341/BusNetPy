"""地理边界校验与 Shapefile 导出模块。

通过 DataV 阿里云 API 获取城市行政边界，对公交站点进行地理空间校验，
并将站点和线路数据导出为 Shapefile 格式。

典型用法::

    from BusNetPynew.conversion_geo import main

    main('站点.csv', '线路信息.csv', '线路折线.csv', '长沙', '湖南省')
"""

import os

import geopandas as gpd
import pandas as pd
import requests
from pypinyin import lazy_pinyin
from shapely.geometry import LineString

from .ChineseAdminiDivisionsDict import CitiesCode


def boundary_judgment(
    city: str,
    gdf: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    """使用城市行政边界对公交站点进行地理空间校验。

    从 DataV 阿里云 API 获取城市边界 GeoJSON，通过空间连接筛选
    位于边界内的站点。若获取失败则返回原始数据。

    Args:
        city: 城市中文名称。
        gdf: 公交站点 GeoDataFrame。

    Returns:
        经过边界校验的站点 GeoDataFrame。
    """
    try:
        city_code = CitiesCode.get(str(city))
        if city_code is None:
            return gdf

        url = f"https://geo.datav.aliyun.com/areas/bound/geojson?code={city_code}"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/75.0.3770.80 Safari/537.36"
            )
        }
        resp = requests.get(url, headers=headers)
        datas = gpd.read_file(resp.text, ensure_ascii=False)
        boundary = datas.drop(list(datas.columns[[0, 2, 3, 4, 5]]), axis=1)
        points_with_boundary = gpd.sjoin(gdf, boundary, how="inner", predicate='intersects')

        if not points_with_boundary.empty:
            return points_with_boundary
        return gdf
    except Exception:
        return gdf


def _city_to_pinyin(city: str) -> str:
    """将城市中文名转换为拼音字符串。"""
    return ''.join(lazy_pinyin(city))


def _point_to_line(df: pd.DataFrame) -> LineString:
    """将排序后的坐标点构造为 LineString。"""
    return LineString(df.sort_values("序号")[["lng", "lat"]].values)


def Create_busline(
    path2: str,
    path3: str,
    city: str,
    now_path: str,
) -> None:
    """从线路折线数据创建线路 Shapefile。

    Args:
        path2: 线路信息 CSV 文件路径。
        path3: 线路折线 CSV 文件路径。
        city: 城市中文名称。
        now_path: 输出目录路径。
    """
    line_dir = os.path.join(now_path, "line")
    if not os.path.isdir(line_dir):
        os.mkdir(line_dir)

    df = pd.read_csv(path3)
    busline = (
        df.groupby("全称")
        .apply(_point_to_line)
        .to_frame(name="geometry")
        .pipe(gpd.GeoDataFrame, crs="EPSG:4326")
    )
    buslines_polyline = pd.read_csv(path2)
    busline = busline.merge(buslines_polyline, on='全称')
    busline = busline.drop_duplicates('全称')

    city_pinyin = _city_to_pinyin(city)
    linepath = os.path.join(line_dir, f"{city_pinyin}_busline.shp")
    busline.to_file(linepath, encoding='gb18030')


def point(city: str, path1: str, now_path: str) -> None:
    """从站点数据创建站点 Shapefile。

    Args:
        city: 城市中文名称。
        path1: 站点 CSV 文件路径。
        now_path: 输出目录路径。
    """
    point_dir = os.path.join(now_path, "point")
    if not os.path.isdir(point_dir):
        os.mkdir(point_dir)

    bus_station = pd.read_csv(path1)
    bus_station = bus_station.drop_duplicates('id')
    gdf_bus_station = gpd.GeoDataFrame(
        bus_station,
        geometry=gpd.points_from_xy(bus_station.lng, bus_station.lat),
    )
    gdf_bus_station.crs = 'EPSG:4326'

    point_shp = boundary_judgment(city, gdf_bus_station)
    city_pinyin = _city_to_pinyin(city)
    pointpath = os.path.join(point_dir, f"{city_pinyin}_buspoint.shp")
    point_shp.to_file(pointpath, encoding='gb18030')


def main(
    path1: str,
    path2: str,
    path3: str,
    city: str,
    province: str,
) -> None:
    """执行完整的地理校验与 Shapefile 导出流程。

    Args:
        path1: 站点 CSV 文件路径。
        path2: 线路信息 CSV 文件路径。
        path3: 线路折线 CSV 文件路径。
        city: 城市中文名称。
        province: 省份名称。
    """
    now_path = os.path.join(os.getcwd(), "data", province, "shp")
    if not os.path.isdir(now_path):
        os.makedirs(now_path, exist_ok=True)

    point(city, path1, now_path)
    Create_busline(path2, path3, city, now_path)
