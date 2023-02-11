def solve(limit: int) -> int:
    squared_sum = 0
    sum_squared = 0
    for i in range(1, limit + 1):
        squared_sum += i**2
        sum_squared += i
    sum_squared = sum_squared**2
    difference = sum_squared - squared_sum
    return difference


if __name__ == '__main__':
    print(solve(100))
