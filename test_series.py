"""Testing series.py."""
import pytest


FIB_PARAMS_TABLE = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 5],
    [6, 8],
    [7, 13]
]


LUCAS_PARAMS_TABLE = [
    [0, 2],
    [1, 1],
    [2, 3],
    [3, 4],
    [4, 7],
    [5, 11],
    [6, 18],
    [7, 29]
]


@pytest.mark.parametrize("m, result", FIB_PARAMS_TABLE)
def test_fib(m, result):
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(m) == result


@pytest.mark.parametrize("m, result", LUCAS_PARAMS_TABLE)
def test_lucas(m, result):
    """Test lucas function."""
    from series import lucas
    assert lucas(m) == result


@pytest.mark.parametrize("m, result", FIB_PARAMS_TABLE)
def test_sum_series_fib(m, result):
    """Test default sum_series."""
    from series import sum_series
    assert sum_series(m) == result


@pytest.mark.parametrize("m, result", LUCAS_PARAMS_TABLE)
def test_sum_series_lucas(m, result):
    """Test sum_series with lucas numbers."""
    from series import sum_series
    assert sum_series(m, 2, 1) == result


@pytest.mark.parametrize("m, result", LUCAS_PARAMS_TABLE)
def test_sum_series_lucas_iterative(m, result):
    """Test sum_series with lucas numbers."""
    from series import sum_series_iterative
    assert sum_series_iterative(m, 2, 1) == result


@pytest.mark.parametrize("m, result", FIB_PARAMS_TABLE)
def test_sum_series_fib_iterative(m, result):
    """Test sum_series with lucas numbers."""
    from series import sum_series_iterative
    assert sum_series_iterative(m, 0, 1) == result


@pytest.mark.parametrize("m, result", FIB_PARAMS_TABLE)
def test_fibonacci_iterative(m, result):
    """Test fibonacci_iterative."""
    from series import fibonacci_iterative
    assert fibonacci_iterative(m) == result


@pytest.mark.parametrize("m, result", LUCAS_PARAMS_TABLE)
def test_lucas_iterative(m, result):
    """Test sum_series with lucas numbers."""
    from series import lucas_iterative
    assert lucas_iterative(m) == result
