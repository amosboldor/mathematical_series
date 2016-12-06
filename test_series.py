"""Testing series.py."""
import pytest

PARAMS_TABLE = [
    [0, 0],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 5],
    [6, 8],
    [7, 13]
]


@pytest.mark.parametrize("m, result", PARAMS_TABLE)
def test_fib(m, results):
    """The ackermann function params m and n."""
    from series import fibonacci
    assert fibonacci(m) == results
