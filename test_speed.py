# test_speed.py
import pytest
from speed import calculate_speed

def test_calculate_speed():
    assert calculate_speed(100, 2) == 50
    assert calculate_speed(20, 1) == 20

def test_calculate_speed_zero_time():
    with pytest.raises(ValueError):
        calculate_speed(100, 0)

def test_calculate_speed_negative_time():
    with pytest.raises(ValueError):
        calculate_speed(100, -1)