# Copyright (C) 2025 Eliyahu Gluschove-Koppel
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def main():
    stations = build_station_list()

    by_distance = stations_by_distance(stations, (52.2053, 0.1218))
    by_distance = [(station.name, station.town, dist) for station, dist in by_distance]

    print(f"10 closest:\n{by_distance[:10]}")
    print(f"---\n10 furthest:\n{by_distance[-10:]}")


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    main()
