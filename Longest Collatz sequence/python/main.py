"""This code solves the 14th challange in projecteuler.net"""


def collatz_sequence_chain(starting_point: int) -> int:
    """
    This function returns the chain size of a collatz sequence
    """
    chain_length = 1
    current_pointer = starting_point
    while current_pointer != 1:
        if current_pointer % 2 == 0:
            current_pointer /= 2
        else:
            current_pointer *= 3
            current_pointer += 1
        chain_length += 1
    return chain_length


def solve(max_starting_point: int) -> int:
    """
    This function executes collatz_sequence_chain() for
    every number from 1 to the max_starting_point specified
    in the problem. Then it returns which starting point
    returned the largest chain.
    """
    longest_chain = 0
    longest_chain_starting_point = 0
    for integer in range(1, max_starting_point):
        current_chain = collatz_sequence_chain(integer)
        if current_chain > longest_chain:
            longest_chain = current_chain
            longest_chain_starting_point = integer
        print(integer)
    return longest_chain_starting_point


if __name__ == '__main__':
    solution = solve(1000000)
    print("The solution is", solution)
