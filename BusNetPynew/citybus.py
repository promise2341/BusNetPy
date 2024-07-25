import requests
import pandas as pd
import json
import re
from bs4 import BeautifulSoup
from pypinyin import lazy_pinyin

def getInitial(cityName,headers):
    url = 'https://{}.8684.cn/list1'.format(cityName)
    headers = {'User-Agent':headers}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    initial = soup.find_all('div',{'class':'tooltip-inner'})[3]
    initial = initial.find_all('a')
    ListInitial = []
    for i in initial:
        ListInitial.append(i.get_text())
    return ListInitial

def getLine(city,cityName,n,headers,citybus_name):
    url = 'https://{}.8684.cn/list{}'.format(cityName,n)
    headers = {'User-Agent':headers}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'lxml')
    busline = soup.find('div',{'class':'list clearfix'})
    busline = busline.find_all('a')
    for i in busline:
        information = {"city":city,"name":i.get_text()}
        citybus_name.append(information)
   
def main(city):
    headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    if type(city) == list:
        citybus_name = []
        for i in city:
            cityName = ""
            for i in lazy_pinyin(city):
                cityName += str(i)  
            ListInitial = getInitial(cityName,headers)
            for n in ListInitial:
                getLine(i,cityName,n,headers,citybus_name)
        return citybus_name
    else:
        cityName = ""
        for i in lazy_pinyin(city):
            cityName += str(i)
        #cityName = lazy_pinyin(city)[0] + lazy_pinyin(city)[1]   
        ListInitial = getInitial(cityName,headers)
        citybus_name = []
        for n in ListInitial:
            getLine(city,cityName,n,headers,citybus_name)
        return citybus_name
    



    
