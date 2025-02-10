# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

# Test that the station is consistent

def test_typical_range_consistent():

     # test for consistent data
    station1 = MonitoringStation("1", "m1", "Station1", (52.0, 0.1), (0.5, 1.5), "River 1", "Town 1")
    assert station1.typical_range_consistent() == True
    
    # test if low >= high (inconsistent data)
    station2 = MonitoringStation("2", "m2", "Station2", (52.0, 0.1), (1.5, 0.5), "River 2", "Town 2")
    assert station2.typical_range_consistent() == False
    
    # test if data missing
    station3 = MonitoringStation("3", "m3", "Station3", (52.0, 0.1), None, "River 3", "Town 3")
    assert station3.typical_range_consistent() == False
    
    # test if data incomplete
    station4 = MonitoringStation("4", "m4", "Station4", (52.0, 0.1), (None, 1.5), "River 4", "Town 4")
    assert station4.typical_range_consistent() == False

    station5 = MonitoringStation("5", "m5", "Station5", (52.0, 0.1), (0.5, None), "River 5", "Town 5")
    assert station5.typical_range_consistent() == False

# Test a list of inconsistent stations can be created

def test_inconsistent_typical_range_stations():
    """Test the inconsistent_typical_range_stations function."""
    
    station1 = MonitoringStation("1", "m1", "Station1", (52.0, 0.1), (0.5, 1.5), "River 1", "Town 1")
    station2 = MonitoringStation("2", "m2", "Station2", (52.0, 0.1), (1.5, 0.5), "River 2", "Town 2")
    station3 = MonitoringStation("3", "m3", "Station3", (52.0, 0.1), None, "River 3", "Town 3")
    station4 = MonitoringStation("4", "m4", "Station4", (52.0, 0.1), (None, 1.5), "River 4", "Town 4")
    station5 = MonitoringStation("5", "m5", "Station5", (52.0, 0.1), (0.5, None), "River 5", "Town 4")
    
    stations = [station1, station2, station3, station4, station5]
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    assert set(station.name for station in inconsistent_stations) == {"Station2", "Station3", "Station4", "Station5"}
