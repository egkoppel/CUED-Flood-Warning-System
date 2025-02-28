# threshold for task 2B
def stations_level_over_threshold(stations, tol):
    risk_stations = []
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            risk_stations.append((station, station.relative_water_level()))
    return risk_stations

def stations_highest_rel_level(stations, N):
    """Returns a list of N stations with the highest relative water levels"""
    station_levels = [(station, station.relative_water_level()) for station in stations if station.relative_water_level() is not None]

    # Sort by relative level in descending order
    station_levels_sorted = sorted(station_levels, key=lambda x: x[1], reverse=True)

    # Return the top N stations
    return station_levels_sorted[:N]
