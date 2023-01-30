def fibonacci(x) -> int :
    if x <= 1 :
        return x
    else :
        return fibonacci(x-1) + fibonacci(x-2)

def solve() -> int :
    sum = 0
    value = 0
    counter = 0
    while value < 4000000:
        value = fibonacci(counter)
        if value % 2 == 0 :
            sum += value
        counter += 1
    return sum

def main() -> None :
    print(solve())

if __name__ == "__main__":
    main()
