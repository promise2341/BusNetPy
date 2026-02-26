"""BusNetPy 核心功能单元测试。"""

import math
import unittest

import geopandas as gpd
import networkx as nx
import pandas as pd
from shapely.geometry import LineString, Point

from BusNetPynew import WGS1984, find_cycle, utils
from BusNetPynew.metrical import (
    spaceL,
    cf_all,
    find_nearest_node,
    most_linesta,
    unique_line,
    Nonline,
    avg_station,
)
from BusNetPynew.routplaning import (
    GP_planning,
    route_sta_analy,
    route_linena_analy,
    filtered_edges,
)


class TestWGS1984(unittest.TestCase):
    """坐标转换模块测试。"""

    def test_gcj02towgs84_tiananmen(self):
        """天安门坐标转换验证。"""
        result = WGS1984.gcj02towgs84(116.397428, 39.90923)
        self.assertAlmostEqual(result[0], 116.391184, places=3)
        self.assertAlmostEqual(result[1], 39.907826, places=3)

    def test_wgs84togcj02_roundtrip(self):
        """WGS-84 → GCJ-02 → WGS-84 往返转换精度。"""
        original = [116.391184, 39.907826]
        gcj = WGS1984.wgs84togcj02(original[0], original[1])
        wgs = WGS1984.gcj02towgs84(gcj[0], gcj[1])
        self.assertAlmostEqual(wgs[0], original[0], places=4)
        self.assertAlmostEqual(wgs[1], original[1], places=4)

    def test_out_of_china(self):
        """境外坐标不做偏移。"""
        self.assertTrue(WGS1984.out_of_china(0, 0))
        self.assertFalse(WGS1984.out_of_china(116.4, 39.9))

    def test_main_accepts_strings(self):
        """main() 支持字符串输入。"""
        result = WGS1984.main("116.397428", "39.90923")
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], float)

    def test_foreign_coords_unchanged(self):
        """境外坐标转换不改变值。"""
        result = WGS1984.gcj02towgs84(0.0, 0.0)
        self.assertEqual(result, [0.0, 0.0])


class TestFindCycle(unittest.TestCase):
    """环线检测模块测试。"""

    def test_simple_cycle(self):
        """简单重复模式检测。"""
        result = find_cycle.find_cycle(["A", "B", "C", "A", "B", "C"])
        self.assertEqual(result, ["A", "B", "C"])

    def test_no_cycle(self):
        """无重复模式返回原序列。"""
        result = find_cycle.find_cycle(["A", "B", "C", "D"])
        self.assertEqual(result, ["A", "B", "C", "D"])

    def test_triple_repeat(self):
        """三次重复检测。"""
        result = find_cycle.find_cycle([1, 2, 1, 2, 1, 2])
        self.assertEqual(result, [1, 2])

    def test_single_element_cycle(self):
        """全相同元素。"""
        result = find_cycle.find_cycle(["A", "A", "A", "A"])
        self.assertEqual(result, ["A"])

    def test_empty_sequence(self):
        """空序列。"""
        result = find_cycle.find_cycle([])
        self.assertEqual(result, [])


