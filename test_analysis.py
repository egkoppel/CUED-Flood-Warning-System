import datetime

from matplotlib.dates import date2num

from floodsystem.analysis import polyfit


def test_polyfit_order_1():
    dates = [
        datetime.date(2025, 1, 1),
        datetime.date(2025, 1, 5),
    ]

    levels = [5, 10]

    poly, d0 = polyfit(dates, levels, 1)

    assert d0 == date2num(dates[0])
    assert abs(poly(date2num(dates[0]) - d0) - 5) < 1e-6
    assert abs(poly(date2num(dates[1]) - d0) - 10) < 1e-6
    assert poly.order == 1


def test_polyfit_order_2():
    dates = [
        datetime.date(2025, 1, 1),
        datetime.date(2025, 1, 5),
        datetime.date(2025, 1, 15),
    ]

    levels = [5, 10, 34]

    poly, d0 = polyfit(dates, levels, 2)

    assert d0 == date2num(dates[0])
    assert abs(poly(date2num(dates[0]) - d0) - 5) < 1e-6
    assert abs(poly(date2num(dates[1]) - d0) - 10) < 1e-6
    assert abs(poly(date2num(dates[2]) - d0) - 34) < 1e-6
    assert poly.order == 2
