import matplotlib.pyplot as plt
from datetime import datetime

def plot_water_levels(station, dates, levels):
    """Plots water level data for a given station over time."""
    if not dates or not levels:
        print(f"No data available for {station.name}")
        return

    # Plot water levels
    plt.plot(dates, levels, label="Water Level")

    # Plot typical low and high levels
    plt.axhline(y=station.typical_range[0], color='r', linestyle='--', label="Typical Low")
    plt.axhline(y=station.typical_range[1], color='g', linestyle='--', label="Typical High")

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

