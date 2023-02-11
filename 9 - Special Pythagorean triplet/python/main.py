"""This is the python code for the 9th challange in projecteuler.net"""


def solve(limit: int) -> int:
    """Function that solves the 9th problem in project euler."""
    max_a_b = int(limit / 2)
    for var_a in range(1, max_a_b):
        for var_b in range(1, max_a_b):
            var_c = limit - var_a - var_b
            if var_a**2 + var_b**2 == var_c**2 and var_a < var_b < var_c:
                print('Found', var_a, var_b, var_c)
                return var_a * var_b * var_c
    return None


if __name__ == '__main__':
    print('Answer =', solve(1000))
