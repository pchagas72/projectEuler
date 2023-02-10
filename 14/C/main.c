#include <stdio.h>

int collatz_sequence_chain(long starting_point){
    int chain_length = 1;
    long current_point = starting_point;
    while (current_point != 1) {
        if (current_point % 2 == 0){
            current_point /= 2;
        }
        else{
            current_point *= 3;
            current_point++;
        }
        chain_length += 1;
    }
    return chain_length;
}

long solve(long max_starting_point){
    long longest_chain_starting_point;
    int longest_chain;
    int current_chain;
    for (long i = 1; i <= max_starting_point; i++){
        current_chain = collatz_sequence_chain(i);
        if (current_chain > longest_chain){
            longest_chain = current_chain;
            longest_chain_starting_point = i;
        }
    }
    return longest_chain_starting_point;
}

int main(){
    int solution = solve(1000000);
    printf("The solution is = %d\n", solution);

}