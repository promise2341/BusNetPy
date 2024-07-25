import pandas as pd
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
from shapely.geometry import *
import math
import pyproj




def Nonline(gdf,base_path=None,hx_path=None):

    if gdf.crs.to_epsg() != 4326:
        if 'zx_dis' not in gdf.columns:
            # 定义一个函数，用于从 LineString 中提取最后一个点的坐标
            def ycl_gdf(gdf):
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

                gdf['zx_dis'] = gdf.apply(calculate_distance, axis=1)
                return gdf
            gdf=ycl_gdf(gdf)

        '非直线系数'
        sum_line = gdf.groupby('name')[['hx']].sum().reset_index()
        # 添加route_zx_dis计算每条线路的起终点距离
        sum_line['route_zx_dis'] = None
        for index ,row in sum_line.iterrows():
            if gdf[gdf['name']==row['name']].iloc[0]['id'] == gdf[gdf['name']==row['name']].iloc[0]['next_id']:
                sum_line.at[index,'route_zx_dis'] = 0
            else:
                sum_line.at[index,'route_zx_dis'] = math.sqrt(math.pow(gdf[gdf['name']==row['name']].iloc[0]['lng']-gdf[gdf['name']==row['name']].iloc[-1]['lng_y'],2) + 
                    math.pow(gdf[gdf['name']==row['name']].iloc[0]['lat']-gdf[gdf['name']==row['name']].iloc[-1]['lat_y'],2))/1000
        # 通过距离识别环线，规则是如果起点站点和终点站点的间距小于100m，那么就填充0
        sum_line['fzxxs_base'] = sum_line.apply(lambda row: row['hx'] / row['route_zx_dis'] if row['route_zx_dis'] > 1 else 0, axis=1)
        # 识别出环线
        fzxxs_hx = sum_line[sum_line['fzxxs_base']==0]
        def hx_fzx(row):
            cs = gdf[gdf['name']==row['name']].groupby('name')['hx'].sum()/gdf[gdf['name']==row['name']].groupby('name')['zx_dis'].sum()
            return cs[0]

        fzxxs_hx['fzxxs_hx'] = fzxxs_hx.apply(hx_fzx,axis=1)
        # 根据规范：《城市道路交通规划设计规范GB50220-95》规定：公共交通线路非直线系数不应大于1.4，整个线网的平均非直线系数为1.15～1.2为宜
        result_fzxxs_base = sum_line[sum_line['fzxxs_base']!=0]['fzxxs_base'].mean()
        result_fzxxs_hx = fzxxs_hx['fzxxs_hx'].mean()
        base_line = sum_line[sum_line['fzxxs_base']!=0]
        base_line.to_csv(base_path,encoding='utf-8')
        fzxxs_hx.to_csv(hx_path,encoding='utf-8')

    elif gdf.crs.to_epsg() == 4326:
        gdf = gdf.to_crs(epsg=3857)

        # 定义一个函数，用于从 LineString 中提取最后一个点的坐标
        def ycl_gdf(gdf):
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

            gdf['zx_dis'] = gdf.apply(calculate_distance, axis=1)
            return gdf
        
        gdf=ycl_gdf(gdf)

        '非直线系数'
        sum_line = gdf.groupby('name')[['hx']].sum().reset_index()
        # 添加route_zx_dis计算每条线路的起终点距离
        sum_line['route_zx_dis'] = None
        for index ,row in sum_line.iterrows():
            if gdf[gdf['name']==row['name']].iloc[0]['id'] == gdf[gdf['name']==row['name']].iloc[0]['next_id']:
                sum_line.at[index,'route_zx_dis'] = 0
            else:
                sum_line.at[index,'route_zx_dis'] = math.sqrt(math.pow(gdf[gdf['name']==row['name']].iloc[0]['lng']-gdf[gdf['name']==row['name']].iloc[-1]['lng_y'],2) + 
                    math.pow(gdf[gdf['name']==row['name']].iloc[0]['lat']-gdf[gdf['name']==row['name']].iloc[-1]['lat_y'],2))/1000
        # 通过距离识别环线，规则是如果起点站点和终点站点的间距小于100m，那么就填充0
        sum_line['fzxxs_base'] = sum_line.apply(lambda row: row['hx'] / row['route_zx_dis'] if row['route_zx_dis'] > 1 else 0, axis=1)
        # 识别出环线
        fzxxs_hx = sum_line[sum_line['fzxxs_base']==0]
        def hx_fzx(row):
            cs = gdf[gdf['name']==row['name']].groupby('name')['hx'].sum()/gdf[gdf['name']==row['name']].groupby('name')['zx_dis'].sum()
            return cs[0]

        fzxxs_hx['fzxxs_hx'] = fzxxs_hx.apply(hx_fzx,axis=1)
        # 根据规范：《城市道路交通规划设计规范GB50220-95》规定：公共交通线路非直线系数不应大于1.4，整个线网的平均非直线系数为1.15～1.2为宜
        result_fzxxs_base = sum_line[sum_line['fzxxs_base']!=0]['fzxxs_base'].mean()
        result_fzxxs_hx = fzxxs_hx['fzxxs_hx'].mean()
        base_line = sum_line[sum_line['fzxxs_base']!=0]
        base_line.to_csv(base_path,encoding='utf-8')
        fzxxs_hx.to_csv(hx_path,encoding='utf-8')

    # base_line:非环线数据
    # fzxxs_hx：环线数据
    # result_fzxxs_base：全部数据结果
    # result_fzxxs_hx： 环线数据结果
    return base_line,fzxxs_hx,result_fzxxs_base,result_fzxxs_hx



