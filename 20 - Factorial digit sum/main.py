"""This is the python code for the 20th challange in projecteuler.com"""


def return_factorial_digits(number: int) -> list[int]:
    """
    This function returns the digits in the factorial of X
    in a array of integers.
    """
    factorial = 1
    for i in range(0, number):
        factorial *= number - i
    return [int(digit) for digit in str(factorial)]


def solve(number: int) -> int:
    """
    This function applies the function above, and sums the
    digits inside the returned array. It returns that sum.
    """
    solution = sum(return_factorial_digits(number))
    return solution


if __name__ == '__main__':
    print(solve(100))