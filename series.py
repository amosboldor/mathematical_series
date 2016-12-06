"""Functions to calculate values of integer summation sequences."""


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
    """Return nth value of generalized summation sequence."""
    if n == 0:
        return first
    elif n == 1:
        return second
    return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


if __name__ == "__main__":
    print(__doc__, "\n...\n")
    print("fibonacci(n):\n\n\t" + fibonacci.__doc__)
    print("\n>>> fibonacci(3)\n2\n...\n")
    print("lucas(n):\n\n\t" + lucas.__doc__)
    print("\n>>> lucas(3)\n4\n...\n")
    print("sum_series(n, [first=0], [second=1]):\n\n\t" + sum_series.__doc__)
    print("\n>>> sum_series(3)\n2")
    print("\n>>> sum_series(3, 2, 1)\n4")
