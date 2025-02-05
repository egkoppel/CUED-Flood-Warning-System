# Copyright (C) 2018 Garth N. Wells
# Copyright (C) 2025 Eliyahu Gluschove-Koppel
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math

from .station import MonitoringStation
from .utils import sorted_by_key  # noqa


def stations_by_distance(
        stations: list[MonitoringStation],
        p: tuple[float, float]
) -> list[tuple[MonitoringStation, float]]:
    """Calculates the distance from a list of stations to a given coordinate

    Arguments:
    stations -- list of `MonitoringStation` objects to calculate the distance to
    p -- tuple of a coordinate to calculate the distance to
    """
    raise NotImplementedError("stub")


def _distance_between(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Calculates the distance between two 2D coordinates each given as a tuple of floats"""

    return math.sqrt(
        (a[0] - b[0])**2 + (a[1] - b[1])**2
    )
