"""This code is fodao"""
def is_prime(number: int) -> bool:
    """This code is fodao"""
    if number == 1:
        return False
    i = 2
    while i**2 <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def solve(limit: int) -> int:
    """This code is fodao"""
    primes_sum = 0
    test_number = 1
    while test_number < limit:
        if is_prime(test_number):
            primes_sum += test_number
        test_number += 1
    return primes_sum


def get_answers() -> None:
    """This code is fodao"""
    print(solve(2000000))


if __name__ == '__main__':
    get_answers()