class TestUtils(unittest.TestCase):
    """公共工具函数测试。"""

    def test_get_first_coord(self):
        """提取第一个坐标点。"""
        line = LineString([(0, 0), (1, 1), (2, 2)])
        result = utils.get_first_coord(line)
        self.assertEqual(result, (0.0, 0.0))

    def test_get_last_coord(self):
        """提取最后一个坐标点。"""
        line = LineString([(0, 0), (1, 1), (2, 2)])
        result = utils.get_last_coord(line)
        self.assertEqual(result, (2.0, 2.0))

    def test_non_linestring_returns_none(self):
        """非 LineString 返回 None。"""
        self.assertIsNone(utils.get_first_coord(Point(0, 0)))
        self.assertIsNone(utils.get_last_coord(Point(0, 0)))

    def test_euclidean_distance_km(self):
        """投影坐标欧氏距离。"""
        dist = utils.euclidean_distance_km(0, 0, 3000, 4000)
        self.assertAlmostEqual(dist, 5.0)

    def test_haversine_distance(self):
        """Haversine 距离 - 北京到上海。"""
        dist = utils.haversine_distance(39.9, 116.4, 31.2, 121.5)
        self.assertAlmostEqual(dist, 1071.3, places=0)

    def test_get_utm_zone_beijing(self):
        """北京 UTM 带号。"""
        zone, hemisphere = utils.get_utm_zone(116.4, 39.9)
        self.assertEqual(zone, 50)
        self.assertEqual(hemisphere, 'N')

    def test_get_utm_epsg_beijing(self):
        """北京 UTM EPSG 代码。"""
        epsg = utils.get_utm_epsg(116.4, 39.9)
        self.assertEqual(epsg, '32650')

    def test_get_utm_epsg_southern(self):
        """南半球 UTM EPSG 代码。"""
        epsg = utils.get_utm_epsg(151.2, -33.9)
        self.assertEqual(epsg, '32756')

    def test_extract_endpoint_coords(self):
        """从 GeoDataFrame 提取起止点坐标。"""
        gdf = gpd.GeoDataFrame(
            geometry=[LineString([(0, 0), (1, 1)])],
            crs="EPSG:4326",
        )
        result = utils.extract_endpoint_coords(gdf)
        self.assertIn('lng', result.columns)
        self.assertIn('lat', result.columns)
        self.assertIn('lng_y', result.columns)
        self.assertIn('lat_y', result.columns)
        self.assertIn('zx_dis', result.columns)


class TestSpaceL(unittest.TestCase):
    """Space-L 网络构建测试。"""

    @classmethod
    def setUpClass(cls):
        """构建测试用公交线网数据。"""
        data = [
            {
                "stationname": "A站", "id": "s1", "name": "1路(上行)",
                "lng": 116.40, "lat": 39.90, "dir": 1, "hx": 1.2,
                "next_id": "s2", "nt_stationname": "B站",
                "lng_y": 116.41, "lat_y": 39.91,
            },
            {
                "stationname": "B站", "id": "s2", "name": "1路(上行)",
                "lng": 116.41, "lat": 39.91, "dir": 1, "hx": 0.8,
                "next_id": "s3", "nt_stationname": "C站",
                "lng_y": 116.42, "lat_y": 39.92,
            },
            {
                "stationname": "A站", "id": "s1", "name": "2路(上行)",
                "lng": 116.40, "lat": 39.90, "dir": 1, "hx": 2.0,
                "next_id": "s4", "nt_stationname": "D站",
                "lng_y": 116.405, "lat_y": 39.895,
            },
        ]
        cls.gdf = gpd.GeoDataFrame(data)
        cls.gdf['geometry'] = cls.gdf.apply(
            lambda r: LineString([(r['lng'], r['lat']), (r['lng_y'], r['lat_y'])]),
            axis=1,
        )
        cls.gdf = cls.gdf.set_geometry('geometry')
        cls.gdf.crs = "EPSG:4326"
        cls.G_L, cls.pos = spaceL(cls.gdf)

    def test_node_count(self):
        """节点数量。"""
        self.assertEqual(self.G_L.number_of_nodes(), 4)

    def test_edge_count(self):
        """边数量。"""
        self.assertEqual(self.G_L.number_of_edges(), 3)

    def test_shared_node_lines(self):
        """共享节点包含多条线路。"""
        lines = self.G_L.nodes['s1']['bus_lines']
        self.assertIn('1路(上行)', lines)
        self.assertIn('2路(上行)', lines)

    def test_edge_has_length(self):
        """边具有长度属性。"""
        for u, v, data in self.G_L.edges(data=True):
            self.assertIn('length', data)
            self.assertGreater(data['length'], 0)

    def test_cf_all(self):
        """重复系数计算。"""
        cf = cf_all(self.G_L, self.gdf)
        self.assertGreater(cf, 0)

    def test_find_nearest_node(self):
        """最近节点查找（位置参数）。"""
        node_id, name, dist = find_nearest_node(self.G_L, 116.41, 39.91)
        self.assertEqual(node_id, 's2')
        self.assertIn('站', name)
        self.assertGreaterEqual(dist, 0)

    def test_find_nearest_node_kwargs(self):
        """最近节点查找（lng/lat 关键字参数）。"""
        node_id, name, dist = find_nearest_node(self.G_L, lng=116.41, lat=39.91)
        self.assertEqual(node_id, 's2')
        self.assertIn('站', name)

    def test_unique_line(self):
        """最大共线边。"""
        result = unique_line(self.G_L)
        self.assertIsInstance(result, list)

    def test_most_linesta(self):
        """经过线路最多的站点。"""
        result = most_linesta(self.G_L)
        self.assertEqual(result, 'A站')


