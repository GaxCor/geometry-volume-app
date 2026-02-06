import pytest
import math
from geometry.sphere import volume_sphere

def test_volume_sphere_valid_inputs():
    radius = 2.0
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == expected

def test_volume_sphere_negative_radius_raises():
    radius = -2.0
    with pytest.raises(ValueError):
        volume_sphere(radius)

def test_volume_sphere_float_tolerance():
    radius = 1.1
    expected = (4 / 3) * math.pi * radius**3
    assert volume_sphere(radius) == pytest.approx(expected, rel=1e-6)
