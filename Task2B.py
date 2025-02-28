from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def main():
    # Build list of stations
    stations = build_station_list()
    
    # Update water levels for all stations
    update_water_levels(stations)
    
    # Iterate over stations and print those with relative level > 0.8
    risk_station = stations_level_over_threshold(stations, 0.8)
    for station in risk_station:
        print(station[0].name, station[1])
if __name__ == "__main__":
    main()