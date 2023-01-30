#include <iostream>
using namespace std;

int solve(long n){
	int i = 2;
	while (i * i <= n) {
		if (n % i != 0) {
			i++;
		}else {
			n = n/i;
		}
	}
	return n;
}

int main(){
	cout << solve(600851475143) << endl;
}
