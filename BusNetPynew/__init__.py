"""BusNetPy —— 城市公交网络数据采集、构建与分析工具库。

本包提供从公交数据采集到网络拓扑分析的完整工作流：
    - 数据采集：通过高德地图 API 和 8684.cn 网站获取公交数据
    - 数据构建：将原始数据处理为站点间衔接的结构化 GeoDataFrame
    - 网络建模：构建 Space-L 和 Space-P 拓扑网络模型
    - 指标计算：非直线系数、平均站间距、重复系数等
    - 路径规划：基于图网络的公交换乘最短路径规划
    - 可视化：静态图和交互式地图

典型用法::

    from BusNetPynew import buspider, busbuild, metrical, routplaning, csvis
"""

__version__ = "0.1.0"
__author__ = "promise2341"

__all__ = [
    # 核心模块
    "buspider",
    "busbuild",
    "metrical",
    "routplaning",
    "csvis",
    # 分析模块
    "accessibility",
    "optimization",
    "transfer",
    "resilience",
    "poi_bindling",
    # 工具模块
    "find_cycle",
    "buslist",
    "citybus",
    "WGS1984",
    "citycode",
    "utm_espg",
    "utils",
    "conversion_geo",
    "ChineseAdminiDivisionsDict",
]
