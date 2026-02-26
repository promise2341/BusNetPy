# BusNetPy 使用示例

本文档提供 BusNetPy 各功能的详细使用示例。

---

## 目录

- [1. 坐标转换](#1-坐标转换)
- [2. UTM 投影工具](#2-utm-投影工具)
- [3. 数据采集](#3-数据采集)
- [4. 数据构建](#4-数据构建)
- [5. 网络建模](#5-网络建模)
- [6. 指标计算](#6-指标计算)
- [7. 路径规划](#7-路径规划)
- [8. 可视化](#8-可视化)
- [9. 数据导出](#9-数据导出)

---

## 1. 坐标转换

高德地图使用 GCJ-02 坐标系，本工具库自动转换为 WGS-84 国际坐标系。

```python
from BusNetPynew.WGS1984 import gcj02towgs84, wgs84togcj02, main

# GCJ-02 转 WGS-84（高德坐标 → GPS坐标）
wgs_lng, wgs_lat = gcj02towgs84(116.397428, 39.90923)
print(f"WGS-84: ({wgs_lng:.6f}, {wgs_lat:.6f})")
# 输出: WGS-84: (116.391184, 39.907826)

# WGS-84 转 GCJ-02（GPS坐标 → 高德坐标）
gcj_lng, gcj_lat = wgs84togcj02(116.391184, 39.907826)

# 便捷接口（支持字符串输入）
coords = main("116.397428", "39.90923")
```

---

## 2. UTM 投影工具

```python
from BusNetPynew.utm_espg import (
    get_utm_epsg, latlon_to_utm, utm_to_latlon, haversine_distance
)

# 获取 UTM EPSG 代码
epsg = get_utm_epsg(116.4, 39.9)
print(f"EPSG: {epsg}")  # 32650

# 经纬度转 UTM 坐标
epsg_code, utm_x, utm_y = latlon_to_utm(116.4, 39.9)

# UTM 坐标转经纬度
lat, lon = utm_to_latlon(utm_x, utm_y, epsg_code)

# Haversine 距离计算
dist = haversine_distance(39.9, 116.4, 31.2, 121.5)
print(f"北京→上海: {dist:.2f} km")  # ~1071 km
```

---

## 3. 数据采集

### 3.1 通过行政区划方式采集

```python
from BusNetPynew.buspider import buspi

spider = buspi(
    province='湖南省',
    city='长沙',
    key='你的高德v3_API_Key',
    key_fwd='你的高德v5_API_Key',
    jscode='你的安全密钥',
    keyword='公交',
    region_xzq=['湖南省', '长沙市']  # 行政区划方式
)

# 执行采集
bus_stops, bus_lines = spider.businfo(save_path='./data/')

print(f"站点数: {len(bus_stops)}")
print(f"线路数: {len(bus_lines)}")
```

### 3.2 通过多边形区域采集

```python
spider = buspi(
    province='湖南省',
    city='长沙',
    key='你的高德v3_API_Key',
    key_fwd='你的高德v5_API_Key',
    jscode='你的安全密钥',
    keyword='公交',
    polygon_mult='112.8,28.1|113.2,28.1|113.2,28.4|112.8,28.4'
)

bus_stops, bus_lines = spider.businfo(save_path='./data/')
```

### 3.3 通过 8684.cn 获取线路列表

```python
from BusNetPynew.citybus import main

# 单个城市
lines = main('长沙')
print(f"长沙公交线路数: {len(lines)}")

# 多个城市
lines = main(['长沙', '株洲'])
```

---

## 4. 数据构建

将采集的 CSV 数据构建为结构化线网数据。

```python
from BusNetPynew.busbuild import read_busdata, build_route

# 读取 CSV 数据
df_line, df_point = read_busdata(
    path_line='./data/湖南省/csv/长沙公交线路.csv',
    path_point='./data/湖南省/csv/长沙公交站点.csv'
)

print(f"折线点数: {len(df_line)}")
print(f"站点数: {len(df_point)}")

# 构建结构化线网（投影到 EPSG:3857 计算距离，最终输出 WGS-84）
gdf = build_route(df_line, df_point, epsg=3857, wgs84=True)

print(f"线网段数: {len(gdf)}")
print(f"列名: {list(gdf.columns)}")
print(f"线路数: {gdf['name'].nunique()}")
```

### 输出字段说明

| 字段 | 说明 |
|------|------|
| `stationname` | 当前站点名称 |
| `nt_stationname` | 下一站名称 |
| `id` / `next_id` | 站点 ID |
| `name` | 线路全称 |
| `dir` | 正反线路标识 |
| `hx` | 实际线路段长（千米） |
| `zx_dis` | 起止点直线距离（千米） |
| `geometry` | LineString 几何 |

---

## 5. 网络建模

### 5.1 Space-L 网络

```python
from BusNetPynew.metrical import spaceL

G_L, pos = spaceL(gdf)

print(f"节点数: {G_L.number_of_nodes()}")
print(f"边数: {G_L.number_of_edges()}")

# 查看节点属性
for node, data in list(G_L.nodes(data=True))[:3]:
    print(f"站点: {data['staname']}, 线路数: {len(data['bus_lines'])}")
```

### 5.2 Space-P 网络

```python
from BusNetPynew.metrical import spacep
from BusNetPynew.busbuild import build_index

# 需要带 line_index 的站点数据
df_point_indexed = build_index(df_line, df_point)

G_P = spacep(df_point_indexed, gdf)

print(f"节点数: {G_P.number_of_nodes()}")
print(f"边数: {G_P.number_of_edges()}")
```

---

## 6. 指标计算

### 6.1 非直线系数

```python
from BusNetPynew.metrical import Nonline

base_line, cycle_line, fzxxs_base, fzxxs_hx = Nonline(
    gdf,
    base_path='非环线非直线系数.csv',
    hx_path='环线非直线系数.csv'
)

print(f"非环线平均非直线系数: {fzxxs_base:.4f}")
print(f"环线平均非直线系数: {fzxxs_hx:.4f}")
# 参考值: GB50220-95 规定单条≤1.4，全网均值 1.15~1.2
```

### 6.2 平均站间距

```python
from BusNetPynew.metrical import avg_station

avg_sta = avg_station(gdf, file_path='平均站间距.csv')
print(f"全网平均站间距: {avg_sta['hx'].mean():.4f} km")
```

### 6.3 重复系数

```python
from BusNetPynew.metrical import cf_all

cf = cf_all(G_L, gdf)
print(f"重复系数: {cf:.4f}")
```

### 6.4 最大共线边

```python
from BusNetPynew.metrical import unique_line

max_lines = unique_line(G_L)
print(f"最大共线路段经过 {len(max_lines)} 条线路")
```

### 6.5 最多线路站点

```python
from BusNetPynew.metrical import most_linesta

station = most_linesta(G_L)
print(f"经过线路最多的站点: {station}")
```

### 6.6 UTM EPSG 查询

```python
from BusNetPynew.metrical import get_utm_epsg_code

epsg = get_utm_epsg_code(112.97, 28.23)
print(f"长沙 UTM EPSG: {epsg}")
```

---

## 7. 路径规划

```python
from BusNetPynew.metrical import find_nearest_node
from BusNetPynew.routplaning import bus_route_planning

# 查找起终点最近的站点
node1, name1, dist1 = find_nearest_node(G_L, 112.97, 28.23)
node2, name2, dist2 = find_nearest_node(G_L, 113.02, 28.19)

print(f"起点: {name1} (距查询点 {dist1:.2f} km)")
print(f"终点: {name2} (距查询点 {dist2:.2f} km)")

# 执行路径规划
stations, path_gdf, length = bus_route_planning(G_P, G_L, node1, node2, gdf)

print(f"经过站点: {' → '.join(stations)}")
print(f"路径总长: {length:.2f} km")
print(f"路径段数: {len(path_gdf)}")
```

---

## 8. 可视化

### 8.1 静态网络图

```python
from BusNetPynew.metrical import G_ksh

G_ksh(G_L, pos)
```

### 8.2 matplotlib 线网图

```python
from BusNetPynew.busbuild import show_bus

show_bus(gdf)  # 彩色线段 + OpenStreetMap 底图
```

### 8.3 交互式地图

```python
from BusNetPynew.csvis import ksh_point, ksh_line, ksh_all

# 站点图
m = ksh_point(bus_stops)
m.save('站点地图.html')

# 线路图（按线路名着色）
m = ksh_line(gdf, columns_name='name')
m.save('线路地图.html')

# 叠加图
m = ksh_all(bus_stops, gdf)
m.save('叠加地图.html')
```

### 8.4 路径可视化

```python
# 将规划路径可视化
m = path_gdf.explore(color='red', tiles='openstreetmap')
m.save('路径规划.html')
```

---

## 9. 数据导出

### 9.1 导出为 Shapefile

```python
from BusNetPynew.busbuild import save_shp, save_point

# 导出线路
save_shp(gdf, save_path='bus_routes.shp')

# 导出站点
save_point(df_point, save_path='bus_stops.shp', epsg=4326)
```

### 9.2 导出为 CSV

```python
# GeoDataFrame 直接导出（不含几何列）
gdf.drop(columns='geometry').to_csv('bus_network.csv', encoding='utf-8', index=False)
```

### 9.3 通过 conversion_geo 模块导出

```python
from BusNetPynew.conversion_geo import main

main(
    path1='站点.csv',
    path2='线路信息.csv',
    path3='线路折线.csv',
    city='长沙',
    province='湖南省'
)
# 输出到 ./data/湖南省/shp/point/ 和 ./data/湖南省/shp/line/
```

---

## 完整工作流示例

```python
from BusNetPynew.buspider import buspi
from BusNetPynew.busbuild import read_busdata, build_route
from BusNetPynew.metrical import spaceL, spacep, Nonline, avg_station, cf_all, find_nearest_node
from BusNetPynew.routplaning import bus_route_planning
from BusNetPynew.csvis import ksh_all

# ① 数据采集
spider = buspi(
    province='湖南省', city='长沙',
    key='KEY', key_fwd='KEY_V5', jscode='JSCODE',
    keyword='公交', region_xzq=['湖南省', '长沙市']
)
bus_stops, bus_lines = spider.businfo(save_path='./data/')

# ② 数据构建
df_line, df_point = read_busdata(
    './data/湖南省/csv/长沙公交线路.csv',
    './data/湖南省/csv/长沙公交站点.csv'
)
gdf = build_route(df_line, df_point, epsg=3857)

# ③ 网络建模
G_L, pos = spaceL(gdf)
G_P = spacep(df_point, gdf)

# ④ 指标分析
base, cycle, fzxxs_b, fzxxs_h = Nonline(gdf, 'base.csv', 'hx.csv')
avg = avg_station(gdf, 'avg.csv')
cf = cf_all(G_L, gdf)

print(f"非直线系数: {fzxxs_b:.4f}")
print(f"平均站间距: {avg['hx'].mean():.4f} km")
print(f"重复系数: {cf:.4f}")

# ⑤ 路径规划
n1, _, _ = find_nearest_node(G_L, 112.97, 28.23)
n2, _, _ = find_nearest_node(G_L, 113.02, 28.19)
stations, path, length = bus_route_planning(G_P, G_L, n1, n2, gdf)

# ⑥ 可视化
m = ksh_all(bus_stops, gdf)
m.save('公交网络.html')
```
