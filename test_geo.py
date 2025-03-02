import pytest

from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, rivers_by_station_number, \
    stations_by_river
from floodsystem.station import MonitoringStation


@pytest.fixture
def station_list():
    return [
        MonitoringStation(0, 0, "A", (0, 0), 0, "River A", ""),
        MonitoringStation(1, 0, "A", (3.0, 4.0), 0, "River B", ""),
        MonitoringStation(1, 0, "A", (5.5, 5.5), 0, "River C", ""),
        MonitoringStation(0, 0, "A", (50, 50), 0, "River A", ""),
        MonitoringStation(1, 0, "A", (55, 55), 0, "River C", ""),
    ]


def test_stations_by_distance_is_sorted(station_list):
    ret = stations_by_distance(station_list, (0, 0))
    ret = [dist for _, dist in ret]
    assert sorted(ret) == ret

    ret = stations_by_distance(station_list, (3.6, 5.7))
    ret = [dist for _, dist in ret]
    assert sorted(ret) == ret

    ret = stations_by_distance(station_list, (40e6, 5e-2))
    ret = [dist for _, dist in ret]
    assert sorted(ret) == ret


def test_stations_by_distance_correct_distance(station_list):
    dist = stations_by_distance([station_list[0]], (0, 0))[0]
    assert abs(dist[1]) <= 1e-6

    dist = stations_by_distance([station_list[1]], (0, 0))[0]
    assert abs(dist[1] - 555807) <= 10

    dist = stations_by_distance([station_list[0]], (5, 12))[0]
    assert abs(dist[1] - 1443970) <= 10


def test_stations_within_radius(station_list):
    within_radius = stations_within_radius(station_list, (0, 0), 0)
    assert len(within_radius) == 1

    within_radius = stations_within_radius(station_list, (0, 0), 1)
    assert len(within_radius) == 1

    within_radius = stations_within_radius(station_list, (0, 0), 600000)
    assert len(within_radius) == 2


def test_rivers_with_station(station_list):
    river_names = rivers_with_station(station_list)

    assert river_names == {"River A", "River B", "River C"}
    assert "River A" in river_names
    assert "River D" not in river_names  # Should not be present


def test_rivers_by_station_number(station_list):
    # Get top 2 rivers with most stations
    top_rivers = rivers_by_station_number(station_list, 2)

    # Expected results: River A (2), River C (2), River B (1)
    assert ("River A", 2) in top_rivers
    assert ("River C", 2) in top_rivers
    assert len(top_rivers) == 2  # Only the top N rivers are returned

    # If asking for more than available rivers, return all
    all_rivers = rivers_by_station_number(station_list, 10)
    assert len(all_rivers) == 3  # There are only 3 unique rivers


def test_stations_by_river(station_list):
    river_dict = stations_by_river(station_list)

    assert len(river_dict["River A"]) == 2  # Two stations on River A
    assert len(river_dict["River B"]) == 1  # One station on River B
    assert len(river_dict["River C"]) == 2  # Two stations on River C
    assert station_list[0] in river_dict["River A"]
    assert station_list[1] in river_dict["River B"]
