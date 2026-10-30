
import pytest
from thermo import to_kelvin

def test_freezing_point():
    assert to_kelvin(0.0) == 273.15

@pytest.fixture
def boiling_celsius():
    return 100.0

def test_with_fixture(boiling_celsius):
    assert to_kelvin(boiling_celsius) == 373.15

@pytest.mark.parametrize("celsius, kelvin", [(0.0, 273.15), (-273.15, 0.0), (25.0, 298.15)])
def test_conversions(celsius, kelvin):
    assert to_kelvin(celsius) == pytest.approx(kelvin)

def test_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        to_kelvin(-300.0)
