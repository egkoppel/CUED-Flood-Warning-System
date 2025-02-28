from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
        station1 = MonitoringStation("1", "m1", "Station1", (0, 0), (1.0, 3.0), "River1", "Town1")
        station2 = MonitoringStation("2", "m2", "Station2", (0, 0), (1.0, 4.0), "River2", "Town2")
        station3 = MonitoringStation("3", "m3", "Station3", (0, 0), (1.0, 2.0), "River3", "Town3")
        
        station1.latest_level = 3.0
        station2.latest_level = 4.0
        station3.latest_level = 1.5
        
        stations = [station1, station2, station3]
        result = stations_level_over_threshold(stations, 0.8)
        
        assert len(result) == 2
        assert "Station2" in [result[0][0].name, result[1][0].name]
        assert "Station1" in [result[0][0].name, result[1][0].name]
        
        result = stations_level_over_threshold(stations, 1.2)
        assert len(result) == 0
