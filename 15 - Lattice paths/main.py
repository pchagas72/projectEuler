"""This is the python code for the 15th challange in projecteuler.com"""
from math import factorial


def solve(side: int) -> int:
    """
    I reached this equation after 2 hours of trial and error...
    It's pretty simple, since the result will always be the
    combination of (2 * the number of sides and the number of sides
    itself). My notes are in this same folder.
    """
    return int(factorial(2 * side) / (factorial(side) ** 2))


if __name__ == '__main__':
    print(solve(20))
