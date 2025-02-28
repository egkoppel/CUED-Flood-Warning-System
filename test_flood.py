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

from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_highest_rel_level():
    """Test stations_highest_rel_level function"""
    
    # Create mock stations with different relative water levels
    station1 = MonitoringStation("1", "m1", "Station1", (0, 0), (1.0, 3.0), "River1", "Town1")
    station2 = MonitoringStation("2", "m2", "Station2", (0, 0), (1.0, 4.0), "River2", "Town2")
    station3 = MonitoringStation("3", "m3", "Station3", (0, 0), (1.0, 2.0), "River3", "Town3")
    
    # Assign latest water levels
    station1.latest_level = 3.0  # relative level = (3.0 - 1.0) / (3.0 - 1.0) = 1.0
    station2.latest_level = 4.0  # relative level = (4.0 - 1.0) / (4.0 - 1.0) = 1.0
    station3.latest_level = 1.5  # relative level = (1.5 - 1.0) / (2.0 - 1.0) = 0.5

    stations = [station1, station2, station3]

    # Get the top 2 stations with the highest relative levels
    result = stations_highest_rel_level(stations, 2)

    assert len(result) == 2
    assert result[0][0].name in ["Station1", "Station2"]
    assert result[1][0].name in ["Station1", "Station2"]
    assert result[0][1] == 1.0  # Both Station1 and Station2 have the highest level 1.0
    assert result[1][1] == 1.0

    # Get the top 1 station
    result = stations_highest_rel_level(stations, 1)
    assert len(result) == 1
    assert result[0][0].name in ["Station1", "Station2"]
    assert result[0][1] == 1.0

    # Get the top 3 stations (should return all stations)
    result = stations_highest_rel_level(stations, 3)
    assert len(result) == 3
    assert result[2][0].name == "Station3"  # The station with the lowest relative level (0.5)

    # Request more stations than available
    result = stations_highest_rel_level(stations, 5)
    assert len(result) == 3  # Only 3 stations exist, so should return all of them

    # Test with an empty list
    result = stations_highest_rel_level([], 3)
    assert result == []
