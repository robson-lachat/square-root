# test_math.py

import pytest
from src.math_logic import calculate_roots


def test_list_size():
    # Checks if exactly 10 results were generated
    result = calculate_roots(10)
    assert len(result) == 10


def test_specific_values():
    result = calculate_roots(10)
    # The root of 4 (index 3) should be 2.0
    assert result[3] == 2.0
    # The root of 9 (index 8) should be 3.0
    assert result[8] == 3.0


def test_negative_number():
    with pytest.raises(ValueError):
        calculate_roots(-1)
