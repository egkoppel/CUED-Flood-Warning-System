# Copyright (C) 2018 Garth N. Wells
# Copyright (C) 2025 Eliyahu Gluschove-Koppel
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from math import sqrt, cos, asin, radians

from .station import MonitoringStation
from .utils import sorted_by_key  # noqa


def stations_by_distance(
        stations: list[MonitoringStation],
        p: tuple[float, float]
) -> list[tuple[MonitoringStation, float]]:
    """Calculates the distance in meters from a list of stations to a given coordinate

    Arguments:
        stations -- list of `MonitoringStation` objects to calculate the distance to
        p -- tuple of a coordinate to calculate the distance to
    """

    # Calculate distances between all stations
    distances = [(station, _haversine_distance_between(p, station.coord)) for station in stations]

    # Sort the list by the second element of the tuple (distance) and return the list
    return sorted_by_key(distances, 1)


def stations_within_radius(
        stations: list[MonitoringStation],
        centre: tuple[float, float],
        r: float
) -> list[MonitoringStation]:
    """Returns a list of `MonitoringStation` objects within `r` meters of the point `centre`"""

    all_stations = stations_by_distance(stations, centre)
    return list(filter(lambda station: station[1] <= r, all_stations))


def _haversine_distance_between(a: tuple[float, float], b: tuple[float, float], r: float = 6371009) -> float:
    """Calculates the haversine distance between two coordinates each given as a tuple of floats (lat, long)

    Arguments:
        a, b -- the two coordinates
        r -- the radius of the sphere, defaulting to Earth average radius
    """

    φ0, λ0 = a
    φ1, λ1 = b

    return 2 * r * asin(sqrt(
        0.5 * (1 - cos(radians(abs(φ0 - φ1))) + cos(radians(φ0))*cos(radians(φ1))*(1 - cos(radians(abs(λ0 - λ1)))))
    ))
