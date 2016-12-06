"""Testing series.py."""


def test_fib0():
    """Test fib for n 0 and 1."""
    from series import fibonacci
    assert fibonacci(0) == 0 and fibonacci(1) == 1
