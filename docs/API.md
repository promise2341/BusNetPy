# BusNetPy API 参考文档

本文档详细介绍 BusNetPy 各模块的公开 API。

---

## 目录

- [buspider 模块](#buspider-模块)
- [busbuild 模块](#busbuild-模块)
- [metrical 模块](#metrical-模块)
- [routplaning 模块](#routplaning-模块)
- [csvis 模块](#csvis-模块)
- [WGS1984 模块](#wgs1984-模块)
- [find_cycle 模块](#find_cycle-模块)
- [utm_espg 模块](#utm_espg-模块)
- [buslist 模块](#buslist-模块)
- [citybus 模块](#citybus-模块)
- [utils 模块](#utils-模块)

---

## buspider 模块

> `BusNetPynew.buspider`

公交数据采集主模块，通过高德地图 REST API 采集公交数据。

### `class buspi(**kwargs)`

公交数据采集器。

**参数：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `province` | `str` | 是 | 省份名称 |
| `city` | `str` | 是 | 城市名称 |
| `key` | `str` | 是 | 高德 v3 API Key |
| `key_fwd` | `str` | 是 | 高德 v5 API Key |
| `jscode` | `str` | 是 | 高德 JavaScript 安全密钥 |
| `keyword` | `str` | 否 | 搜索关键字，默认 `'公交'` |
| `region_xzq` | `list` | 否 | 行政区划 `[省, 市]`，与 `polygon_mult` 二选一 |
| `polygon_mult` | `str` | 否 | 多边形区域坐标字符串 |

#### `buspi.businfo(save_path=None)`

执行数据采集。

**参数：**
- `save_path` (`str`): 数据保存根目录

**返回：** `(GeoDataFrame, GeoDataFrame)` — 站点数据和线路数据

#### `buspi.bus_to_shpfile(gdf, file_path=None)`

将 GeoDataFrame 保存为 Shapefile。

#### `buspi.re_col(gdf, col=None)` [静态方法]

重命名 GeoDataFrame 列名。

---

## busbuild 模块

> `BusNetPynew.busbuild`

公交数据构建模块，将原始 CSV 数据处理为结构化线网 GeoDataFrame。

### `read_busdata(path_line, path_point, encod_line='utf-8', encod_point='utf-8')`

读取线路折线和站点 CSV 数据。

**参数：**
- `path_line` (`str`): 线路折线 CSV 路径
- `path_point` (`str`): 站点 CSV 路径
- `encod_line` (`str`): 线路文件编码
- `encod_point` (`str`): 站点文件编码

**返回：** `(DataFrame, DataFrame)` — 线路数据和站点数据

### `build_route(line, point, epsg=3857, wgs84=True)`

构建完整的结构化公交线网数据。

**参数：**
- `line` (`DataFrame`): 线路折线数据
- `point` (`DataFrame`): 站点数据
- `epsg` (`int`): 投影坐标系 EPSG 代码，默认 3857
- `wgs84` (`bool`): 是否转换回 WGS-84

**返回：** `GeoDataFrame` — 结构化线网，含以下关键字段：

| 字段 | 说明 |
|------|------|
| `stationname` | 当前站点名称 |
| `nt_stationname` | 下一站名称 |
| `id` | 当前站点 ID |
| `next_id` | 下一站 ID |
| `name` | 线路全称 |
| `hx` | 段长（千米） |
| `zx_dis` | 直线距离（千米） |
| `geometry` | LineString 几何 |

### `show_bus(gdf)`

可视化公交线网（matplotlib + contextily 底图）。

### `save_shp(gdf, save_path)`

将线网 GeoDataFrame 保存为 Shapefile。

### `save_point(point, save_path, epsg=4326)`

将站点数据保存为 Shapefile。

---

## metrical 模块

> `BusNetPynew.metrical`

网络分析指标计算模块。

### `spaceL(gdf)`

构建 Space-L 拓扑网络（相邻站点连接）。

**参数：**
- `gdf` (`GeoDataFrame`): 结构化线网数据

**返回：** `(nx.Graph, dict)` — 网络图和节点位置字典

节点属性：
- `pos`: `(lng, lat)` 坐标
- `staname`: 站点名称
- `bus_lines`: 经过的公交线路列表

边属性：
- `length`: 线段长度（千米）
- `bus_lines`: 经过的公交线路列表

### `spacep(df_point, gdf)`

构建 Space-P 拓扑网络（同线路站点全连接）。

**参数：**
- `df_point` (`DataFrame`): 站点数据
- `gdf` (`GeoDataFrame`): 结构化线网数据

**返回：** `nx.Graph`

### `Nonline(gdf, base_path=None, hx_path=None)`

计算非直线系数。

**参数：**
- `gdf` (`GeoDataFrame`): 线网数据
- `base_path` (`str`, 可选): 非环线结果保存路径
- `hx_path` (`str`, 可选): 环线结果保存路径

**返回：** `(DataFrame, DataFrame, float, float)` — 非环线数据、环线数据、非环线均值、环线均值

### `avg_station(gdf, file_path=None)`

计算各线路平均站间距。

**返回：** `DataFrame` — 各线路平均站间距

### `cf_all(G_L, gdf)`

计算重复系数（实际运营里程 / 网络拓扑长度）。

**返回：** `float`

### `unique_line(G_L)`

查找共线线路最多的站点区间。

**返回：** `list[str]` — 去重后的线路名称列表

### `most_linesta(G_L)`

查找经过线路最多的站点。

**返回：** `str` 或 `None`

### `find_nearest_node(G, longitude, latitude)`

在网络中查找最近节点。

**返回：** `(node_id, station_name, distance_km)`

### `G_ksh(G_L, pos)`

可视化 Space-L 网络拓扑图。

### `route_to_84(gdf)`

将非 WGS-84 的 GeoDataFrame 转为 WGS-84。

---

## routplaning 模块

> `BusNetPynew.routplaning`

公交路径规划模块。

### `bus_route_planning(G_P, G_L, node1, node2, gdf)`

完整的公交路径规划流程。

**参数：**
- `G_P` (`nx.Graph`): Space-P 网络
- `G_L` (`nx.Graph`): Space-L 网络
- `node1`: 起始节点 ID
- `node2`: 目标节点 ID
- `gdf` (`GeoDataFrame`): 线网数据

**返回：** `(list[str], GeoDataFrame, float)` — 站点列表、路径几何、总长度

### `GP_planning(G_P, node1, node2)`

Space-P 网络最短路径搜索（含换乘惩罚）。

### `route_sta_analy(G_P, nodes)`

提取路径站点名称列表。

### `route_linena_analy(G_P, nodes)`

提取路径线路名称列表。

### `filtered_edges(G_L, linename_list)`

从 Space-L 网络筛选指定线路子图。

### `busroute_result(G_filtered, node1, node2, gdf, linename_list)`

从子图中提取路径几何。

---

## csvis 模块

> `BusNetPynew.csvis`

交互式地图可视化模块（基于 folium）。

### `ksh_point(gdf)`

站点分布交互式地图。

### `ksh_line(gdf, columns_name=None)`

线路分布交互式地图，支持按列着色。

### `ksh_all(nodes, lines)`

站点与线路叠加交互式地图。

---

## WGS1984 模块

> `BusNetPynew.WGS1984`

坐标系转换模块。

### `gcj02towgs84(lng, lat)`

GCJ-02 转 WGS-84。

**返回：** `[wgs_lng, wgs_lat]`

### `wgs84togcj02(lng, lat)`

WGS-84 转 GCJ-02。

**返回：** `[gcj_lng, gcj_lat]`

### `main(lng, lat)`

GCJ-02 转 WGS-84 的便捷接口（支持字符串输入）。

### `out_of_china(lng, lat)`

判断坐标是否在中国境外。

---

## find_cycle 模块

> `BusNetPynew.find_cycle`

### `find_cycle(sequence)`

检测序列中的最短重复循环模式。

**参数：**
- `sequence` (`list`): 待检测序列

**返回：** 最短循环子序列，无重复则返回原序列

---

## utm_espg 模块

> `BusNetPynew.utm_espg`

UTM 投影工具模块。

### `get_utm_epsg(longitude, latitude)`

获取 UTM EPSG 代码。

### `latlon_to_utm(longitude, latitude)`

经纬度转 UTM。**返回：** `(epsg_code, utm_x, utm_y)`

### `utm_to_latlon(utm_x, utm_y, epsg_code)`

UTM 转经纬度。**返回：** `(latitude, longitude)`

### `haversine_distance(lat1, lon1, lat2, lon2)`

Haversine 大圆距离（千米）。

### `find_nearest_node(G, longitude, latitude)`

在图网络中查找最近节点。

---

## buslist 模块

> `BusNetPynew.buslist`

### `class getpoi(**kwargs)`

高德 POI 搜索获取公交线路名称。

**参数：**

| 参数 | 类型 | 说明 |
|------|------|------|
| `api_key` | `str` | 高德 v5 API Key |
| `cityname` | `list` | 行政区划 `[省, 市]` |
| `keywords` | `str` | 搜索关键字 |
| `polygon` | `str` | 多边形区域坐标 |

**属性：**
- `bus_lines` (`list[str]`): 公交线路名称列表

---

## citybus 模块

> `BusNetPynew.citybus`

### `main(city)`

通过 8684.cn 获取城市公交线路名称列表。

**参数：**
- `city` (`str` 或 `list[str]`): 城市名或城市名列表

**返回：** `list[dict]` — `[{'city': '...', 'name': '...'}, ...]`

---

## utils 模块

> `BusNetPynew.utils`

公共工具函数模块。

### `get_first_coord(geometry)`

提取 LineString 第一个坐标点。

### `get_last_coord(geometry)`

提取 LineString 最后一个坐标点。

### `euclidean_distance_km(x1, y1, x2, y2)`

投影坐标欧氏距离（千米）。

### `haversine_distance(lat1, lon1, lat2, lon2)`

WGS-84 Haversine 大圆距离（千米）。

### `extract_endpoint_coords(gdf)`

提取 GeoDataFrame 起止点坐标并计算直线距离。

### `get_utm_zone(longitude, latitude)`

获取 UTM 带号和半球。

### `get_utm_epsg(longitude, latitude)`

获取 UTM EPSG 代码字符串。
