import datetime

from matplotlib.dates import date2num

from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def main():
    # Build list of stations
    stations = build_station_list()

    # Update latest water level data
    update_water_levels(stations)

    # Take only the stations that are already near to the typical high level
    stations = stations_level_over_threshold(stations, 0.8)

    print(f"Calculating based on {len(stations)} stations")
    print(f"0/{len(stations)}", end="\r")

    # Then calculate the polynomial fit with degree 4 based on the past week, and use it to predict the values for
    # the next two days
    station_scores = []
    for i, station in enumerate(stations):
        print(f"{i}/{len(stations)}", end="\r")
        station, rel_level = station # Since `stations_level_over_threshold` returns a tuple with the relative level too

        # Fetch water level data for past 2 days
        dt = datetime.timedelta(days=5)
        dates, levels = fetch_measure_levels(station.measure_id, dt)

        # polyfit seems to sometimes throw weird errors inside numpy so just ignore the broken stations?
        try:
            # Plot water levels
            poly, d0 = polyfit(dates, levels, 4)
        except:
            station_scores.append(None)
            continue

        now = datetime.datetime.utcnow()
        now_val = poly(date2num(now) - d0)
        next_day_val = poly(date2num(now + datetime.timedelta(days=1)) - d0)
        next2_day_val = poly(date2num(now + datetime.timedelta(days=2)) - d0)

        # Calculate the rise each day
        rise_now_next = next_day_val - now_val
        rise_next_next2 = next2_day_val - next_day_val

        # If the level is going to fall, then give station a score of 0
        if rise_now_next <= 0 or rise_next_next2 <= 0:
            station_scores.append(0)
            continue

        # Otherwise, see whether it will start rising faster
        rise_factor = rise_next_next2 / rise_now_next

        # If this is >1, then the level is going to rise faster, if <1, then the level is going to level off, and so
        # the likelihood of flooding is lower, so score it lower
        # The likelihood of flooding is also probably dependent on the rate of level rise, so multiply this in too
        # and also the current relative level so multiply it all together
        score = rise_next_next2 * (2 if rise_factor >= 1 else 1) * rel_level
        station_scores.append(score)

    # Then for each town, calculate the mean score between all the stations
    towns = {} # Store a dict of town name to (score, station_count)
    for score, station in zip(station_scores, stations):
        if score is None:
            continue
        if station[0].town is None:
            continue

        if station[0].town in towns.keys():
            towns[station[0].town][0] += score
            towns[station[0].town][1] += 1
        else:
            towns[station[0].town] = [score, 1]

    # Looking at the resulting data, many towns have a score of 0 so classify these as low
    # Many towns are under 1, so classify these as moderate, <5 as high, and anything above as severe
    for town, score in towns.items():
        mean_score = score[0] / score[1]
        town_name_padded = " "*(21 - len(town))
        if mean_score < 1e-6:
            print(f"{town}:{town_name_padded}Low risk (score: {mean_score:.3f} based on {score[1]} stations)")
        elif mean_score < 1:
            print(f"{town}:{town_name_padded}Moderate risk (score: {mean_score:.3f} based on {score[1]} stations)")
        elif mean_score < 5:
            print(f"{town}:{town_name_padded}High risk (score: {mean_score:.3f} based on {score[1]} stations)")
        else:
            print(f"{town}:{town_name_padded}Severe risk (score: {mean_score:.3f} based on {score[1]} stations)")


if __name__ == "__main__":
    main()
