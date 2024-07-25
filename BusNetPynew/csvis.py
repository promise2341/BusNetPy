import osmnx as ox
import pandas as pd
import geopandas as gpd

def ksh_point(gdf):
    return gdf.explore(tiles="openstreetmap", marker_kwds={"radius": 3})

def ksh_line(gdf,columns_name=None):
    # 将所有列转换为Python内置类型
    for i in gdf.columns:
        if i != 'geometry':
            gdf[i] = gdf[i].astype(str)
    return gdf.explore(tiles="cartodbdarkmatter", column=columns_name,cmap="plasma")


def ksh_all(nodes,lines):
    m = lines.explore(color="skyblue", tiles="cartodbdarkmatter")
    return nodes.explore(m=m, color="pink", marker_kwds={"radius": 2})


