package main

func fibonacci(x int) int {
	if ( x == 0) {
		return 0
	} else if(x == 1){
		return 1
	} else {
		return fibonacci(x-1) + fibonacci(x-2)
	}
}
func solve() int{
	var sum int = 0;
	var value int = 0;	
	var counter int = 0;
	for value < 4000000{
		value = fibonacci(counter);	
		if value % 2 == 0{
			sum += value;
		}
		counter++;
	}
	return sum;
}

func main(){
	println(solve())
}
