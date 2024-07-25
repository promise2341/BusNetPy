import pandas as pd
from . import find_cycle
import geopandas as gpd
from shapely.geometry import LineString,Point
from shapely import wkt
import contextily as ctx
import matplotlib.pyplot as plt
import warnings
import math

# 抑制所有警告
warnings.filterwarnings('ignore')



def wgs_dis(row):
    """
    
    计算两个wgs84坐标点之间的距离

    参数:
    x1, y1: 第一个点的gps坐标
    x2, y2: 第二个点的gps坐标

    返回:
    两个点之间的距离（km）
    """

    R = 6371  # 地球半径（单位：公里）

    lat1, lon1, lat2, lon2 = map(math.radians, [row['lat'], row['lng'], row['lat_y'], row['lng_y']])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c

    return distance



def read_busdata(path_line,path_point,encod_line='utf-8',encod_point='utf-8'):
    """

    读取公交数据

    参数:

    返回：


    """

    df_line = pd.read_csv(path_line,encoding = encod_line)
    df_point = pd.read_csv(path_point,encoding=encod_point)
    # 初始化一个新列来存储索引值
    df_point['line_index'] = None

    return df_line,df_point



def build_index(df_line,df_point):
    """

    提取公交站点在公交线路中索引信息，用于截取站点间线路形状

    参数:
        df_line,df_point = read_busdata中返回的数据

    返回：
        df_point:带线路编号索引的结构化数据

    """

    # 遍历df_line中所有独特的全称值
    for line_name in df_line['全称'].unique():
    
        # 筛选出对应的线路和站点数据
        testline = df_line[df_line['全称'] == line_name]
        testpoint = df_point[df_point['name'] == line_name]

        # 将正反线路去重
        if len(testpoint['正反线路'].unique())>1:
            testpoint = testpoint[testpoint['正反线路']==testpoint['正反线路'].unique()[0]]

        last_index = 0
        
        # 遍历testpoint中的每一行
        for i, point_row in testpoint.iterrows():
            

            # 在testline中寻找同时具有相同lng和lat的行
            matched_line = testline[last_index:][(testline['lng'] == point_row['lng']) & (testline['lat'] == point_row['lat'])]
            
            # 如果找到了匹配的行，获取其索引
            if not matched_line.empty:
                line_index = matched_line.index[0]  # 取第一个匹配项的索引
                # 更新下一次搜索的起始索引位置
                last_index = last_index + 1
                # 将索引值赋值给df_point中对应的行
                df_point.at[i, 'line_index'] = line_index
            else:
                matched_line = testline[0:][(testline['lng'] == point_row['lng']) & (testline['lat'] == point_row['lat'])]
                line_index = matched_line.index[0]  # 取第一个匹配项的索引
                # 更新下一次搜索的起始索引位置
                last_index = 0
                # 将索引值赋值给df_point中对应的行
                df_point.at[i, 'line_index'] = line_index

    df_point = df_point.dropna(subset=['line_index'])
    
    for line_name in df_point['name'].unique():

        test_line = df_point[df_point['name']==line_name]
        station_name = test_line['站点名称'].tolist()
        cycle = find_cycle.find_cycle(station_name)
    
        if (len(test_line) - len(cycle)) > (len(cycle)/2):
            df_point = df_point[~df_point['name'].isin([line_name])]
            df_cycle = test_line.iloc[:len(cycle)]
            df_point = pd.concat([df_point,df_cycle],axis=0)


    return df_point



def line_build(df_point,df_line,epsg=3857):

    """

    构造前后站点衔接数据

    参数:

    返回：


    """

    #对站点线路进行遍历后错位上移一步站点名称形成前后站斜街
    for i in df_point['name'].unique():
        result = df_point[df_point['name']==i]['站点名称'].shift(-1, axis=0)
        result_lng = df_point[df_point['name']==i]['lng'].shift(-1, axis=0)
        result_lat = df_point[df_point['name']==i]['lat'].shift(-1, axis=0)
        result_id = df_point[df_point['name']==i]['id'].shift(-1, axis=0)
        result_index = df_point[df_point['name']==i]['line_index'].shift(-1, axis=0)

        df_point.loc[df_point['name']==i,'next_站点名称'] = result
        df_point.loc[df_point['name']==i,'next_lng'] = result_lng
        df_point.loc[df_point['name']==i,'next_lat'] = result_lat
        df_point.loc[df_point['name']==i,'next_id'] = result_id
        df_point.loc[df_point['name']==i,'next_line_index'] = result_index

    df_point = df_point.dropna()
    # 创建一个新列用于存储LineString
    df_point['geometry'] = None
    

    # 遍历df
    for index, row in df_point.iterrows():
        # 获取当前行的line_index和next_line_index
        line_index = row['line_index']
        next_line_index = row['next_line_index']

        if line_index < next_line_index:
            # 获取line_index到next_line_index之间的所有行的坐标点
            points = df_line.iloc[line_index:next_line_index + 1][['lng', 'lat']]
        else:
            points = df_line.iloc[next_line_index:line_index + 1][['lng', 'lat']]
        
        # 构造LineString对象，我们需要将points DataFrame转换为点的列表
        line = LineString(points.values.tolist())
        
        # 将LineString对象添加到当前行的geometry列
        df_point.at[index, 'geometry'] = line
        
    # 转换为GeoDataFrame
    gdf = gpd.GeoDataFrame(df_point, geometry='geometry', crs="EPSG:4326")
    # 投影转换
    gdf = gdf.to_crs(epsg=epsg)
    

    # 计算geometry长度并填充到hx字段
    gdf['hx'] = gdf.length/1000
    gdf.drop(columns='城市',inplace=True)
    gdf = gdf.rename(columns={'站点名称':'stationname','正反线路':'dir','next_站点名称':'nt_stationname'})
    
    
    return gdf



