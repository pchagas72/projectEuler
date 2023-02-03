def checkPrime(number: int) -> int:
    for i in range(2, number):
        if (number % i) == 0 or number == 1:
            return 0
    return 1


def solve(limit: int) -> int:
    prime_counter = 0
    current_number = 0
    while prime_counter != limit+1:
        current_number += 1
        prime_counter += checkPrime(current_number)
    return current_number


if __name__ == '__main__':
    print(solve(10001))
