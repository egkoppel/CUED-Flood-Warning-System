# Copyright (C) 2025 Eliyahu Gluschove-Koppel
#
# SPDX-License-Identifier: MIT
"""This module provides functions to analyse historical water level data
"""
import datetime

from matplotlib.dates import date2num
import numpy as np

from floodsystem.utils import sorted_by_key


def polyfit(dates, levels, p):
    combined_sorted = sorted_by_key(zip(dates, levels), 0)
    unzipped = list(zip(*combined_sorted))
    dates = unzipped[0]
    levels = unzipped[1]

    dates = date2num(dates)
    d0 = dates[0]
    dates = dates - d0

    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0
