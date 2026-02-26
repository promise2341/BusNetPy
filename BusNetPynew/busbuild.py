"""公交数据构建模块。

将采集的原始公交 CSV 数据（线路折线、站点信息）处理为站点间衔接的
结构化 GeoDataFrame，用于后续网络建模和指标分析。

典型用法::

    from BusNetPynew.busbuild import read_busdata, build_route, show_bus

    df_line, df_point = read_busdata('线路.csv', '站点.csv')
    gdf = build_route(df_line, df_point, epsg=3857, wgs84=True)
    show_bus(gdf)
"""

import warnings
from typing import Tuple, Optional

import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString, Point
import contextily as ctx
import matplotlib.pyplot as plt

from . import find_cycle
from .utils import (
    get_last_coord,
    get_first_coord,
    euclidean_distance_km,
    haversine_distance,
)

warnings.filterwarnings('ignore')


def wgs_dis(row: pd.Series) -> float:
    """计算 DataFrame 行中两个 WGS-84 坐标点之间的 Haversine 距离。

    要求行中包含 lng, lat（起点）和 lng_y, lat_y（终点）四个字段。

    Args:
        row: 包含 lng, lat, lng_y, lat_y 字段的 Series。

    Returns:
        两点之间的距离，单位：千米。
    """
    return haversine_distance(row['lat'], row['lng'], row['lat_y'], row['lng_y'])


