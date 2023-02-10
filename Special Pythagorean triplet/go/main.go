package main

func checks(a int, b int, c int) bool {
	if a*a+b*b == c*c {
		if a < b && b < c {
			return true
		}
	}
	return false
}

func solve(limit int) int {
	var max_a_b int = int(limit / 2)
	for a := 1; a < max_a_b; a++ {
		for b := 1; b < max_a_b; b++ {
			var c int = limit - a - b
			if checks(a, b, c) {
				return a * b * c
			}
		}
	}
	return 0
}

func main() {
	println(solve(1000))
}
