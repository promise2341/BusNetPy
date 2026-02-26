"""公交数据采集主模块。

通过高德地图 REST API（v3）采集公交线路的站点坐标、线路信息和
折线路径数据，并将原始数据转换为 GeoDataFrame 格式。

需要高德开放平台的 Web 服务 API Key 和安全密钥。
申请地址：https://lbs.amap.com/

典型用法::

    from BusNetPynew.buspider import buspi

    spider = buspi(
        province='湖南省', city='长沙', key='API_KEY',
        key_fwd='API_KEY_V5', jscode='JSCODE', keyword='公交',
        region_xzq=['湖南省', '长沙市']
    )
    bus_stops, bus_lines = spider.businfo(save_path='./data/')
"""

import csv
import json
import os
import random
import re
import time
import warnings
from typing import Optional, Tuple, List

import geopandas as gpd
import pandas as pd
import requests
from fuzzywuzzy import fuzz
from shapely.geometry import Point, LineString
from tqdm import tqdm

from . import WGS1984
from . import buslist

warnings.filterwarnings("ignore")


def _find_best_match(target: str, options: List[str]) -> Tuple[str, int]:
    """在候选列表中查找与目标字符串最相似的项。

    Args:
        target: 目标字符串。
        options: 候选字符串列表。

    Returns:
        (best_match, highest_score) 最佳匹配字符串和相似度分数。
    """
    best_match = None
    highest_score = 0
    for option in options:
        score = fuzz.ratio(target, option)
        if score > highest_score:
            highest_score = score
            best_match = option
    return best_match, highest_score


def _contains_digit(s: str) -> bool:
    """判断字符串中是否包含数字。"""
    return any(char.isdigit() for char in s)


def _remove_after_last_digit(text: str) -> str:
    """删除字符串中最后一个数字之后的所有字符。

    Args:
        text: 输入字符串。

    Returns:
        截断后的字符串。若无数字则返回原字符串。
    """
    digits = [(m.start(), m.group()) for m in re.finditer(r'\d', text)]
    if not digits:
        return text
    max_index = digits[-1][0]
    return text[:max_index + 1]


