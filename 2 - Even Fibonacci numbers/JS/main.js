function fibonacci(x) {
	if (x <= 1) {
		return x;
	} else {
		return fibonacci(x-1) + fibonacci(x-2);
	}
}

function solve() {
	var sum = 0;
	var value = 0;
	var counter = 0;

	while (value < 4000000){
		value = fibonacci(counter);
		if (value % 2 == 0){
			sum += value;
		}
		counter++;
	}
	return sum;
}

console.log(solve());
