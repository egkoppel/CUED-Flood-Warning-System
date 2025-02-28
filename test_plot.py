"""Unit test for the plot module"""

import matplotlib.pyplot as plt
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation
import pytest

@pytest.fixture
def mock_station():
    """Create a mock station for testing"""
    return MonitoringStation("test-id", "measure-id", "Test Station", (0, 0), (1.0, 3.0), "Test River", "Test Town")

def test_plot_water_levels_valid_data(mock_station, monkeypatch):
    """Test plot_water_levels with valid data"""
    
    # Mock plt.show() to prevent actual plotting
    monkeypatch.setattr(plt, "show", lambda: None)

    dates = [datetime.datetime(2024, 2, i) for i in range(1, 6)]
    levels = [1.2, 1.8, 2.0, 2.5, 2.9]

    try:
        plot_water_levels(mock_station, dates, levels)
    except Exception as e:
        pytest.fail(f"plot_water_levels raised an error: {e}")

def test_plot_water_levels_no_data(mock_station, capsys):
    """Test plot_water_levels when no data is provided"""
    
    plot_water_levels(mock_station, [], [])

    captured = capsys.readouterr()
    assert f"No data available for {mock_station.name}" in captured.out

