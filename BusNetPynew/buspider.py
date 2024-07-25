from urllib.parse import quote
import urllib
import pandas as pd
import xlwt
import json
from . import citycode
from . import buslist
import requests
import csv
import random
import time
from . import WGS1984
from . import citybus
# from . import conversion_geo
import os
import pandas as pd
from tqdm import tqdm
from shapely.geometry import Point,LineString
import geopandas as gpd
import warnings
from fuzzywuzzy import fuzz
import re

warnings.filterwarnings("ignore")


class buspi:

    def __init__(self,**kwargs):
        self.province = kwargs.get('province')
        self.city = kwargs.get('city')
        self.key = kwargs.get('key')
        self.key_fwd = kwargs.get('key_fwd')
        self.keyword = kwargs.get('keyword')
        self.jscode = kwargs.get('jscode')
        # self.save_path = kwargs.get('save_path')
        self.region_xzq = kwargs.get('region_xzq',None)
        self.polygon_mult = kwargs.get('polygon_mult',None)

        

    def businfo(self,save_path=None):

        # 参数
        province = self.province
        city = self.city
        key = self.key
        keyword = self.keyword
        key_fwd = self.key_fwd
        jscode = self.jscode
        # save_path = self.save_path
        region_xzq = self.region_xzq
        polygon_mult = self.polygon_mult

        

        relistname = []

        # 判断结果相似性
        def find_best_match(target, options):
            best_match = None
            highest_score = 0
            
            for option in options:
                score = fuzz.ratio(target, option)
                if score > highest_score:
                    highest_score = score
                    best_match = option
            
            return best_match, highest_score
        

        # 判断是否有数字
        def contains_digit(s):
            return any(char.isdigit() for char in s)
        
        # 对关键字切片工具
        def remove_after_last_digit(text):
            # 查找字符串中的所有数字及其索引
            digits = [(m.start(), m.group()) for m in re.finditer(r'\d', text)]
            
            if not digits:
                # 如果没有数字，返回原字符串
                return text
            
            # 找到索引最大的数字
            max_index = digits[-1][0]
            
            # 删除从该索引之后的所有字符
            return text[:max_index + 1]


        # 站点信息
        def station(html, keywords, bus_station, buslines_information, buslines_polyline, city):
            buslines = html["buslines"]
            count = 0
            if len(buslines)<2:
                
                # 如果不是则正常运行
                for i in buslines:
                    # 判断是否已经查如果该线路
                    if i['name'] not in relistname:
                        
                        relistname.append(i['name'])
                        count = count + 1
                        busstops = i["busstops"]
                        my_new_busline = []
                        """站点信息"""
                        for T in busstops:
                            cell = []
                            lng1 = T["location"].split(",")[0]
                            lat1 = T["location"].split(",")[1]
                            cell = [city, T["name"], WGS1984.main(lng1, lat1)[0], WGS1984.main(lng1, lat1)[1], T["id"], i["name"],
                                    count]
                            with open(bus_station, 'a', newline='', encoding='utf-8') as f:
                                write = csv.writer(f)
                                write.writerow(cell)

                        """线路信息"""
                        information = [city, count, keywords[0:4], i["name"], i["basic_price"], i["total_price"], i["distance"],
                                    i["start_stop"], i["end_stop"], i["type"], i["start_time"], i["end_time"]]
                        with open(buslines_information, 'a', newline='', encoding='utf-8') as f:
                            write = csv.writer(f)
                            write.writerow(information)

                        """线路路线"""
                        polyline = i["polyline"]
                        split_polyline = polyline.split(";")
                        cou = 0
                        buslines_name2 = i["name"]
                        for i in split_polyline:
                            cou = cou + 1
                            excessive = i.split(",")
                            bus_polyline = [city, cou, buslines_name2, keywords[0:4], WGS1984.main(excessive[0], excessive[1])[0],
                                            WGS1984.main(excessive[0], excessive[1])[1]]
                            with open(buslines_polyline, 'a', newline='', encoding='utf-8') as f:
                                write = csv.writer(f)
                                write.writerow(bus_polyline)

            # 如果不是则需要判断返回的name的相似性
            else: 
                if fuzz.ratio(buslines[0]['name'], buslines[1]['name']) > 49:
                    # 那么也正常运行
                    for i in buslines:
                        # 判断是否已经查如果该线路
                        if i['name'] not in relistname:
                            relistname.append(i['name'])
                            count = count + 1
                            busstops = i["busstops"]
                            """站点信息"""
                            for T in busstops:
                                cell = []
                                lng1 = T["location"].split(",")[0]
                                lat1 = T["location"].split(",")[1]
                                cell = [city, T["name"], WGS1984.main(lng1, lat1)[0], WGS1984.main(lng1, lat1)[1], T["id"], i["name"],
                                        count]
                                with open(bus_station, 'a', newline='', encoding='utf-8') as f:
                                    write = csv.writer(f)
                                    write.writerow(cell)

                            """线路信息"""
                            information = [city, count, keywords[0:4], i["name"], i["basic_price"], i["total_price"], i["distance"],
                                        i["start_stop"], i["end_stop"], i["type"], i["start_time"], i["end_time"]]
                            with open(buslines_information, 'a', newline='', encoding='utf-8') as f:
                                write = csv.writer(f)
                                write.writerow(information)

                            """线路路线"""
                            polyline = i["polyline"]
                            split_polyline = polyline.split(";")
                            cou = 0
                            buslines_name2 = i["name"]
                            for i in split_polyline:
                                cou = cou + 1
                                excessive = i.split(",")
                                bus_polyline = [city, cou, buslines_name2, keywords[0:4], WGS1984.main(excessive[0], excessive[1])[0],
                                                WGS1984.main(excessive[0], excessive[1])[1]]
                                with open(buslines_polyline, 'a', newline='', encoding='utf-8') as f:
                                    write = csv.writer(f)
                                    write.writerow(bus_polyline)
                else:
                    my_new_busline = []
                    target = keywords
                    options = [buslines[0]['name'], buslines[1]['name']]
                    best_match, score = find_best_match(target, options)
                    indices = [index_match for index_match , value in enumerate(options) if value == best_match]
                    
                    # print(options)
                    # print(target)
                    # print(indices)
                    my_new_busline.append(buslines[indices[0]])
                    # print(my_new_busline)
                    # 那么也正常运行
                    for i in my_new_busline:
                        # 判断是否已经查如果该线路
                        if i['name'] not in relistname:
                            relistname.append(i['name'])
                            count = count + 1
                            busstops = i["busstops"]
                            """站点信息"""
                            for T in busstops:
                                cell = []
                                lng1 = T["location"].split(",")[0]
                                lat1 = T["location"].split(",")[1]
                                cell = [city, T["name"], WGS1984.main(lng1, lat1)[0], WGS1984.main(lng1, lat1)[1], T["id"], i["name"],
                                        count]
                                with open(bus_station, 'a', newline='', encoding='utf-8') as f:
                                    write = csv.writer(f)
                                    write.writerow(cell)

                            """线路信息"""
                            information = [city, count, keywords[0:4], i["name"], i["basic_price"], i["total_price"], i["distance"],
                                        i["start_stop"], i["end_stop"], i["type"], i["start_time"], i["end_time"]]
                            with open(buslines_information, 'a', newline='', encoding='utf-8') as f:
                                write = csv.writer(f)
                                write.writerow(information)

                            """线路路线"""
                            polyline = i["polyline"]
                            split_polyline = polyline.split(";")
                            cou = 0
                            buslines_name2 = i["name"]
                            for i in split_polyline:
                                cou = cou + 1
                                excessive = i.split(",")
                                bus_polyline = [city, cou, buslines_name2, keywords[0:4], WGS1984.main(excessive[0], excessive[1])[0],
                                                WGS1984.main(excessive[0], excessive[1])[1]]
                                with open(buslines_polyline, 'a', newline='', encoding='utf-8') as f:
                                    write = csv.writer(f)
                                    write.writerow(bus_polyline)
            

        def research(city, keywords, key, jscode,bus_station, buslines_information, buslines_polyline):
            url = "https://restapi.amap.com/v3/bus/linename?parameters"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}
            keyword = {"s": "rsv3", "extensions": "all", "key": key, 'jscode':jscode , "output": "json", "city": city, "offset": "2",
                    "keywords": keywords, "platform": "JS"}
            a = requests.get(url, headers=headers, params=keyword)
            html = a.text
            data = json.loads(html)

            # 如果buslines返回的值为空值的话，那么对keyword切片
            if data["status"] == "1":
                if data['buslines']:
                    station(data, keywords, bus_station, buslines_information, buslines_polyline, city)
                elif (not data['buslines']) and contains_digit(keywords):
                    keywords = remove_after_last_digit(keywords)
                    station(data, keywords, bus_station, buslines_information, buslines_polyline, city)
                else:
                    print("未查询到{}市的{}信息".format(city, keywords))
            else:
                print("未查询到{}市的{}信息".format(city, keywords))


        path_bus = save_path
        if os.path.isdir(path_bus) == False:
            os.mkdir(path_bus)
        if os.path.isdir(path_bus + province) == False:
            os.mkdir(path_bus + province)

        now_path =path_bus + province + "/csv/"
        if os.path.isdir(now_path) == False:
            os.mkdir(now_path)

        bus_station = now_path + city + "公交站点.csv"
        buslines_information = now_path + city + "公交线路信息.csv"
        buslines_polyline = now_path + city + "公交线路.csv"

        with open(bus_station, 'a', newline='', encoding='utf_8_sig') as f:
            write = csv.writer(f)
            write.writerow(["城市", "站点名称", "lng", "lat", "id", "name", "正反线路"])

        with open(buslines_information, 'a', newline='', encoding='utf_8_sig') as f:
            write = csv.writer(f)
            write.writerow(
                ["城市", "正反线路", "简称", "全称", "上车票价", "全程票价", "距离", "起点站", "终点站", "线路类型",
                "首班时间", "末班时间"])

        with open(buslines_polyline, 'a', newline='', encoding='utf_8_sig') as f:
            write = csv.writer(f)
            write.writerow(["城市", "序号", "全称", "简称", "lng", "lat"])

        if polygon_mult:
            # 使用多边形爬取方法
            citybus_name = buslist.getpoi(api_key = key_fwd,polygon = polygon_mult,keywords = keyword).bus_lines
            print(citybus_name)
        # print(citybus_name)
        if region_xzq:
        # 使用行政区方法
            citybus_name = buslist.getpoi(api_key = key_fwd,cityname = region_xzq,keywords = keyword).bus_lines

        print("【正在获取{}公交线路数据】\n".format(city))

        for i in tqdm(citybus_name):
            keywords = i
            city = city
            research(city, keywords, key, jscode,bus_station, buslines_information, buslines_polyline)
            time.sleep(random.randint(0, 1))



        bustop_csv= pd.read_csv(bus_station)
        df_info_csv = pd.read_csv(buslines_information)
        buslines_csv = pd.read_csv(buslines_polyline)

        # df_info_csv.drop_duplicates('上车票价',keep='first',inplace=True)

        # 点层转换
        def geop(row):
            return Point(row['lng'],row['lat'])
        bustop_csv['geometry'] = bustop_csv.apply(geop,axis=1)
        bustop_csv = gpd.GeoDataFrame(bustop_csv,geometry = 'geometry',crs='4326')

        # 线要素转换
        df_info_csv['geometry']=None
        def poilist(row):
            return (row['lng'],row['lat'])
        
        for line_name in buslines_csv['全称'].unique():
            coords = buslines_csv[buslines_csv['全称']==line_name].apply(poilist,axis=1).to_list()
            line = LineString(coords)
            x = df_info_csv[df_info_csv['全称']==line_name].index[0]
            
            df_info_csv.loc[x,'geometry']=line
        df_info_csv = gpd.GeoDataFrame(df_info_csv,geometry = 'geometry',crs='4326')
        df_info_csv.dropna(inplace=True)


        return bustop_csv , df_info_csv
        # conversion_geo.main(bus_station, buslines_information, buslines_polyline, city, province)

    def re_col(gdf,col=[]):
        gdf.columns = col
        return gdf
    
    def bus_to_shpfile(self,gdf,file_path=None):
        if file_path == None:
            file_path = self.save_path

        gdf = gdf[~gdf.geometry.is_empty]
        for i in gdf.columns:
            if i != 'geometry':
                gdf[i] = gdf[i].astype(str)
        # 保存 GeoDataFrame 为 Shapefile 文件
        gdf.to_file(driver='ESRI Shapefile', filename=file_path,encoding = 'utf-8')


    

    # def save_shp(gdf,save_path=None):
    # # 删除geometry列中为空的行
    