class buspi:
    """公交数据采集器。

    通过高德地图 API 采集指定城市的公交站点、线路信息和折线路径数据。

    Args:
        province: 省份名称。
        city: 城市名称。
        key: 高德 v3 API Key。
        key_fwd: 高德 v5 API Key。
        jscode: 高德 JavaScript 安全密钥。
        keyword: 搜索关键字，默认 '公交'。
        region_xzq: 行政区划列表 [省, 市]，与 polygon_mult 二选一。
        polygon_mult: 多边形区域坐标字符串，与 region_xzq 二选一。

    Examples:
        >>> spider = buspi(
        ...     province='湖南省', city='长沙',
        ...     key='your_key', key_fwd='your_key_v5',
        ...     jscode='your_jscode', keyword='公交',
        ...     region_xzq=['湖南省', '长沙市']
        ... )
    """

    def __init__(self, **kwargs):
        self.province: str = kwargs.get('province')
        self.city: str = kwargs.get('city')
        self.key: str = kwargs.get('key')
        self.key_fwd: str = kwargs.get('key_fwd')
        self.keyword: str = kwargs.get('keyword', '公交')
        self.jscode: str = kwargs.get('jscode')
        self.region_xzq: Optional[list] = kwargs.get('region_xzq', None)
        self.polygon_mult: Optional[str] = kwargs.get('polygon_mult', None)

    def _process_buslines(
        self,
        buslines: list,
        keywords: str,
        bus_station: str,
        buslines_information: str,
        buslines_polyline: str,
        city: str,
        relistname: list,
    ) -> None:
        """处理 API 返回的公交线路数据并写入 CSV 文件。"""
        if len(buslines) < 2:
            target_buslines = buslines
        elif fuzz.ratio(buslines[0]['name'], buslines[1]['name']) > 49:
            target_buslines = buslines
        else:
            target = keywords
            options = [buslines[0]['name'], buslines[1]['name']]
            best_match, _ = _find_best_match(target, options)
            indices = [i for i, v in enumerate(options) if v == best_match]
            target_buslines = [buslines[indices[0]]]

        count = 0
        for line in target_buslines:
            if line['name'] in relistname:
                continue

            relistname.append(line['name'])
            count += 1

            for stop in line["busstops"]:
                lng1 = stop["location"].split(",")[0]
                lat1 = stop["location"].split(",")[1]
                wgs_coords = WGS1984.main(lng1, lat1)
                cell = [
                    city, stop["name"], wgs_coords[0], wgs_coords[1],
                    stop["id"], line["name"], count
                ]
                with open(bus_station, 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow(cell)

            information = [
                city, count, keywords[0:4], line["name"],
                line["basic_price"], line["total_price"], line["distance"],
                line["start_stop"], line["end_stop"], line["type"],
                line["start_time"], line["end_time"]
            ]
            with open(buslines_information, 'a', newline='', encoding='utf-8') as f:
                csv.writer(f).writerow(information)

            polyline = line["polyline"]
            split_polyline = polyline.split(";")
            buslines_name2 = line["name"]
            for cou, coord_str in enumerate(split_polyline, start=1):
                excessive = coord_str.split(",")
                wgs_coords = WGS1984.main(excessive[0], excessive[1])
                bus_polyline = [
                    city, cou, buslines_name2, keywords[0:4],
                    wgs_coords[0], wgs_coords[1]
                ]
                with open(buslines_polyline, 'a', newline='', encoding='utf-8') as f:
                    csv.writer(f).writerow(bus_polyline)

    def _research(
        self,
        city: str,
        keywords: str,
        key: str,
        jscode: str,
        bus_station: str,
        buslines_information: str,
        buslines_polyline: str,
        relistname: list,
    ) -> None:
        """查询单条公交线路的详细信息。"""
        url = "https://restapi.amap.com/v3/bus/linename?parameters"
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/75.0.3770.80 Safari/537.36"
            )
        }
        params = {
            "s": "rsv3", "extensions": "all", "key": key,
            "jscode": jscode, "output": "json", "city": city,
            "offset": "2", "keywords": keywords, "platform": "JS"
        }

        resp = requests.get(url, headers=headers, params=params)
        data = json.loads(resp.text)

        if data["status"] == "1":
            if data['buslines']:
                self._process_buslines(
                    data['buslines'], keywords, bus_station,
                    buslines_information, buslines_polyline, city, relistname,
                )
            elif not data['buslines'] and _contains_digit(keywords):
                keywords = _remove_after_last_digit(keywords)
                self._process_buslines(
                    data['buslines'], keywords, bus_station,
                    buslines_information, buslines_polyline, city, relistname,
                )

    def businfo(
        self,
        save_path: Optional[str] = None,
    ) -> Tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
        """执行公交数据采集。

        采集指定城市的公交站点和线路数据，保存为 CSV 文件并返回 GeoDataFrame。

        Args:
            save_path: 数据保存根目录路径。

        Returns:
            (bustop_gdf, busline_gdf) 元组：
                - bustop_gdf: 站点 GeoDataFrame（Point 几何）
                - busline_gdf: 线路 GeoDataFrame（LineString 几何）

        Examples:
            >>> stops, lines = spider.businfo(save_path='./data/')
        """
        province = self.province
        city = self.city
        key = self.key
        keyword = self.keyword
        key_fwd = self.key_fwd
        jscode = self.jscode
        region_xzq = self.region_xzq
        polygon_mult = self.polygon_mult

        relistname = []

        path_bus = save_path
        if not os.path.isdir(path_bus):
            os.mkdir(path_bus)
        if not os.path.isdir(path_bus + province):
            os.mkdir(path_bus + province)

        now_path = path_bus + province + "/csv/"
        if not os.path.isdir(now_path):
            os.mkdir(now_path)

        bus_station = now_path + city + "公交站点.csv"
        buslines_information = now_path + city + "公交线路信息.csv"
        buslines_polyline = now_path + city + "公交线路.csv"

        with open(bus_station, 'a', newline='', encoding='utf_8_sig') as f:
            csv.writer(f).writerow(["城市", "站点名称", "lng", "lat", "id", "name", "正反线路"])

        with open(buslines_information, 'a', newline='', encoding='utf_8_sig') as f:
            csv.writer(f).writerow([
                "城市", "正反线路", "简称", "全称", "上车票价", "全程票价",
                "距离", "起点站", "终点站", "线路类型", "首班时间", "末班时间"
            ])

        with open(buslines_polyline, 'a', newline='', encoding='utf_8_sig') as f:
            csv.writer(f).writerow(["城市", "序号", "全称", "简称", "lng", "lat"])

        citybus_name = []
        if polygon_mult:
            citybus_name = buslist.getpoi(
                api_key=key_fwd, polygon=polygon_mult, keywords=keyword
            ).bus_lines

        if region_xzq:
            citybus_name = buslist.getpoi(
                api_key=key_fwd, cityname=region_xzq, keywords=keyword
            ).bus_lines

        for line_name in tqdm(citybus_name, desc=f"正在获取{city}公交线路数据"):
            self._research(
                city, line_name, key, jscode,
                bus_station, buslines_information, buslines_polyline, relistname,
            )
            time.sleep(random.randint(0, 1))

        bustop_csv = pd.read_csv(bus_station)
        df_info_csv = pd.read_csv(buslines_information)
        buslines_csv = pd.read_csv(buslines_polyline)

        bustop_csv['geometry'] = bustop_csv.apply(
            lambda row: Point(row['lng'], row['lat']), axis=1
        )
        bustop_csv = gpd.GeoDataFrame(bustop_csv, geometry='geometry', crs='4326')

        df_info_csv['geometry'] = None

        for line_name in buslines_csv['全称'].unique():
            coords = buslines_csv[buslines_csv['全称'] == line_name].apply(
                lambda row: (row['lng'], row['lat']), axis=1
            ).to_list()
            if len(coords) >= 2:
                line = LineString(coords)
                idx = df_info_csv[df_info_csv['全称'] == line_name].index
                if len(idx) > 0:
                    df_info_csv.loc[idx[0], 'geometry'] = line

        df_info_csv = gpd.GeoDataFrame(df_info_csv, geometry='geometry', crs='4326')
        df_info_csv.dropna(inplace=True)

        return bustop_csv, df_info_csv

    @staticmethod
    def re_col(
        gdf: gpd.GeoDataFrame,
        col: Optional[List[str]] = None,
    ) -> gpd.GeoDataFrame:
        """重命名 GeoDataFrame 的列名。

        Args:
            gdf: 待重命名的 GeoDataFrame。
            col: 新列名列表。

        Returns:
            重命名后的 GeoDataFrame。
        """
        if col:
            gdf.columns = col
        return gdf

    def bus_to_shpfile(
        self,
        gdf: gpd.GeoDataFrame,
        file_path: Optional[str] = None,
    ) -> None:
        """将 GeoDataFrame 保存为 Shapefile 文件。

        Args:
            gdf: 待保存的 GeoDataFrame。
            file_path: 保存路径，默认使用 save_path。
        """
        gdf = gdf[~gdf.geometry.is_empty]
        for col in gdf.columns:
            if col != 'geometry':
                gdf[col] = gdf[col].astype(str)
        gdf.to_file(driver='ESRI Shapefile', filename=file_path, encoding='utf-8')
