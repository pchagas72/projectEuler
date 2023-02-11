"""This code solves the 10th problem in projecteuler.net"""


def is_prime(number: int) -> bool:
    """This function checks if a number is prime with O(sqrt(n))"""
    if number == 1:
        return False
    i = 2
    while i**2 <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def solve(limit: int) -> int:
    """This function solves the problem using the previous ones"""
    primes_sum = 0
    test_number = 1
    while test_number < limit:
        if is_prime(test_number):
            primes_sum += test_number
        test_number += 1
    return primes_sum


if __name__ == '__main__':
    print(solve(2000000))
