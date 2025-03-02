import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest water level data
    update_water_levels(stations)

    # Get the 5 stations with the highest relative water level
    top_stations = stations_highest_rel_level(stations, 5)

    for station, _ in top_stations:
        # Fetch water level data for past 2 days
        dt = datetime.timedelta(days=2)
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        # Plot water levels
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    run()

