def solve(n) -> int :
    i = 2;

    while i*i <= n :
        if n % i != 0 :
            i += 1
        else :
            n = n/i
    return n

def main() -> None :
    print(solve(600851475143))

if __name__ == "__main__":
    main()
