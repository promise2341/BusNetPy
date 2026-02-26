# BusNetPy —— 公交网络分析工具库

<p align="center">
  <strong>基于 Python 的城市公交网络数据采集、构建与分析工具库</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform">
</p>

---

## 目录

- [简介](#简介)
- [功能特性](#功能特性)
- [安装](#安装)
- [快速开始](#快速开始)
- [模块说明](#模块说明)
- [使用流程](#使用流程)
- [API 文档](#api-文档)
- [示例](#示例)
- [依赖库](#依赖库)
- [项目结构](#项目结构)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)

---

## 简介

**BusNetPy** 是一个面向城市公共交通研究的 Python 工具库，提供从数据采集到网络分析的完整工作流。支持通过高德地图 API 和 8684 网站获取公交线路数据，构建 Space-L 和 Space-P 拓扑网络模型，计算非直线系数、平均站间距、重复系数等核心指标，并支持公交路径规划和地理可视化。

本工具库适用于城市交通规划、公交网络评价、学术研究等场景。

---

## 功能特性

| 功能模块 | 说明 |
|---------|------|
| **数据采集** | 通过高德地图 REST API（v3/v5）采集公交站点、线路信息和折线坐标 |
| **网页爬取** | 通过 8684.cn 网站爬取城市公交线路名称列表 |
| **坐标转换** | 支持 GCJ-02（高德坐标）与 WGS-84（国际坐标）互转 |
| **数据构建** | 将原始数据构建为站点间衔接的结构化 GeoDataFrame |
| **网络建模** | 构建 Space-L（相邻站点连接）和 Space-P（同线路站点全连接）拓扑网络 |
| **指标计算** | 非直线系数、平均站间距、重复系数、最大共线边、最多线路站点 |
| **路径规划** | 基于 Space-P 网络的公交换乘最短路径规划 |
| **可视化** | 静态图（matplotlib）和交互式地图（folium/geopandas） |
| **数据导出** | 导出为 Shapefile、CSV 等格式 |
| **可达性分析** | 等时圈分析、站点覆盖率、出行时间矩阵 |
| **线网优化** | 重复路段识别、覆盖盲区检测、站间距异常检测、线路效率评估 |
| **换乘分析** | 换乘站识别与评级、直达率分析、线路换乘关联矩阵 |
| **网络韧性** | 关键节点识别、失效模拟、冗余度分析、渐进式攻击健壮性评估 |
| **POI 联动** | 站点周边 POI 画像、公共设施可达性、职住通勤分析 |

---

## 安装

### 环境要求

- Python >= 3.8
- pip 包管理器

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/promise2341/BusNetPy.git
cd BusNetPy

# 2. 安装依赖
pip install -r requirements.txt
```

### 依赖库

主要依赖：

| 库名 | 用途 |
|------|------|
| `pandas` | 数据处理与分析 |
| `geopandas` | 地理空间数据处理 |
| `shapely` | 几何对象操作 |
| `networkx` | 图与网络分析 |
| `requests` | HTTP 请求（API 调用） |
| `beautifulsoup4` | 网页解析（8684 爬虫） |
| `matplotlib` | 静态可视化 |
| `contextily` | 底图瓦片服务 |
| `pyproj` | 坐标系投影变换 |
| `tqdm` | 进度条显示 |
| `fuzzywuzzy` | 模糊字符串匹配 |
| `pypinyin` | 中文转拼音 |
| `osmnx` | OpenStreetMap 网络分析 |

---

## 快速开始

### 1. 数据采集

使用高德地图 API 采集公交数据，需要先申请 [高德开放平台](https://lbs.amap.com/) 的 API Key。

```python
from BusNetPynew.buspider import buspi

# 初始化采集器
spider = buspi(
    province='湖南省',
    city='长沙',
    key='你的高德API_Key',
    key_fwd='你的高德API_Key_v5',
    jscode='你的安全密钥',
    keyword='公交',
    region_xzq=['湖南省', '长沙市']  # 行政区划方式
)

# 执行采集，返回站点和线路 GeoDataFrame
bus_stops, bus_lines = spider.businfo(save_path='./data/')
```

### 2. 数据构建

将采集的原始数据构建为站点间衔接的结构化线网数据：

```python
from BusNetPynew.busbuild import read_busdata, build_route

# 读取 CSV 数据
df_line, df_point = read_busdata(
    path_line='线路折线.csv',
    path_point='站点数据.csv'
)

# 构建结构化线网（默认投影 EPSG:3857，输出转回 WGS84）
gdf_route = build_route(df_line, df_point, epsg=3857, wgs84=True)
```

### 3. 网络建模

构建 Space-L 和 Space-P 拓扑网络：

```python
from BusNetPynew.metrical import spaceL, spacep

# Space-L 网络（相邻站点连接）
G_L, pos = spaceL(gdf_route)

# Space-P 网络（同线路站点全连接）
G_P = spacep(df_point, gdf_route)
```

### 4. 指标计算

```python
from BusNetPynew.metrical import Nonline, avg_station, cf_all, unique_line, most_linesta

# 非直线系数
base_line, cycle_line, fzxxs_base, fzxxs_hx = Nonline(
    gdf_route, base_path='非环线.csv', hx_path='环线.csv'
)

# 平均站间距
avg_sta = avg_station(gdf_route, file_path='平均站间距.csv')

# 重复系数
cf = cf_all(G_L, gdf_route)

# 最大共线边
max_lines = unique_line(G_L)

# 最多线路站点
most_linesta(G_L)
```

### 5. 路径规划

```python
from BusNetPynew.metrical import find_nearest_node
from BusNetPynew.routplaning import bus_route_planning

# 查找最近站点
node1, name1, dist1 = find_nearest_node(G_L, lng=112.97, lat=28.23)
node2, name2, dist2 = find_nearest_node(G_L, lng=113.02, lat=28.19)

# 公交路径规划
stations, path_gdf, length = bus_route_planning(G_P, G_L, node1, node2, gdf_route)
```

### 6. 可视化

```python
from BusNetPynew.csvis import ksh_point, ksh_line, ksh_all
from BusNetPynew.metrical import G_ksh

# 静态网络图
G_ksh(G_L, pos)

# 交互式地图
ksh_line(gdf_route, columns_name='name')  # 线路图
ksh_point(bus_stops)                        # 站点图
ksh_all(bus_stops, gdf_route)              # 叠加图
```

---

## 模块说明

| 模块 | 文件 | 功能 |
|------|------|------|
| `buspider` | `buspider.py` | 公交数据采集主模块，调用高德 API 获取线路和站点数据 |
| `busbuild` | `busbuild.py` | 数据构建模块，将原始数据处理为结构化公交线网 |
| `metrical` | `metrical.py` | 网络分析指标模块，计算非直线系数、站间距、构建网络拓扑 |
| `routplaning` | `routplaning.py` | 公交路径规划模块，基于 Space-P 的最短路径算法 |
| `csvis` | `csvis.py` | 交互式可视化模块，基于 geopandas 的 folium 地图 |
| `buslist` | `buslist.py` | 公交线路名称列表获取（高德 POI 搜索） |
| `citybus` | `citybus.py` | 通过 8684.cn 网站爬取公交线路名称 |
| `WGS1984` | `WGS1984.py` | GCJ-02 与 WGS-84 坐标互转 |
| `find_cycle` | `find_cycle.py` | 环线检测，识别公交线路中的环形模式 |
| `citycode` | `citycode.py` | 全国城市行政编码数据（adcode/citycode） |
| `utm_espg` | `utm_espg.py` | UTM 投影带号计算与坐标变换工具 |
| `accessibility` | `accessibility.py` | 可达性分析（等时圈、覆盖率、时间矩阵） |
| `optimization` | `optimization.py` | 线网优化建议（重复路段、盲区、站间距） |
| `transfer` | `transfer.py` | 换乘分析（换乘站识别、直达率、关联矩阵） |
| `resilience` | `resilience.py` | 网络韧性（关键节点、失效模拟、冗余度） |
| `poi_bindling` | `poi_bindling.py` | POI 联动（设施可达性、通勤分析） |
| `utils` | `utils.py` | 公共工具函数（坐标提取、距离计算等） |
| `ChineseAdminiDivisionsDict` | `ChineseAdminiDivisionsDict.py` | 中国行政区划编码字典 |
| `conversion_geo` | `conversion_geo.py` | 地理边界校验与 Shapefile 导出 |

---

## 使用流程

```
数据采集 ──→ 数据构建 ──→ 网络建模 ──→ 指标分析 ──→ 可视化/导出
                                    │
                                    ├──→ 路径规划
                                    ├──→ 可达性分析（等时圈/覆盖率）
                                    ├──→ 换乘分析（换乘站/直达率）
                                    ├──→ 线网优化（盲区/冗余/效率）
                                    ├──→ 网络韧性（关键节点/失效模拟）
                                    └──→ POI 联动（设施可达/通勤分析）
```

**详细流程：**

1. **数据采集**（`buspider`）：通过高德 API 采集公交站点坐标、线路信息、线路折线
2. **数据构建**（`busbuild`）：读取 CSV 数据，建立站点索引，构建前后站衔接关系，生成 GeoDataFrame
3. **网络建模**（`metrical`）：构建 Space-L（相邻连接）和 Space-P（同线全连接）图网络
4. **指标分析**（`metrical`）：计算非直线系数、平均站间距、重复系数等
5. **路径规划**（`routplaning`）：基于网络模型进行公交出行路径规划
6. **可视化**（`csvis`/`metrical`）：静态图和交互式地图展示

---

## 项目结构

```
BusNetPy/
├── BusNetPynew/                     # 主包目录
│   ├── __init__.py                  # 包初始化与导出
│   ├── buspider.py                  # 数据采集模块
│   ├── busbuild.py                  # 数据构建模块
│   ├── metrical.py                  # 网络分析指标模块
│   ├── routplaning.py               # 路径规划模块
│   ├── csvis.py                     # 交互式可视化模块
│   ├── buslist.py                   # POI 搜索获取线路列表
│   ├── citybus.py                   # 8684 网站爬虫
│   ├── WGS1984.py                   # 坐标转换（GCJ-02 ↔ WGS-84）
│   ├── find_cycle.py                # 环线检测
│   ├── utils.py                     # 公共工具函数
│   ├── citycode.py                  # 城市行政编码
│   ├── utm_espg.py                  # UTM 投影工具
│   ├── ChineseAdminiDivisionsDict.py  # 行政区划字典
│   └── conversion_geo.py            # 地理校验与导出
├── tests/                           # 单元测试
│   ├── __init__.py
│   └── test_core.py                 # 核心功能测试
├── docs/                            # 文档目录
│   ├── API.md                       # API 参考文档
│   └── examples.md                  # 使用示例
├── requirements.txt                 # 依赖列表
├── AGENTS.md                        # 开发环境说明
└── README.md                        # 项目说明文档
```

---

## 核心概念

### Space-L 网络

Space-L 拓扑网络中，**只有相邻站点之间存在边**。该模型保留了公交线路的地理拓扑关系，适用于：
- 分析公交线网的空间覆盖
- 计算重复系数（实际线路长度 / 网络长度）
- 识别最大共线路段

### Space-P 网络

Space-P 拓扑网络中，**同一条线路上的任意两个站点之间都存在边**。该模型体现了乘客的可达性，适用于：
- 公交路径规划
- 可达性分析
- 换乘方案计算

### 非直线系数

非直线系数 = 线路实际长度 / 起终点直线距离。根据《城市道路交通规划设计规范 GB50220-95》，单条线路非直线系数不应大于 1.4，全网平均值以 1.15～1.2 为宜。

---

## 常见问题

### Q: 需要哪些 API Key？

使用数据采集功能需要高德开放平台的 Web 服务 API Key：
- `key`：高德 v3 API Key（公交线路详情查询）
- `key_fwd`：高德 v5 API Key（POI 搜索）
- `jscode`：JavaScript 安全密钥

申请地址：[https://lbs.amap.com/](https://lbs.amap.com/)

### Q: 不用 API Key 能做什么？

所有离线分析功能（网络建模、指标计算、路径规划、可视化）均可使用预采集的 CSV 数据运行，无需 API Key。

### Q: 坐标系是什么？

- 高德 API 返回的坐标为 **GCJ-02** 坐标系
- 本工具库自动将其转换为 **WGS-84** 国际通用坐标系
- 指标计算时会投影至 **UTM** 或 **EPSG:3857** 坐标系以保证距离精度

### Q: 支持哪些城市？

支持中国大陆所有城市，城市行政编码数据已内置于 `citycode.py` 模块。

---

## 贡献指南

1. Fork 本仓库
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m "Add your feature"`
4. 推送分支：`git push origin feature/your-feature`
5. 提交 Pull Request

### 代码规范

- 遵循 PEP 8 代码风格
- 函数签名使用类型注解
- 公共函数编写 Google 风格的 docstring
- 新功能需附带单元测试

---

## 许可证

本项目采用 MIT 许可证。
