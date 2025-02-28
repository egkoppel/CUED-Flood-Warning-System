
def stations_level_over_threshold(stations, tol):
    return [station for station in stations if station.typical_range_consistent() and station.relative_water_level() is not None and station.relative_water_level() > tol]
