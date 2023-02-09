"""This code solves the 12th challange on projectEuler.net"""
from math import sqrt
from itertools import count


def return_divisors(triangle: int) -> list[int]:
    """
    This function returns the divisors if the given triangle.
    Not the most efficient, but it's the way I did and understand.
    """
    divisors = []
    limit = int(sqrt(triangle))
    for possible_divisor in range(1, limit + 1):
        if triangle % possible_divisor == 0:
            divisors.append(possible_divisor)
            if possible_divisor != triangle / possible_divisor:
                divisors.append(triangle / possible_divisor)
    return divisors


def solve() -> int:
    """
    This function applies return_divisors() for every triangle.
    """
    triangle = 0
    for integer in count(start=1):
        triangle += integer
        divisors = return_divisors(triangle)
        if len(divisors) >= 500:
            break
    return triangle


if __name__ == '__main__':
    print(solve())
