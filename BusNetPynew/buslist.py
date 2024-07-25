from urllib.parse import quote
import urllib
import pandas as pd
import xlwt
import json
from . import citycode

class getpoi:
    
    poi_search_url_region = 'https://restapi.amap.com/v5/place/text?keywords=%s&region=%s&key=%s&page_size=25&show_fields=children&page_num=%s'
    poi_search_url_polygon = 'https://restapi.amap.com/v5/place/polygon?keywords=%s&polygon=%s&key=%s&page_size=25&show_fields=children&page_num=%s'
    citycodepip = citycode.codes_pip()
    totalcontent = {}
    bus_lines = []
    x=0

    def __init__(self,**kwargs):
        self.api_key = kwargs.get('api_key')
        self.cityname = kwargs.get('cityname','1')
        self.keywords = kwargs.get('keywords','公交')
        # self.search_type = kwargs.get('search_type')
        self.polygon = kwargs.get('polygon','1')
        for page in range(1,101):
            # if self.search_type == '1':
            if len(self.cityname) > 1:
                # print(self.search_citycode())
                bus_data = self.get_poi_code(self.search_citycode(),page)
                bus_data = json.loads(bus_data)
                if bus_data['count'] > '0':
                    self.bus_lines += self.hand(bus_data)
                if bus_data['count'] == '0':
                    # 使用集合去重
                    self.bus_lines = list(set(self.bus_lines))
                    break
                if bus_data['status']=='0':
                    print('！爬取程序存在错误：{},请根据错误代码校正！'.format(bus_data['info']))
                    break
            # if self.search_type == '2':
            if len(self.polygon) > 1:
                
                bus_data = self.get_poi_mutl(page)
                bus_data = json.loads(bus_data)
                if bus_data['count'] > '0':
                    self.bus_lines += self.hand(bus_data)
                if bus_data['count'] == '0':
                    # 使用集合去重
                    self.bus_lines = list(set(self.bus_lines))
                    
                    break
                if bus_data['status']=='0':
                    print('！爬取程序存在错误：{},请根据错误代码校正！'.format(bus_data['info']))
                    break
        # 使用集合去重
        self.bus_lines = list(set(self.bus_lines))
            # else:
            #     print('参数输入有误')
            #     break
            

    # 内容搜索
    def hand(self, poidata):
        pois = poidata['pois']
        poilist = []
        for i in range(len(pois)):
            content = {}
            if ';' in pois[i]['address']:
                mult_json = pois[i]['address']
                mult_json = mult_json.split(';')
                for j in mult_json:
                    poilist.append(j)
                
            else:
                content = pois[i]['address']
                poilist.append(content)
        return poilist

    # 搜索城市编码
    def search_citycode(self):
        qv,city = self.citycodepip
        city_bm = city.loc[self.cityname[0]]['citycode']
        code = qv.loc[self.cityname[1],city_bm]['adcode']
        return code

    
    # 爬取json数据-行政区或市域
    def get_poi_code(self,region, page):
        poiurl = self.poi_search_url_region % (quote(self.keywords),region,self.api_key,page)
        data = ''
        with urllib.request.urlopen(poiurl) as f:
            data = f.read().decode('utf8')
        return data
    

    # 爬取多边形区域
    def get_poi_mutl(self, page):
        poiurl = self.poi_search_url_polygon % (quote(self.keywords),self.polygon,self.api_key,page)
        data = ''
        with urllib.request.urlopen(poiurl) as f:
            data = f.read().decode('utf8')
        return data