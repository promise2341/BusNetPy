"""公交线路名称 POI 搜索模块。

通过高德地图 v5 API 的 POI 搜索功能获取指定区域（行政区或多边形）
内的公交线路名称列表。

典型用法::

    from BusNetPynew.buslist import getpoi

    # 按行政区搜索
    result = getpoi(api_key='YOUR_KEY', cityname=['湖南省', '长沙市'], keywords='公交')
    print(result.bus_lines)

    # 按多边形区域搜索
    result = getpoi(api_key='YOUR_KEY', polygon='116.0,39.0|117.0,40.0', keywords='公交')
    print(result.bus_lines)
"""

import json
import urllib.request
from typing import List, Optional
from urllib.parse import quote

from . import citycode


class getpoi:
    """高德 POI 搜索获取公交线路名称。

    通过高德 v5 API 的文本搜索或多边形搜索获取区域内的公交线路名称。

    Attributes:
        bus_lines: 去重后的公交线路名称列表。

    Args:
        api_key: 高德 v5 API Key。
        cityname: 行政区划列表 [省, 市]（与 polygon 二选一）。
        keywords: 搜索关键字，默认 '公交'。
        polygon: 多边形区域坐标字符串（与 cityname 二选一）。

    Examples:
        >>> result = getpoi(api_key='key', cityname=['湖南省', '长沙市'])
        >>> isinstance(result.bus_lines, list)
        True
    """

    _URL_REGION = (
        'https://restapi.amap.com/v5/place/text?keywords=%s&region=%s'
        '&key=%s&page_size=25&show_fields=children&page_num=%s'
    )
    _URL_POLYGON = (
        'https://restapi.amap.com/v5/place/polygon?keywords=%s&polygon=%s'
        '&key=%s&page_size=25&show_fields=children&page_num=%s'
    )

    def __init__(self, **kwargs):
        self.api_key: str = kwargs.get('api_key')
        self.cityname: Optional[list] = kwargs.get('cityname', None)
        self.keywords: str = kwargs.get('keywords', '公交')
        self.polygon: Optional[str] = kwargs.get('polygon', None)
        self.bus_lines: List[str] = []

        self._citycode_data = citycode.codes_pip()
        self._fetch_bus_lines()

    def _fetch_bus_lines(self) -> None:
        """执行分页搜索并收集公交线路名称。"""
        for page in range(1, 101):
            if self.cityname and len(self.cityname) > 1:
                region_code = self._search_citycode()
                raw = self._get_poi_by_region(region_code, page)
                bus_data = json.loads(raw)

                if bus_data.get('status') == '0':
                    break
                if bus_data.get('count', '0') == '0':
                    break

                self.bus_lines += self._extract_lines(bus_data)

            if self.polygon and len(self.polygon) > 1:
                raw = self._get_poi_by_polygon(page)
                bus_data = json.loads(raw)

                if bus_data.get('status') == '0':
                    break
                if bus_data.get('count', '0') == '0':
                    break

                self.bus_lines += self._extract_lines(bus_data)

        self.bus_lines = list(set(self.bus_lines))

    @staticmethod
    def _extract_lines(poidata: dict) -> List[str]:
        """从 POI 搜索结果中提取公交线路名称。

        Args:
            poidata: 高德 API 返回的 JSON 数据。

        Returns:
            公交线路名称列表。
        """
        pois = poidata.get('pois', [])
        result = []
        for poi in pois:
            address = poi.get('address', '')
            if ';' in address:
                result.extend(address.split(';'))
            else:
                result.append(address)
        return result

    def _search_citycode(self) -> str:
        """查找城市的行政区划代码。

        Returns:
            行政区划代码（adcode）字符串。
        """
        qv, city_df = self._citycode_data
        city_bm = city_df.loc[self.cityname[0]]['citycode']
        code = qv.loc[self.cityname[1], city_bm]['adcode']
        return str(code)

    def _get_poi_by_region(self, region: str, page: int) -> str:
        """通过行政区代码搜索 POI。

        Args:
            region: 行政区划代码。
            page: 页码。

        Returns:
            JSON 响应字符串。
        """
        url = self._URL_REGION % (quote(self.keywords), region, self.api_key, page)
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf8')

    def _get_poi_by_polygon(self, page: int) -> str:
        """通过多边形区域搜索 POI。

        Args:
            page: 页码。

        Returns:
            JSON 响应字符串。
        """
        url = self._URL_POLYGON % (quote(self.keywords), self.polygon, self.api_key, page)
        with urllib.request.urlopen(url) as f:
            return f.read().decode('utf8')