def read_busdata(
    path_line: str,
    path_point: str,
    encod_line: str = 'utf-8',
    encod_point: str = 'utf-8',
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """读取公交线路折线和站点 CSV 数据。

    Args:
        path_line: 线路折线 CSV 文件路径。
        path_point: 站点信息 CSV 文件路径。
        encod_line: 线路文件编码，默认 utf-8。
        encod_point: 站点文件编码，默认 utf-8。

    Returns:
        (df_line, df_point) 元组，分别为线路数据和站点数据。
    """
    df_line = pd.read_csv(path_line, encoding=encod_line)
    df_point = pd.read_csv(path_point, encoding=encod_point)
    df_point['line_index'] = None
    return df_line, df_point


def build_index(
    df_line: pd.DataFrame,
    df_point: pd.DataFrame,
) -> pd.DataFrame:
    """提取公交站点在线路折线中的索引位置。

    通过经纬度匹配，为每个站点标注其在对应线路折线数据中的行索引，
    用于后续截取站点间的线路几何形状。

    同时使用环线检测去除环线路的重复站点段。

    Args:
        df_line: 线路折线 DataFrame（含 lng, lat, 全称 列）。
        df_point: 站点信息 DataFrame（含 lng, lat, name, 站点名称 列）。

    Returns:
        添加了 line_index 列的 df_point DataFrame。
    """
    for line_name in df_line['全称'].unique():
        testline = df_line[df_line['全称'] == line_name]
        testpoint = df_point[df_point['name'] == line_name]

        if len(testpoint['正反线路'].unique()) > 1:
            testpoint = testpoint[testpoint['正反线路'] == testpoint['正反线路'].unique()[0]]

        last_index = 0

        for i, point_row in testpoint.iterrows():
            matched_line = testline[last_index:][
                (testline['lng'] == point_row['lng']) & (testline['lat'] == point_row['lat'])
            ]

            if not matched_line.empty:
                line_index = matched_line.index[0]
                last_index = last_index + 1
                df_point.at[i, 'line_index'] = line_index
            else:
                matched_line = testline[0:][
                    (testline['lng'] == point_row['lng']) & (testline['lat'] == point_row['lat'])
                ]
                line_index = matched_line.index[0]
                last_index = 0
                df_point.at[i, 'line_index'] = line_index

    df_point = df_point.dropna(subset=['line_index'])

    for line_name in df_point['name'].unique():
        test_line = df_point[df_point['name'] == line_name]
        station_name = test_line['站点名称'].tolist()
        cycle = find_cycle.find_cycle(station_name)

        if (len(test_line) - len(cycle)) > (len(cycle) / 2):
            df_point = df_point[~df_point['name'].isin([line_name])]
            df_cycle = test_line.iloc[:len(cycle)]
            df_point = pd.concat([df_point, df_cycle], axis=0)

    return df_point


def line_build(
    df_point: pd.DataFrame,
    df_line: pd.DataFrame,
    epsg: int = 3857,
) -> gpd.GeoDataFrame:
    """构造前后站点衔接的公交线网 GeoDataFrame。

    为每个站点生成到下一站的错位关联，构建站点间的 LineString 几何，
    并计算线路实际长度（hx 字段，单位千米）。

    Args:
        df_point: 含 line_index 列的站点 DataFrame。
        df_line: 线路折线 DataFrame。
        epsg: 投影坐标系 EPSG 代码，默认 3857。

    Returns:
        结构化的公交线网 GeoDataFrame，含 hx（段长）、geometry 等列。
    """
    for name in df_point['name'].unique():
        mask = df_point['name'] == name
        df_point.loc[mask, 'next_站点名称'] = df_point[mask]['站点名称'].shift(-1, axis=0)
        df_point.loc[mask, 'next_lng'] = df_point[mask]['lng'].shift(-1, axis=0)
        df_point.loc[mask, 'next_lat'] = df_point[mask]['lat'].shift(-1, axis=0)
        df_point.loc[mask, 'next_id'] = df_point[mask]['id'].shift(-1, axis=0)
        df_point.loc[mask, 'next_line_index'] = df_point[mask]['line_index'].shift(-1, axis=0)

    df_point = df_point.dropna()
    df_point['geometry'] = None

    for index, row in df_point.iterrows():
        line_index = row['line_index']
        next_line_index = row['next_line_index']

        if line_index < next_line_index:
            points = df_line.iloc[int(line_index):int(next_line_index) + 1][['lng', 'lat']]
        else:
            points = df_line.iloc[int(next_line_index):int(line_index) + 1][['lng', 'lat']]

        line = LineString(points.values.tolist())
        df_point.at[index, 'geometry'] = line

    gdf = gpd.GeoDataFrame(df_point, geometry='geometry', crs="EPSG:4326")
    gdf = gdf.to_crs(epsg=epsg)

    gdf['hx'] = gdf.length / 1000
    gdf.drop(columns='城市', inplace=True)
    gdf = gdf.rename(columns={
        '站点名称': 'stationname',
        '正反线路': 'dir',
        'next_站点名称': 'nt_stationname',
    })

    return gdf


def ycl_gdf(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """从 GeoDataFrame 中提取起止点坐标并计算直线距离。

    为 GeoDataFrame 添加起点 (lng, lat)、终点 (lng_y, lat_y) 坐标列，
    以及直线距离 (zx_dis) 列。

    Args:
        gdf: 含 LineString 几何列的 GeoDataFrame。

    Returns:
        添加了坐标和距离列的 GeoDataFrame。
    """
    gdf['lng_y'], gdf['lat_y'] = zip(*gdf['geometry'].apply(get_last_coord))
    gdf['lng'], gdf['lat'] = zip(*gdf['geometry'].apply(get_first_coord))

    if gdf.crs.to_epsg() != 4326:
        gdf['zx_dis'] = gdf.apply(
            lambda row: euclidean_distance_km(row['lng'], row['lat'], row['lng_y'], row['lat_y']),
            axis=1,
        )
    else:
        gdf['zx_dis'] = gdf.apply(wgs_dis, axis=1)
    return gdf


def build_route(
    line: pd.DataFrame,
    point: pd.DataFrame,
    epsg: int = 3857,
    wgs84: bool = True,
) -> gpd.GeoDataFrame:
    """整合构建完整的公交线网结构化数据。

    依次执行站点索引匹配、线网构建、坐标提取与距离计算，
    输出可直接用于网络建模和指标分析的 GeoDataFrame。

    Args:
        line: 线路折线 DataFrame。
        point: 站点信息 DataFrame。
        epsg: 投影坐标系 EPSG 代码，默认 3857。
        wgs84: 是否将结果转换回 WGS-84 坐标系，默认 True。

    Returns:
        结构化的公交线网 GeoDataFrame。

    Examples:
        >>> df_line, df_point = read_busdata('line.csv', 'point.csv')
        >>> gdf = build_route(df_line, df_point, epsg=3857)
    """
    df_point = build_index(line, point)
    gdf = line_build(df_point, line, epsg=epsg)
    gdf = ycl_gdf(gdf)
    if wgs84:
        gdf = gdf.to_crs(epsg=4326)
        gdf = ycl_gdf(gdf)
    return gdf


def show_bus(gdf: gpd.GeoDataFrame) -> None:
    """使用 matplotlib 和 contextily 可视化公交线网。

    以线段长度（hx）为颜色映射，叠加 OpenStreetMap 底图。

    Args:
        gdf: 公交线网 GeoDataFrame（需含 hx 列和 geometry 列）。
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, column='hx', legend=True)
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    plt.show()


def save_shp(gdf: gpd.GeoDataFrame, save_path: Optional[str] = None) -> None:
    """将 GeoDataFrame 保存为 Shapefile 文件。

    自动将所有非几何列转为字符串类型以确保兼容性。

    Args:
        gdf: 待保存的 GeoDataFrame。
        save_path: Shapefile 保存路径。
    """
    gdf = gdf[~gdf.geometry.is_empty]
    for col in gdf.columns:
        if col != 'geometry':
            gdf[col] = gdf[col].astype(str)
    gdf.to_file(driver='ESRI Shapefile', filename=save_path, encoding='utf-8')


def save_point(
    point: pd.DataFrame,
    save_path: Optional[str] = None,
    epsg: int = 4326,
) -> None:
    """将站点数据保存为 Shapefile 文件。

    自动从 lng/lat 列创建 Point 几何，并进行投影转换。

    Args:
        point: 站点 DataFrame（含 lng, lat, 站点名称, 正反线路 等列）。
        save_path: Shapefile 保存路径。
        epsg: 输出坐标系 EPSG 代码，默认 4326。
    """
    geometry = [Point(xy) for xy in zip(point['lng'], point['lat'])]
    point_gdf = gpd.GeoDataFrame(point, geometry=geometry, crs="EPSG:4326")
    point_gdf = point_gdf.to_crs(epsg=epsg)
    point_gdf = point_gdf.rename(columns={
        '站点名称': 'stationname',
        '正反线路': 'dir',
        '城市': 'city',
    })

    point_gdf['line_index'] = point_gdf['line_index'].astype(str)
    point_gdf['dir'] = point_gdf['dir'].astype(int)
    point_gdf['lng'] = point_gdf['lng'].astype(float)
    point_gdf['lat'] = point_gdf['lat'].astype(float)
    point_gdf['city'] = point_gdf['city'].astype(str)
    point_gdf['stationname'] = point_gdf['stationname'].astype(str)
    point_gdf['id'] = point_gdf['id'].astype(str)
    point_gdf['name'] = point_gdf['name'].astype(str)

    point_gdf.to_file(driver='ESRI Shapefile', filename=save_path, encoding='utf-8')
