"""8684 网站公交线路名称爬取模块。

通过爬取 8684.cn 网站获取指定城市的公交线路名称列表，
作为高德 API POI 搜索的替代数据源。

典型用法::

    from BusNetPynew.citybus import main

    bus_lines = main('长沙')  # 返回长沙市所有公交线路信息列表
"""

from typing import List, Dict, Union

import requests
from bs4 import BeautifulSoup
from pypinyin import lazy_pinyin


_DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/75.0.3770.80 Safari/537.36"
)


def getInitial(city_pinyin: str, user_agent: str) -> List[str]:
    """获取城市公交线路的首字母分类列表。

    Args:
        city_pinyin: 城市拼音名称（如 'changsha'）。
        user_agent: HTTP 请求的 User-Agent 头。

    Returns:
        线路分类标识列表（用于分页爬取）。
    """
    url = f'https://{city_pinyin}.8684.cn/list1'
    headers = {'User-Agent': user_agent}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    initial = soup.find_all('div', {'class': 'tooltip-inner'})[3]
    initial = initial.find_all('a')
    return [i.get_text() for i in initial]


def getLine(
    city: str,
    city_pinyin: str,
    page_id: str,
    user_agent: str,
    citybus_name: List[Dict[str, str]],
) -> None:
    """爬取指定分类页面下的公交线路名称。

    Args:
        city: 城市中文名称。
        city_pinyin: 城市拼音名称。
        page_id: 分类页面标识。
        user_agent: HTTP 请求的 User-Agent 头。
        citybus_name: 结果列表（原地追加）。
    """
    url = f'https://{city_pinyin}.8684.cn/list{page_id}'
    headers = {'User-Agent': user_agent}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    busline = soup.find('div', {'class': 'list clearfix'})
    busline = busline.find_all('a')
    for i in busline:
        citybus_name.append({"city": city, "name": i.get_text()})


def _city_to_pinyin(city: str) -> str:
    """将城市中文名转换为拼音字符串。

    Args:
        city: 城市中文名称。

    Returns:
        拼音字符串。

    Examples:
        >>> _city_to_pinyin('长沙')
        'changsha'
    """
    return ''.join(lazy_pinyin(city))


def main(city: Union[str, List[str]]) -> List[Dict[str, str]]:
    """获取城市的公交线路名称列表。

    支持传入单个城市名或城市名列表。

    Args:
        city: 城市中文名称或城市名称列表。

    Returns:
        公交线路信息列表，每项为 {'city': '城市名', 'name': '线路名'}。

    Examples:
        >>> lines = main('长沙')
        >>> lines[0].keys()
        dict_keys(['city', 'name'])
    """
    user_agent = _DEFAULT_USER_AGENT
    citybus_name: List[Dict[str, str]] = []

    if isinstance(city, list):
        for c in city:
            city_pinyin = _city_to_pinyin(c)
            initial_list = getInitial(city_pinyin, user_agent)
            for page_id in initial_list:
                getLine(c, city_pinyin, page_id, user_agent, citybus_name)
    else:
        city_pinyin = _city_to_pinyin(city)
        initial_list = getInitial(city_pinyin, user_agent)
        for page_id in initial_list:
            getLine(city, city_pinyin, page_id, user_agent, citybus_name)

    return citybus_name
