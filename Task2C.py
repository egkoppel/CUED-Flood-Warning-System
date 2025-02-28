from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update latest water level data
    update_water_levels(stations)

    # Get the 10 stations with the highest relative water level
    top_stations = stations_highest_rel_level(stations, 10)

    # Print results
    for station, level in top_stations:
        print(f"{station.name} {level}")

if __name__ == "__main__":
    run()
