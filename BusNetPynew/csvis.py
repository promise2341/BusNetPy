"""交互式地图可视化模块。

基于 geopandas 的 explore() 方法（底层使用 folium）生成交互式地图，
支持站点图、线路图和叠加图的展示。

典型用法::

    from BusNetPynew.csvis import ksh_point, ksh_line, ksh_all

    # 站点分布图
    m = ksh_point(bus_stops_gdf)

    # 线路分布图（按线路名着色）
    m = ksh_line(bus_lines_gdf, columns_name='name')

    # 站点与线路叠加图
    m = ksh_all(bus_stops_gdf, bus_lines_gdf)
"""

from typing import Optional

import geopandas as gpd


def ksh_point(gdf: gpd.GeoDataFrame):
    """生成公交站点交互式地图。

    使用 OpenStreetMap 底图，以圆形标记展示站点位置。

    Args:
        gdf: 包含站点 Point 几何列的 GeoDataFrame。

    Returns:
        folium.Map 交互式地图对象。

    Examples:
        >>> import geopandas as gpd
        >>> from shapely.geometry import Point
        >>> gdf = gpd.GeoDataFrame(geometry=[Point(116.4, 39.9)], crs="EPSG:4326")
        >>> m = ksh_point(gdf)
    """
    return gdf.explore(tiles="openstreetmap", marker_kwds={"radius": 3})


def ksh_line(
    gdf: gpd.GeoDataFrame,
    columns_name: Optional[str] = None,
):
    """生成公交线路交互式地图。

    使用深色底图，支持按指定列名进行着色区分。

    Args:
        gdf: 包含线路 LineString 几何列的 GeoDataFrame。
        columns_name: 用于颜色分类的列名（如 'name'）。

    Returns:
        folium.Map 交互式地图对象。
    """
    gdf = gdf.copy()
    for col in gdf.columns:
        if col != 'geometry':
            gdf[col] = gdf[col].astype(str)
    return gdf.explore(
        tiles="cartodbdarkmatter",
        column=columns_name,
        cmap="plasma",
    )


def ksh_all(nodes: gpd.GeoDataFrame, lines: gpd.GeoDataFrame):
    """生成站点与线路叠加的交互式地图。

    线路以天蓝色显示，站点以粉色小圆点叠加在线路上方。

    Args:
        nodes: 包含站点 Point 几何列的 GeoDataFrame。
        lines: 包含线路 LineString 几何列的 GeoDataFrame。

    Returns:
        folium.Map 交互式地图对象。
    """
    m = lines.explore(color="skyblue", tiles="cartodbdarkmatter")
    return nodes.explore(m=m, color="pink", marker_kwds={"radius": 2})
