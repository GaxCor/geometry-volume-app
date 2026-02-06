import pytest
import math
from geometry.cylinder import volume_cylinder

def test_volume_cylinder_valid_inputs():
    radius, height = 2.0, 3.0
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == expected

def test_volume_cylinder_negative_dimension():
    radius, height = 2.0, -3.0
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == expected

def test_volume_cylinder_float_tolerance():
    radius, height = 1.1, 2.2
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius, height) == pytest.approx(expected, rel=1e-6)
