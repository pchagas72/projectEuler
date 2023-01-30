package main

func solve(n int) int {
	var i int = 2;

	for i * i <= n{
		println(n)
		if n % i != 0 {
			i++
		}else {
			n = n/i
		}

	}
	return n
}

func main(){
	println(solve(600851475143))
}
