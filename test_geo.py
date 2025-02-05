from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation

station_list = [
    MonitoringStation(0, 0, "A", (0, 0), 0, "", ""),
    MonitoringStation(1, 0, "A", (3.0, 4.0), 0, "", ""),
    MonitoringStation(1, 0, "A", (5.5, 5.5), 0, "", ""),
]


def test_stations_by_distance_is_sorted():
    ret = stations_by_distance(station_list, (0, 0))
    ret = [dist for _, dist in ret]
    assert sorted(ret) == ret

    ret = stations_by_distance(station_list, (3.6, 5.7))
    ret = [dist for _, dist in ret]
    assert sorted(ret) == ret

    ret = stations_by_distance(station_list, (40e6, 5e-2))
    ret = [dist for _, dist in ret]
    assert sorted(ret) == ret


def test_stations_by_distance_correct_distance():
    dist = stations_by_distance([station_list[0]], (0, 0))[0]
    assert abs(dist[1]) <= 1e-6

    dist = stations_by_distance([station_list[1]], (0, 0))[0]
    assert abs(dist[1] - 555807) <= 10

    dist = stations_by_distance([station_list[0]], (5, 12))[0]
    assert abs(dist[1] - 1443970) <= 10


def test_stations_within_radius():
    within_radius = stations_within_radius(station_list, (0, 0), 0)
    assert len(within_radius) == 1

    within_radius = stations_within_radius(station_list, (0, 0), 1)
    assert len(within_radius) == 1

    within_radius = stations_within_radius(station_list, (0, 0), 600000)
    assert len(within_radius) == 2
