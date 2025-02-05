# Copyright (C) 2025 Eliyahu Gluschove-Koppel
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def main():
    stations = build_station_list()

    by_distance = stations_within_radius(stations, (52.2053, 0.1218), 10000)
    names = [station.name for station, _ in by_distance]

    print(f"{sorted(names)}")


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    main()
