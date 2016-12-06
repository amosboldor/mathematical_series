"""Define fibonacci and lucas functions."""


def fibonacci(n):
    """Return nth value of the fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return nth value of the lucas sequence."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """Return nth value (based on arguments)."""
    if n == 0:
        return first
    elif n == 1:
        return second
    return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
