"""新增功能模块的单元测试。

覆盖：可达性分析、线网优化、换乘分析、网络韧性、POI 联动。
"""

import unittest

import geopandas as gpd
import networkx as nx
import pandas as pd
from shapely.geometry import LineString, Point, Polygon

from BusNetPynew.accessibility import (
    isochrone,
    multi_isochrone,
    travel_time_matrix,
    station_service_area,
)
from BusNetPynew.optimization import (
    find_redundant_segments,
    detect_spacing_anomalies,
    evaluate_route_efficiency,
    suggest_new_stops,
)
from BusNetPynew.transfer import (
    identify_transfer_stations,
    direct_reach_rate,
    transfer_connectivity,
    line_connection_matrix,
    transfer_summary,
)
from BusNetPynew.resilience import (
    critical_nodes,
    simulate_node_failure,
    simulate_line_failure,
    redundancy_analysis,
    network_robustness,
)
from BusNetPynew.poi_bindling import (
    station_poi_profile,
    commute_analysis,
    nearby_stations,
)


def _build_test_network():
    """构建测试用公交网络。

    网络拓扑:
        s1(火车站) --1路/2路--> s2(五一广场) --1路--> s3(岳麓山)
        s1(火车站) --2路--> s4(烈士公园) --2路--> s5(省博物馆)
        s2(五一广场) --3路--> s4(烈士公园)
    """
    G = nx.Graph()
    G.add_node('s1', pos=(112.98, 28.20), staname='火车站', bus_lines=['1路(上行)', '2路(上行)'])
    G.add_node('s2', pos=(112.97, 28.19), staname='五一广场', bus_lines=['1路(上行)', '3路(上行)'])
    G.add_node('s3', pos=(112.95, 28.18), staname='岳麓山', bus_lines=['1路(上行)'])
    G.add_node('s4', pos=(112.99, 28.22), staname='烈士公园', bus_lines=['2路(上行)', '3路(上行)'])
    G.add_node('s5', pos=(113.00, 28.23), staname='省博物馆', bus_lines=['2路(上行)'])

    G.add_edge('s1', 's2', length=1.5, bus_lines=['1路(上行)', '2路(上行)'])
    G.add_edge('s2', 's3', length=2.0, bus_lines=['1路(上行)'])
    G.add_edge('s1', 's4', length=3.0, bus_lines=['2路(上行)'])
    G.add_edge('s4', 's5', length=2.5, bus_lines=['2路(上行)'])
    G.add_edge('s2', 's4', length=1.2, bus_lines=['3路(上行)'])
    return G


def _build_test_gdf():
    """构建测试用线网 GeoDataFrame。"""
    data = [
        {'stationname': '火车站', 'nt_stationname': '五一广场',
         'id': 's1', 'next_id': 's2', 'name': '1路(上行)', 'hx': 1.5},
        {'stationname': '五一广场', 'nt_stationname': '岳麓山',
         'id': 's2', 'next_id': 's3', 'name': '1路(上行)', 'hx': 2.0},
        {'stationname': '火车站', 'nt_stationname': '烈士公园',
         'id': 's1', 'next_id': 's4', 'name': '2路(上行)', 'hx': 3.0},
        {'stationname': '烈士公园', 'nt_stationname': '省博物馆',
         'id': 's4', 'next_id': 's5', 'name': '2路(上行)', 'hx': 2.5},
        {'stationname': '五一广场', 'nt_stationname': '烈士公园',
         'id': 's2', 'next_id': 's4', 'name': '3路(上行)', 'hx': 1.2},
    ]
    gdf = gpd.GeoDataFrame(data)
    gdf['geometry'] = [
        LineString([(112.98, 28.20), (112.97, 28.19)]),
        LineString([(112.97, 28.19), (112.95, 28.18)]),
        LineString([(112.98, 28.20), (112.99, 28.22)]),
        LineString([(112.99, 28.22), (113.00, 28.23)]),
        LineString([(112.97, 28.19), (112.99, 28.22)]),
    ]
    gdf = gdf.set_geometry('geometry')
    gdf.crs = 'EPSG:4326'
    return gdf


