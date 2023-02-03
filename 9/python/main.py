def solve(limit: int) -> int:
    max_a_b = int(limit / 2)
    for a in range(1, max_a_b):
        for b in range(1, max_a_b):
            c = limit - a - b
            if a**2 + b**2 == c**2 and a < b < c:
                print('Found', a, b, c)
                return a * b * c
    return None


if __name__ == '__main__':
    print('Answer =', solve(1000))
