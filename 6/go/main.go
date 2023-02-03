package main

func solve(limit int) int {
	var squared_sum int = 0
	var sum_squared int = 0
	for i := 0; i <= limit; i++ {
		squared_sum += i * i
		sum_squared += i
	}
	sum_squared = sum_squared * sum_squared
	var difference = sum_squared - squared_sum
	return difference
}

func main() {
	println(solve(100))
}