def _build_test_stops():
    """构建测试用站点 GeoDataFrame。"""
    data = [
        {'stationname': '火车站', 'lng': 112.98, 'lat': 28.20, 'id': 's1'},
        {'stationname': '五一广场', 'lng': 112.97, 'lat': 28.19, 'id': 's2'},
        {'stationname': '岳麓山', 'lng': 112.95, 'lat': 28.18, 'id': 's3'},
        {'stationname': '烈士公园', 'lng': 112.99, 'lat': 28.22, 'id': 's4'},
        {'stationname': '省博物馆', 'lng': 113.00, 'lat': 28.23, 'id': 's5'},
    ]
    gdf = gpd.GeoDataFrame(
        data,
        geometry=[Point(r['lng'], r['lat']) for r in data],
        crs='EPSG:4326',
    )
    return gdf


# ========== 可达性分析测试 ==========

class TestAccessibility(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.G = _build_test_network()
        cls.stops = _build_test_stops()

    def test_isochrone_basic(self):
        result = isochrone(self.G, 's1', time_limit=30)
        self.assertGreater(result['total_reachable'], 0)
        self.assertIn('s1', result['reachable_nodes'])
        self.assertIsInstance(result['reachable_details'], pd.DataFrame)

    def test_isochrone_short_time(self):
        result = isochrone(self.G, 's1', time_limit=1)
        self.assertLessEqual(result['total_reachable'], 2)

    def test_isochrone_invalid_node(self):
        result = isochrone(self.G, 'nonexistent', time_limit=30)
        self.assertEqual(result['total_reachable'], 0)

    def test_multi_isochrone(self):
        gdf = multi_isochrone(self.G, 's1', [15, 30, 60])
        self.assertIsInstance(gdf, gpd.GeoDataFrame)
        self.assertLessEqual(len(gdf), 3)

    def test_travel_time_matrix(self):
        matrix = travel_time_matrix(self.G, nodes=['s1', 's2', 's3'])
        self.assertEqual(matrix.shape, (3, 3))
        self.assertEqual(matrix.loc['s1', 's1'], 0)
        self.assertGreater(matrix.loc['s1', 's3'], 0)

    def test_station_service_area(self):
        result = station_service_area(self.stops, radius_m=500)
        self.assertEqual(len(result), 5)
        self.assertIn('area_km2', result.columns)


# ========== 线网优化测试 ==========

class TestOptimization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.G = _build_test_network()
        cls.gdf = _build_test_gdf()

    def test_find_redundant_segments(self):
        df = find_redundant_segments(self.G, threshold=2)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('line_count', df.columns)

    def test_find_redundant_high_threshold(self):
        df = find_redundant_segments(self.G, threshold=10)
        self.assertEqual(len(df), 0)

    def test_detect_spacing_anomalies(self):
        result = detect_spacing_anomalies(self.gdf, min_km=0.5, max_km=2.5)
        self.assertIn('too_short', result)
        self.assertIn('too_long', result)
        self.assertIn('stats', result)
        self.assertGreater(result['stats']['total_segments'], 0)

    def test_evaluate_route_efficiency(self):
        df = evaluate_route_efficiency(self.gdf, self.G)
        self.assertGreater(len(df), 0)
        self.assertIn('efficiency_score', df.columns)

    def test_suggest_new_stops(self):
        result = suggest_new_stops(self.gdf, max_spacing_km=2.0)
        self.assertIsInstance(result, gpd.GeoDataFrame)


# ========== 换乘分析测试 ==========

class TestTransfer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.G = _build_test_network()

    def test_identify_transfer_stations(self):
        df = identify_transfer_stations(self.G)
        self.assertGreater(len(df), 0)
        self.assertIn('level', df.columns)
        self.assertTrue(df.iloc[0]['line_count'] >= 2)

    def test_direct_reach_rate(self):
        rates = direct_reach_rate(self.G)
        self.assertGreater(rates['direct_rate'], 0)
        self.assertGreaterEqual(rates['one_transfer_rate'], rates['direct_rate'])
        self.assertLessEqual(rates['direct_rate'], 1.0)

    def test_transfer_connectivity(self):
        df = transfer_connectivity(self.G)
        self.assertGreater(len(df), 0)
        self.assertIn('line_a', df.columns)
        self.assertIn('line_b', df.columns)

    def test_line_connection_matrix(self):
        matrix = line_connection_matrix(self.G)
        self.assertEqual(matrix.shape[0], matrix.shape[1])
        self.assertEqual(matrix.loc['1路', '1路'], 0)

    def test_transfer_summary(self):
        summary = transfer_summary(self.G)
        self.assertIn('transfer_stations', summary)
        self.assertIn('direct_rate', summary)
        self.assertGreater(summary['total_stations'], 0)


# ========== 网络韧性测试 ==========

class TestResilience(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.G = _build_test_network()

    def test_critical_nodes(self):
        df = critical_nodes(self.G, top_n=5)
        self.assertGreater(len(df), 0)
        self.assertIn('critical_score', df.columns)
        self.assertLessEqual(df.iloc[0]['critical_score'], 100)

    def test_simulate_node_failure(self):
        impact = simulate_node_failure(self.G, ['s1'])
        self.assertIn('severity', impact)
        self.assertGreater(len(impact['affected_lines']), 0)
        self.assertGreaterEqual(impact['after_components'], impact['original_components'])

    def test_simulate_line_failure(self):
        impact = simulate_line_failure(self.G, '1路')
        self.assertIn('severity', impact)
        self.assertIn('removed_edges', impact)

    def test_redundancy_analysis(self):
        result = redundancy_analysis(self.G)
        self.assertIn('bridge_count', result)
        self.assertIn('avg_redundancy', result)
        self.assertGreater(result['avg_redundancy'], 0)

    def test_network_robustness_targeted(self):
        df = network_robustness(self.G, attack_mode='targeted', max_removals=3)
        self.assertGreater(len(df), 1)
        self.assertIn('largest_ratio', df.columns)
        self.assertEqual(df.iloc[0]['largest_ratio'], 1.0)

    def test_network_robustness_random(self):
        df = network_robustness(self.G, attack_mode='random', max_removals=2)
        self.assertGreater(len(df), 1)


# ========== POI 联动测试 ==========

class TestPOI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.G = _build_test_network()
        cls.stops = _build_test_stops()
        cls.pois = gpd.GeoDataFrame(
            [
                {'name': '湘雅医院', 'type': '医院', 'lng': 112.975, 'lat': 28.195},
                {'name': '长沙一中', 'type': '学校', 'lng': 112.985, 'lat': 28.205},
                {'name': '万达广场', 'type': '商场', 'lng': 112.965, 'lat': 28.185},
                {'name': '省人民医院', 'type': '医院', 'lng': 112.995, 'lat': 28.225},
            ],
            geometry=[
                Point(112.975, 28.195),
                Point(112.985, 28.205),
                Point(112.965, 28.185),
                Point(112.995, 28.225),
            ],
            crs='EPSG:4326',
        )

    def test_station_poi_profile(self):
        df = station_poi_profile(self.stops, self.pois, radius_m=2000)
        self.assertEqual(len(df), 5)
        self.assertIn('total_pois', df.columns)

    def test_commute_analysis(self):
        result = commute_analysis(self.G, ['s1', 's2'], ['s4', 's5'])
        self.assertIn('avg_commute_min', result)
        self.assertIsNotNone(result['avg_commute_min'])
        self.assertGreater(result['avg_commute_min'], 0)

    def test_nearby_stations(self):
        result = nearby_stations(self.stops, lng=112.98, lat=28.20, radius_m=3000)
        self.assertGreater(len(result), 0)
        self.assertIn('distance_m', result.columns)


# ========== 模块导入测试 ==========

class TestNewModuleImports(unittest.TestCase):

    def test_all_new_modules_importable(self):
        from BusNetPynew import accessibility
        from BusNetPynew import optimization
        from BusNetPynew import transfer
        from BusNetPynew import resilience
        from BusNetPynew import poi_bindling
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
