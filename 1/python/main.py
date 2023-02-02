def solve(limit: int) -> int:
    sum: int = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def main() -> None:
    limit: int = 1000
    solve(limit)


if __name__ == '__main__':
    main()
