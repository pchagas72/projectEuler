package main

var divisors_test_list []int = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
var divisors_final_list []int = []int{11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

func max_array(array []int) int {
	var max int = 0
	for _, i := range array {
		if i > max {
			max = i
		}
	}
	return max
}

func return_remainder_sum(divisors_list []int, divisor int) int {
	var remainder_sum int = 0
	for _, i := range divisors_list {
		remainder_sum += divisor % i
	}
	return remainder_sum
}

func solve(divisors_slice []int) int {
	var max_value int = max_array(divisors_slice)
	var searching bool = true
	var divisor int = 0
	for searching {
		divisor += max_value
		if return_remainder_sum(divisors_slice, divisor) == 0 {
			break
		}
	}
	return divisor

}

func main() {
	var test_answer int = solve(divisors_test_list)
	var final_answer int = solve(divisors_final_list)
	println(test_answer)
	println(final_answer)
}