def avg_station(gdf,file_path=None):
    '平均站间距'
    if gdf.crs.to_epsg() != 4326:
        if 'zx_dis' not in gdf.columns:
            def ycl_gdf(gdf):
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

                gdf['zx_dis'] = gdf.apply(calculate_distance, axis=1)
                return gdf
            gdf=ycl_gdf(gdf)


        avg_sta= gdf.groupby('name')['hx'].mean().reset_index().sort_values('hx')
        avg_sta.to_csv(file_path,encoding = 'utf-8')

    if gdf.crs.to_epsg() == 4326:
        gdf = gdf.to_crs(3857)
        
        def ycl_gdf(gdf):
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

            gdf['zx_dis'] = gdf.apply(calculate_distance, axis=1)
            return gdf
        gdf=ycl_gdf(gdf)


        avg_sta= gdf.groupby('name')['hx'].mean().reset_index().sort_values('hx')
        avg_sta.to_csv(file_path,encoding = 'utf-8')
    return avg_sta


# 获取带号
def get_utm_epsg(longitude, latitude):

    # 确定半球和带号
    def get_utm_zone_and_hemisphere(longitude, latitude):
        # 确定带号
        zone_number = int((longitude + 180) / 6) + 1
        
        # 确定半球
        hemisphere = 'N' if latitude >= 0 else 'S'
        
        return zone_number, hemisphere

    zone_number, hemisphere = get_utm_zone_and_hemisphere(longitude, latitude)
    
    # 确定EPSG代码
    if hemisphere == 'N':
        epsg_code = f"326{zone_number:02d}"  # 北半球
    else:
        epsg_code = f"327{zone_number:02d}"  # 南半球
    print(f'带号为:{zone_number}')
    return epsg_code



# 构造网络
def spaceL(gdf):
    # 创建一个无向图
    G_L = nx.Graph()
    
    # 添加节点
    pos = {}  # 初始化位置字典
    for point, row in gdf.iterrows():
        # 如果节点已经存在，追加线路名称
        if G_L.has_node(row['id']):
            G_L.nodes[row['id']]['bus_lines'].append(row['name'])
        else:
            G_L.add_node(row['id'], pos=(row['lng'], row['lat']), staname=row['stationname'], bus_lines=[row['name']])
        pos[row['id']] = (row['lng'], row['lat'])

    # 添加边
    for point, row in gdf.iterrows():
        # 如果节点不存在，则添加节点
        if not G_L.has_node(row['next_id']):
            G_L.add_node(row['next_id'], pos=(row['lng_y'], row['lat_y']), staname=row['nt_stationname'], bus_lines=[row['name']])
        else:
            # 如果节点已经存在，但是新的线路名称不在列表中，则追加
            if row['name'] not in G_L.nodes[row['next_id']]['bus_lines']:
                G_L.nodes[row['next_id']]['bus_lines'].append(row['name'])
        pos[row['next_id']] = (row['lng_y'], row['lat_y'])

        # 添加边，如果边已存在，则追加线路名称
        if G_L.has_edge(row['id'], row['next_id']):
            if row['name'] not in G_L[row['id']][row['next_id']]['bus_lines']:
                G_L[row['id']][row['next_id']]['bus_lines'].append(row['name'])
        else:
            G_L.add_edges_from([(row['id'], row['next_id'])], length=row['hx'], bus_lines=[row['name']])
    return G_L,pos


