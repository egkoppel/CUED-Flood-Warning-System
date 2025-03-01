import matplotlib.pyplot as plt
from datetime import datetime


def _add_water_level_to_plot(station, dates, levels):
    if not dates or not levels:
        print(f"No data available for {station.name}")
        return

    # Plot water levels
    plt.plot(dates, levels, label="Water Level")

    # Plot typical low and high levels
    plt.axhline(y=station.typical_range[0], color='r', linestyle='--', label="Typical Low")
    plt.axhline(y=station.typical_range[1], color='g', linestyle='--', label="Typical High")


def plot_water_levels(station, dates, levels):
    _add_water_level_to_plot(station, dates, levels)

    # Labels and title
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Ensure layout doesn't cut off labels
    plt.tight_layout()

    # Show plot
    plt.show()
