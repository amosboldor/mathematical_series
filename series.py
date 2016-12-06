"""Define fibonacci and lucas functions."""


def fibonacci(n):
    """Return nth value of the fibonacci sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