def G_ksh(G_L,pos):
    # 绘制网络图
    plt.figure(figsize=(10, 8))
    nx.draw(G_L, pos, node_size=0.1, node_color='blue', with_labels=False)
    
    plt.show()


# 做大共线边
def unique_line(G_L):
    # 检查共线最多的站点
    # 初始化变量用于存储最多线路的边信息
    max_bus_lines = 0
    edge_with_max_bus_lines = None

    # 遍历图中的所有边
    for edge in G_L.edges(data=True):
        # 获取当前边的bus_lines属性
        current_bus_lines = edge[2].get('bus_lines', [])
        # 检查当前边的bus_lines列表长度
        if len(current_bus_lines) > max_bus_lines:
            # 更新最多线路的边信息
            max_bus_lines = len(current_bus_lines)
            edge_with_max_bus_lines = edge


    # 为了剔除正反线路影响，提取‘(’前面的数据
    result_line = [item.split('(')[0] for item in edge_with_max_bus_lines[2]['bus_lines']]
    # 对列表去重然后计算长度
    unique_list_line = list(set(result_line))
    max_lines_count_line = len(unique_list_line)

    # G_L.nodes[node_with_max_sta]['staname']
    # 打印结果
    if edge_with_max_bus_lines:
        print(f"含有公交线路最多的站点区间是: {G_L.nodes[edge_with_max_bus_lines[0]]['staname']}-{G_L.nodes[edge_with_max_bus_lines[1]]['staname']},{edge_with_max_bus_lines[0]} - {edge_with_max_bus_lines[1]}")
        print(f"含有线路条数: {max_lines_count_line}")
        print(f"Bus lines: {unique_list_line}")
    else:
        print("没有边")
    return unique_list_line


# 最多线路的站点
def most_linesta(G_L):
    # 初始化变量以追踪含有线路最多的站点信息
    max_lines_count = 0
    node_with_max_sta = None

    # 遍历图中的所有节点及其属性
    for node, attrs in G_L.nodes(data=True):
        # 获取当前节点的 'bus_lines' 属性值
        bus_lines = attrs.get('bus_lines', [])
        # 检查当前节点的线路数量是否是最多的
        if len(bus_lines) > max_lines_count:
            max_lines_count = len(bus_lines)
            node_with_max_sta = node

    # 为了剔除正反线路影响，提取‘(’前面的数据
    result_sta = [item.split('(')[0] for item in G_L.nodes[node_with_max_sta]['bus_lines']]
    # 对列表去重然后计算长度
    unique_list = list(set(result_sta))
    max_lines_count = len(unique_list)


    # 打印结果
    if node_with_max_sta:
        # print(f"含有最多公交线路的站点: {node_with_max_sta}")
        print(f"含有线路数量: {max_lines_count}")
        print(f"站点名称为：{G_L.nodes[node_with_max_sta]['staname']}")
    else:
        print("没有节点.")



# 计算重复系数 实际运行距离/线路总长度
def cf_all(G_L,gdf):
    # 初始化长度总和
    total_length = 0

    # 遍历图中的所有边，获取每条边的length属性，并加到总和中
    for u, v, data in G_L.edges(data=True):
        edge_length = data.get('length', 0)  # 如果某条边没有length属性，默认为0
        total_length += edge_length
    cfxs =  gdf['hx'].sum()/total_length
    return cfxs



