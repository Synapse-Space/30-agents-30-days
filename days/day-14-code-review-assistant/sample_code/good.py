from typing import Iterable


def calculate_total(numbers: Iterable[int]) -> int:
    """
    Calculate the sum of all numbers.
    """
    return sum(numbers)


class Calculator:
    """
    Simple calculator.
    """

    def add(self, a: int, b: int) -> int:
        """Add two numbers."""
        return a + b