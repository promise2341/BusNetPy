import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString,Point,Polygon,mapping
from pypinyin import lazy_pinyin
import os
import requests
from ChineseAdminiDivisionsDict import CitiesCode, ProvinceCode

def boundary_judgment(city,gdf):
    try:
        url = "https://geo.datav.aliyun.com/areas/bound/geojson?code={}".format(CitiesCode[str(city)])
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}
        a = requests.get(url, headers=headers)
        datas = gpd.read_file(a.text, ensure_ascii=False)
        boundary = datas.drop(list(datas.columns[[0,2,3,4,5]]),axis=1)
        points_with_boundary = gpd.sjoin(gdf,boundary, how="inner", op='intersects')
        if points_with_boundary.empty == False:
            return points_with_boundary
        else:
            return gdf
    except:
        return gdf
        print("【程序警告】:\n未查询到{}的行政边界，将不会对{}公交站点进行地理校对，请手动删除{}其他区域的公交站点".format(city,city,city))

def point_to_line(df):
    return LineString(df.sort_values("序号")[["lng","lat"]].values)

def Create_busline(path2,path3,city,now_path):
    if os.path.isdir(now_path+"/line")==False:
        os.mkdir(now_path+"/line")
    df = pd.read_csv(path3)
    busline = (df
           .groupby("全称")
           .apply(point_to_line)
           .to_frame(name="geometry")
           .pipe(gpd.GeoDataFrame,crs="EPSG:4326"))
    buslines_polyline = pd.read_csv(path2)
    busline = busline.merge(buslines_polyline, on='全称')
    busline = busline.drop_duplicates('全称')

    cityName = ""
    for i in lazy_pinyin(city):
        cityName += str(i)
    #city = lazy_pinyin(city)[0] + lazy_pinyin(city)[1] 
    linepath = now_path+"/line/" + cityName + "_busline.shp"
    busline.to_file(linepath,encoding = 'gb18030')

def point(path1,city,now_path):
    if os.path.isdir(now_path+"/point")==False:
        os.mkdir(now_path+"/point")
    bus_station = pd.read_csv(path1)
    bus_station = bus_station.drop_duplicates('id')
    gdf_bus_station = gpd.GeoDataFrame(bus_station, geometry=gpd.points_from_xy(bus_station.lng, bus_station.lat))
    gdf_bus_station.crs = 'EPSG:4326'
    
    point_shp = boundary_judgment(city,gdf_bus_station)
    cityName = ""
    for i in lazy_pinyin(city):
        cityName += str(i)
    #city = lazy_pinyin(city)[0] + lazy_pinyin(city)[1] 
    pointpath = now_path+"/point/" + cityName + "_buspoint.shp"
    point_shp.to_file(pointpath,encoding = 'gb18030') 

def main(path1,path2,path3,city,province):
    
    now_path = os.getcwd()+"/data/" + province + "/shp"
    
    if os.path.isdir(now_path)==False:
        os.mkdir(now_path)

    """站点shp数据保存"""
    point(path1,city,now_path)
    """线路shp数据保存"""
    Create_busline(path2,path3,city,now_path)
