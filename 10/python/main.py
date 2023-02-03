def is_prime(number: int) -> bool:
    if number == 1:
        return False
    i = 2
    while i**2 <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def solve(limit: int) -> int:
    sum = 0
    test_number = 1
    while test_number < limit:
        if is_prime(test_number):
            sum += test_number
        test_number += 1
    return sum


def get_answers() -> None:
    print(solve(2000000))


if __name__ == '__main__':
    get_answers()
