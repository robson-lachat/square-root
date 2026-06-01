# math_logic.py

import math


def calculate_roots(limit: int):
    """Calculates the square root from 1 to the specified limit."""
    if limit < 0:
        raise ValueError("Cannot calculate square root of a negative number")

    roots = [math.sqrt(i) for i in range(1, limit + 1)]
    return roots


if __name__ == "__main__":  # pragma: no cover
    limit = 12
    print(f"Calculating square roots from 1 to {limit}:")
    print(calculate_roots(limit))



if __name__ == "__main__":  # pragma: no cover
    limit = 5
    print(f"Calculating square roots from 1 to {limit}:")
    print(calculate_roots(limit))