class TestSpaceP(unittest.TestCase):
    """Space-P 网络和路径规划测试。"""

    @classmethod
    def setUpClass(cls):
        """构建 Space-P 网络。"""
        cls.G_P = nx.Graph()
        cls.G_P.add_node("s1", pos=(116.40, 39.90), staname="A站")
        cls.G_P.add_node("s2", pos=(116.41, 39.91), staname="B站")
        cls.G_P.add_node("s3", pos=(116.42, 39.92), staname="C站")
        cls.G_P.add_edge("s1", "s2", length=1.2, line_name="1路")
        cls.G_P.add_edge("s2", "s3", length=0.8, line_name="1路")
        cls.G_P.add_edge("s1", "s3", length=2.0, line_name="1路")

        cls.G_L = nx.Graph()
        cls.G_L.add_node("s1", pos=(116.40, 39.90), staname="A站", bus_lines=["1路"])
        cls.G_L.add_node("s2", pos=(116.41, 39.91), staname="B站", bus_lines=["1路"])
        cls.G_L.add_node("s3", pos=(116.42, 39.92), staname="C站", bus_lines=["1路"])
        cls.G_L.add_edge("s1", "s2", length=1.2, bus_lines=["1路"])
        cls.G_L.add_edge("s2", "s3", length=0.8, bus_lines=["1路"])

    def test_gp_planning(self):
        """Space-P 路径规划。"""
        nodes = GP_planning(self.G_P, "s1", "s3")
        self.assertIn("s1", nodes)
        self.assertIn("s3", nodes)

    def test_route_sta_analy(self):
        """提取路径站点名称。"""
        nodes = ["s1", "s2", "s3"]
        stations = route_sta_analy(self.G_P, nodes)
        self.assertEqual(stations, ["A站", "B站", "C站"])

    def test_route_linena_analy(self):
        """提取路径线路名称。"""
        nodes = ["s1", "s2", "s3"]
        lines = route_linena_analy(self.G_P, nodes)
        self.assertEqual(len(lines), 2)

    def test_filtered_edges(self):
        """筛选指定线路子图。"""
        G_filtered = filtered_edges(self.G_L, ["1路"])
        self.assertEqual(G_filtered.number_of_edges(), 2)

    def test_no_path_raises(self):
        """无路径抛出异常。"""
        G = nx.Graph()
        G.add_node("a", pos=(0, 0), staname="X")
        G.add_node("b", pos=(1, 1), staname="Y")
        with self.assertRaises(nx.NetworkXNoPath):
            GP_planning(G, "a", "b")


