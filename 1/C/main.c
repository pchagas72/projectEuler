#include <stdio.h>

int solve() {
	int sum = 0;
	for (int i = 0; i < 1000; i++) {
		if (i % 3 == 0 || i % 5 == 0){
			sum += i;
		}
	}
	return sum;
}

int main() {
	printf("%d\n", solve());
	return 0;
}
