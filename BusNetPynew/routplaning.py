import geopandas as gpd
from shapely import *
import networkx as nx
import pandas as pd




# gP部分
def GP_planning(G_P,node1,node2):

    # spaceP部分
    def custom_weight(G_P, u, v, attr):
        """计算边的权重，考虑节点切换损失"""
        edge_weight = G_P[u][v].get(attr, 1)  # 获取边的权重
        u_name = G_P.nodes[u].get('staname')
        v_name = G_P.nodes[v].get('staname')
        switch_penalty = 3 if u_name != v_name else 0  # 节点切换损失
        return edge_weight + switch_penalty

    def custom_shortest_path(G_P, source, target, weight='length'):
        """使用自定义权重函数计算最短路径"""
        def weight_function(u, v, d):
            return custom_weight(G_P, u, v, weight)
        
        return nx.shortest_path(G_P, source, target, weight=weight_function)


    try:
        nodes = custom_shortest_path(G_P,source=node1, target=node2,weight='length')
        # print("最短路径上的节点列表:", nodes)
    except nx.NetworkXNoPath:
        print(f"从节点 {node1} 到节点 {node2} 没有路径。")
    return nodes



# 返回经过的上下车及换成站点
def route_sta_analy(G_P,nodes):

    staname_list = []
    # 获取每个节点的属性
    node_attributes = {node: G_P.nodes[node] for node in nodes}
    for node, attributes in node_attributes.items():
        
        for attribute, value in attributes.items():
            if attribute=='staname':
                staname_list.append(value)
    return staname_list



# 获取历经的线路名称信息
def route_linena_analy(G_P,nodes):
    linename_list=[]
    # 遍历最短路径上的边
    for i in range(len(nodes) - 1):
        start_node = nodes[i]
        end_node = nodes[i+1]
        
        # 获取两个节点之间边的属性
        edge_attributes = G_P.edges[start_node, end_node]
        
        # # 打印节点以及边的属性
        # print(f'Edge from {start_node} to {end_node}:')
        for attribute, value in edge_attributes.items():
            if attribute == 'line_name':
                linename_list.append(value)
    return linename_list

#取出需求线路
def filtered_edges(G_L,linename_list):
    # 构建一个新的图，只包含特定name属性的边
    G_filtered = nx.Graph()
    # # 检查'bus_line'是否包含特定的公交线路名称
    # selected_edges = [(u, v, data) for u, v, data in G_L.edges(data=True) if data.get('linename') in linename_list]
    # G_filtered.add_edges_from(selected_edges)

    for u, v, data in G_L.edges(data=True):
        # 如果没有'bus_line'键，或者值为None，使用空字符串
        bus_line = data.get('bus_lines', '')
        
        # 检查'bus_line'是否包含特定的公交线路名称
        for linenamebl in bus_line:
            if linenamebl in linename_list:
                G_filtered.add_edge(u, v, **data)
    return G_filtered


# 获取最终路径
def busroute_result(G_filtered,node1,node2,gdf,linename_list):
    # 使用新的G来进行路径规划
    shortest_path_nodes = nx.shortest_path(G_filtered, source=node1, target=node2)
    length = nx.shortest_path_length(G_filtered, source=node1, target=node2,weight='length')
    # segment_test=pd.DataFrame()
    segments = []
    for i in range(len(shortest_path_nodes) - 1):
        shortest_path_nodes_l = nx.shortest_path(G_filtered,source=shortest_path_nodes[i],target=shortest_path_nodes[i+1])
        # print(shortest_path_nodes_l)
        for j in range(len(shortest_path_nodes_l) - 1):
            start_node = shortest_path_nodes_l[j]
            end_node = shortest_path_nodes_l[j+1]
            
            # 假设gdf中有起点和终点标识符列为'start_node'和'end_node'
           
            segment = gdf[(gdf['name'].isin(linename_list))&(gdf['id'] == start_node) & (gdf['next_id'] == end_node)]
            if not segment.empty:
                segments.append(segment.iloc[:1])
            else:
                
                segment = gdf[(gdf['next_id'] == start_node) & (gdf['id'] == end_node)]
                # segment_test = pd.concat([segment_test,segment],axis=0)
                segments.append(segment.iloc[:1])

     # 将所有相关路段合并为一个GeoDataFrame
    path_gdf = gpd.GeoDataFrame(pd.concat(segments, ignore_index=True))
    path_gdf = path_gdf[['stationname','nt_stationname','geometry',]]
    return path_gdf,length



def bus_route_planning(G_P,G_L,node1,node2,gdf):
    nodes = GP_planning(G_P,node1,node2)
    staname_list = route_sta_analy(G_P,nodes)
    linename_list = route_linena_analy(G_P,nodes)
    G_filtered = filtered_edges(G_L,linename_list)
    path_gdf,length = busroute_result(G_filtered,node1,node2,gdf,linename_list)
    return staname_list , path_gdf,length
