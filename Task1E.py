from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def main():
    stations = build_station_list()
    river_counts = rivers_by_station_number(stations, 9)
    print(river_counts)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    main()

