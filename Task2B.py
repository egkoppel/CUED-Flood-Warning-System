from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()
    
    # Update water levels for all stations
    update_water_levels(stations)
    
    # Iterate over stations and print those with relative level > 0.8
    risk_stations = stations_level_over_threshold(stations, 0.8)
    for station, level in risk_stations:
        print(f"{station.name}, {level}")

if __name__ == "__main__":
    run()