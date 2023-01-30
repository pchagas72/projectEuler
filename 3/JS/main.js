function solve(n) {

	var i = 2;

	while (i * i <= n) {
		if (n % i != 0) {
			i++;
		} else {
			n = n/i;
		}
	}
	return n;
}

console.log(solve(600851475143));