def ycl_gdf(gdf):

    """

    用于从 LineString 中提取最后一个点的坐标

    参数:

    返回：


    """
    def get_last_coord(geometry):
        if isinstance(geometry, LineString):
            return list(geometry.coords)[-1]  # 返回最后一个坐标元组 (lng, lat)
        else:
            return None

    # 应用这个函数到每个 geometry 上，新建两个列 'lng_end' 和 'lat_end'
    gdf['lng_y'], gdf['lat_y'] = zip(*gdf['geometry'].apply(get_last_coord))
    # 定义一个函数，用于从 LineString 中提取最后一个点的坐标
    def get_first_coord(geometry):
        if isinstance(geometry, LineString):
            return list(geometry.coords)[0]  # 返回最后一个坐标元组 (lng, lat)
        else:
            return None

    # 应用这个函数到每个 geometry 上，新建两个列 'lng_end' 和 'lat_end'
    gdf['lng'], gdf['lat'] = zip(*gdf['geometry'].apply(get_first_coord))
    def calculate_distance(row):
        return math.sqrt(abs(math.pow(row['lng'] - row['lng_y'], 2) + math.pow(row['lat'] - row['lat_y'], 2)))/1000
    

    if gdf.crs.to_epsg() != 4326:
        gdf['zx_dis'] = gdf.apply(calculate_distance, axis=1)
    if gdf.crs.to_epsg() == 4326:
        gdf['zx_dis'] = gdf.apply(wgs_dis, axis=1)
    return gdf



def build_route(line,point,epsg=3857,wgs84=True):
    """

    整合函数构造在节点处打断的公交线网结构化数据

    参数:

    返回：


    """

    df_point = build_index(line,point)
    gdf = line_build(df_point,line,epsg=epsg)
    gdf = ycl_gdf(gdf)
    if wgs84:
        gdf = gdf.to_crs(epsg=4326)
        gdf = ycl_gdf(gdf)
    return gdf



def show_bus(gdf):
    # 可视化
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, column='hx', legend=True)
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    plt.show()



def save_shp(gdf,save_path=None):
    # 删除geometry列中为空的行
    gdf = gdf[~gdf.geometry.is_empty]
    for i in gdf.columns:
        if i != 'geometry':
            gdf[i] = gdf[i].astype(str)
    # 保存 GeoDataFrame 为 Shapefile 文件
    gdf.to_file(driver='ESRI Shapefile', filename=save_path,encoding = 'utf-8')
    


def save_point(point,save_path=None,epsg=4326):
    # 创建几何列
    geometry = [Point(xy) for xy in zip(point['lng'], point['lat'])]
    point_gdf = gpd.GeoDataFrame(point, geometry=geometry, crs="EPSG:4326")
    # 投影转换
    point_gdf = point_gdf.to_crs(epsg=epsg)
    point_gdf = point_gdf.rename(columns={'站点名称':'stationname','正反线路':'dir','城市':'city'})

    # 转换字段类型
    point_gdf['line_index'] = point_gdf['line_index'].astype(str)
    point_gdf['dir'] = point_gdf['dir'].astype(int)
    point_gdf['lng'] = point_gdf['lng'].astype(float)
    point_gdf['lat'] = point_gdf['lat'].astype(float)
    point_gdf['city'] = point_gdf['city'].astype(str)
    point_gdf['stationname'] = point_gdf['stationname'].astype(str)
    point_gdf['id'] = point_gdf['id'].astype(str)
    point_gdf['name'] = point_gdf['name'].astype(str)

    # 保存 GeoDataFrame 为 Shapefile 文件
    point_gdf.to_file(driver='ESRI Shapefile', filename=save_path, encoding='utf-8')