# 构造space_P
def spacep(df_point,gdf):

    id_df = df_point[['lng','lat','id','站点名称']]

    # 创建一个无向图
    G_p = nx.Graph()


    for index , row in id_df.iterrows():
        G_p.add_node(row['id'], pos=(row['lng'], row['lat']),staname = row['站点名称'])

    print('完成spaceP公交站点标定')
    # 遍历每个不同的线路名称
    for name in gdf['name'].unique():
        # 获取这条线路的所有站点
        route = gdf[gdf['name'] == name]

        # edges_p = [(a, b) for a in route['id'] for b in route['next_id'] if a != b]
        result = {}
        for index , row in route.iterrows():
            id = row['id']

            for index_nt , row_nt in route.iterrows():
                
                if index_nt >= index:
                    id_nt = row_nt['next_id']
                    length = route.loc[index:index_nt]['hx'].sum()

                    result.update({(id,id_nt):length})

            
        for (u,v),length in result.items():
            G_p.add_edge(u,v,length=length,line_name = name)

        # G_p.add_edges_from(edges_p,line_name=name)


    print('完成spaceP公交网络标定')
    return G_p


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


def route_to_84(gdf):
    """
    非84坐标gdf转为84

    参数:
    gdf:结构化后的gdf

    返回:
    gdf:结构化的84坐标gdf
    """
    gdf = gdf.to_crs(epsg=4326)
    gdf = ycl_gdf(gdf)
    return gdf




def find_nearest_node(G,longitude, latitude):
    """
    寻找最近的节点

    参数:
    lon: 第一个点的UTM坐标
    lat: 第二个点的UTM坐标

    返回:
    节点和距离
    """
    # 确定半球和带号
    def get_utm_zone_and_hemisphere(longitude, latitude):
        # 确定带号
        zone_number = int((longitude + 180) / 6) + 1
        
        # 确定半球
        hemisphere = 'N' if latitude >= 0 else 'S'
        
        return zone_number, hemisphere

    # 获取带号
    def get_utm_epsg(longitude, latitude):
        zone_number, hemisphere = get_utm_zone_and_hemisphere(longitude, latitude)
        
        # 确定EPSG代码
        if hemisphere == 'N':
            epsg_code = f"326{zone_number:02d}"  # 北半球
        else:
            epsg_code = f"327{zone_number:02d}"  # 南半球
        print(f'带号为:{zone_number}')
        return epsg_code


    # 经纬度转utm
    def latlon_to_utm(longitude, latitude):
        epsg_code = get_utm_epsg(longitude, latitude)
        transformer = pyproj.Transformer.from_crs("epsg:4326", f"epsg:{epsg_code}")
        utm_y, utm_x = transformer.transform(latitude, longitude)
        return epsg_code, utm_x, utm_y

    # utm转经纬度
    def utm_to_latlon(utm_x, utm_y, epsg_code):
        transformer = pyproj.Transformer.from_crs(f"epsg:{epsg_code}", "epsg:4326")
        latitude, longitude = transformer.transform(utm_y, utm_x)
        return latitude, longitude


    def utm_distance(x1, y1, x2, y2):
        """
        计算两个UTM坐标点之间的距离

        参数:
        x1, y1: 第一个点的UTM坐标
        x2, y2: 第二个点的UTM坐标

        返回:
        两个点之间的距离（米）
        """
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance



    def haversine_distance(lat1, lon1, lat2, lon2):
        """
        计算两个UTM坐标点之间的距离

        参数:
        x1, y1: 第一个点的gps坐标
        x2, y2: 第二个点的gps坐标

        返回:
        两个点之间的距离km
        """

        R = 6371  # 地球半径（单位：公里）

        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        return distance

    nearest_node = None
    min_distance = float('inf')
    # _, longitude ,latitude = latlon_to_utm(longitude, latitude)

    for node, data in G.nodes(data=True):
        node_lat = data['pos'][1]
        node_lon = data['pos'][0]
        distance = haversine_distance(latitude, longitude, node_lat, node_lon)
        # distance = utm_distance(longitude,latitude, node_lon, node_lat)
        node_id = node
        
        if distance < min_distance:
            min_distance = distance
            nearest_sta = data['staname']+'站'
            node_t = node_id

    return node_t , nearest_sta, min_distance



# 公交路径规划算法


