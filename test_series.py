"""Testing series.py."""


def test_fib0():
    from series import fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1