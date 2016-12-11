"""Functions to calculate values of integer summation sequences."""


def fibonacci(n):
    """Return nth value of the fibonacci sequence."""
    return sum_series(n)


def lucas(n):
    """Return nth value of the lucas sequence."""
    return sum_series(n, 2, 1)


def sum_series(n, first=0, second=1):
    """Return nth value of generalized summation sequence."""
    if n == 0:
        return first
    elif n == 1:
        return second
    return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


def sum_series_iterative(n, first=0, second=1):
    """Iterative version of return nth value of the fibonacci sequence."""
    for i in range(n):
        first, second = second, first + second
    return first


def fibonacci_iterative(n):
    """Iterative version of return nth value of the fibonacci sequence."""
    sum_series_iterative(n)


def lucas_iterative(n):
    """Iterative version of return nth value of the lucas sequence."""
    sum_series_iterative(n, 2, 1)

if __name__ == "__main__":
    print(__doc__, "\n...\n")
    print("fibonacci(n):\n\n\t" + fibonacci.__doc__)
    print("\n>>> fibonacci(3)\n2\n...\n")
    print("lucas(n):\n\n\t" + lucas.__doc__)
    print("\n>>> lucas(3)\n4\n...\n")
    print("sum_series(n, [first=0], [second=1]):\n\n\t" + sum_series.__doc__)
    print("\n>>> sum_series(3)\n2")
    print("\n>>> sum_series(3, 2, 1)\n4")
