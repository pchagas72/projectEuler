package main

func is_prime(number int) bool {
	if number == 1 {
		return false
	}
	for divisor := 2; divisor*divisor < number; divisor++ {
		if number%divisor == 0 {
			return false
		}
	}
	return true
}

func solve(limit int) int {
	var primes_sum int = 0
	for test_number := 1; test_number < limit; test_number++ {
		if is_prime(test_number) {
			primes_sum += test_number
		}
	}
	return primes_sum
}

func main() {
	println(solve(2000000))
}
