from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

def main():
    stations = build_station_list()
    
    # Get rivers with stations
    rivers = rivers_with_station(stations)
    print(f"{len(rivers)} rivers with at least one station. First 10 - {sorted(rivers)[:10]}")
    
    # Get stations by river
    river_station_map = stations_by_river(stations)
    
    # Print example rivers and their stations
    for river in ["River Aire", "River Cam", "River Thames"]:
        if river in river_station_map:
            station_names = sorted(station.name for station in river_station_map[river])
            print(f"Stations on {river}: {station_names}")

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    main()