class TestNonlineLoopDetection(unittest.TestCase):
    """环线判断测试 —— 验证 CRS 转换后坐标重提取的正确性。"""

    @classmethod
    def setUpClass(cls):
        """构建含明确非环线的 WGS84 测试数据（模拟 build_route 输出）。"""
        from BusNetPynew.busbuild import ycl_gdf

        data = [
            {"stationname": "A站", "id": "s1", "name": "1路(上行)", "dir": 1, "hx": 1.5,
             "next_id": "s2", "nt_stationname": "B站"},
            {"stationname": "B站", "id": "s2", "name": "1路(上行)", "dir": 1, "hx": 2.0,
             "next_id": "s3", "nt_stationname": "C站"},
            {"stationname": "C站", "id": "s3", "name": "1路(上行)", "dir": 1, "hx": 1.8,
             "next_id": "s4", "nt_stationname": "D站"},
        ]
        gdf = gpd.GeoDataFrame(data)
        gdf['geometry'] = [
            LineString([(112.98, 28.20), (112.97, 28.19)]),
            LineString([(112.97, 28.19), (112.95, 28.18)]),
            LineString([(112.95, 28.18), (112.93, 28.17)]),
        ]
        gdf = gdf.set_geometry('geometry')
        gdf.crs = "EPSG:4326"
        cls.gdf_wgs84 = ycl_gdf(gdf)

    def test_nonloop_route_not_classified_as_loop(self):
        """非环线路（起终点相距约 6km）不应被判为环线。"""
        base_line, fzxxs_hx, _, _ = Nonline(self.gdf_wgs84)
        self.assertEqual(len(base_line), 1, "应有 1 条非环线")
        self.assertEqual(len(fzxxs_hx), 0, "不应有环线")

    def test_nonline_coefficient_reasonable(self):
        """非直线系数应为正数（合理范围）。"""
        base_line, _, result_fzxxs_base, _ = Nonline(self.gdf_wgs84)
        self.assertGreater(result_fzxxs_base, 0)

    def test_loop_route_detected(self):
        """起终点相同的环线应被正确识别。"""
        from BusNetPynew.busbuild import ycl_gdf

        data = [
            {"stationname": "A站", "id": "s1", "name": "环线1路", "dir": 1, "hx": 2.0,
             "next_id": "s2", "nt_stationname": "B站"},
            {"stationname": "B站", "id": "s2", "name": "环线1路", "dir": 1, "hx": 2.0,
             "next_id": "s3", "nt_stationname": "C站"},
            {"stationname": "C站", "id": "s3", "name": "环线1路", "dir": 1, "hx": 2.0,
             "next_id": "s1", "nt_stationname": "A站"},
        ]
        gdf = gpd.GeoDataFrame(data)
        gdf['geometry'] = [
            LineString([(112.98, 28.20), (112.99, 28.21)]),
            LineString([(112.99, 28.21), (112.97, 28.21)]),
            LineString([(112.97, 28.21), (112.98, 28.20)]),
        ]
        gdf = gdf.set_geometry('geometry')
        gdf.crs = "EPSG:4326"
        gdf = ycl_gdf(gdf)

        base_line, fzxxs_hx, _, _ = Nonline(gdf)
        self.assertEqual(len(fzxxs_hx), 1, "应有 1 条环线")
        self.assertEqual(len(base_line), 0, "不应有非环线")

    def test_avg_station_with_wgs84_input(self):
        """avg_station 对 WGS84 输入也应正确工作。"""
        avg_sta = avg_station(self.gdf_wgs84)
        self.assertGreater(len(avg_sta), 0)
        self.assertGreater(avg_sta['hx'].iloc[0], 0)


class TestImports(unittest.TestCase):
    """包导入测试。"""

    def test_package_version(self):
        """版本号存在。"""
        import BusNetPynew
        self.assertIsNotNone(BusNetPynew.__version__)

    def test_all_modules_importable(self):
        """所有模块可导入。"""
        from BusNetPynew import buspider
        from BusNetPynew import busbuild
        from BusNetPynew import metrical
        from BusNetPynew import routplaning
        from BusNetPynew import csvis
        from BusNetPynew import find_cycle
        from BusNetPynew import WGS1984
        from BusNetPynew import citybus
        from BusNetPynew import buslist
        from BusNetPynew import citycode
        from BusNetPynew import utm_espg
        from BusNetPynew import utils
        from BusNetPynew import conversion_geo
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
