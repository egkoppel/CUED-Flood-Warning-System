"""Unit test for the plot module"""
from io import BytesIO

import matplotlib.pyplot as plt
import datetime
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import pytest
from matplotlib.testing.decorators import image_comparison


# From https://matplotlib.org/devdocs/devel/testing.html#writing-an-image-comparison-test

@pytest.fixture
def mock_station():
    """Create a mock station for testing"""
    return MonitoringStation("test-id", "measure-id", "Test Station", (0, 0), (1.0, 3.0), "Test River", "Test Town")


@image_comparison(baseline_images=['plot_water_levels'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_plot_water_levels_valid_data(mock_station, monkeypatch):
    """Test plot_water_levels with valid data"""

    # Mock plt.show() to prevent actual plotting
    monkeypatch.setattr(plt, "show", lambda: None)

    dates = [datetime.datetime(2024, 2, i) for i in range(1, 6)]
    levels = [1.2, 1.8, 2.0, 2.5, 2.9]

    plot_water_levels(mock_station, dates, levels)


def test_plot_water_levels_no_data(mock_station, capsys):
    """Test plot_water_levels when no data is provided"""

    plot_water_levels(mock_station, [], [])

    captured = capsys.readouterr()
    assert f"No data available for {mock_station.name}" in captured.out


@image_comparison(baseline_images=['plot_fit'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_plot_water_levels_valid_data(mock_station, monkeypatch):
    """Test plot_water_levels with valid data"""

    # Mock plt.show() to prevent actual plotting
    monkeypatch.setattr(plt, "show", lambda: None)

    dates = [datetime.datetime(2024, 2, i) for i in range(1, 3)]
    levels = [1.2, 2.9]

    plot_water_level_with_fit(mock_station, dates, levels, 1)
