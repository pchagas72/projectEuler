"""This code solves the 13th challange in projecteuler.net"""


def read_data(file_name: str) -> list[int]:
    """
    This function takes a .txt with integers and returns them in groups
    of 50 digit integers.
    """
    with open(file_name, 'r', encoding="UTF-8") as file_object:
        data = file_object.readlines()
    counter = 0
    return_list = []
    placeholder = ''
    for line in data:
        for char in line:
            if char == '\n':
                continue
            placeholder += char
            counter += 1
            if counter >= 50:
                return_list.append(int(placeholder))
                placeholder = ''
                counter = 0
    return return_list


def solve(fifty_digit_numbers: list[int]) -> int:
    """
    This function returns the first ten digits of a sum of a list of numbers
    """
    sigma = 0
    for number in fifty_digit_numbers:
        sigma += number
    return int(str(sigma)[0:10])


if __name__ == '__main__':
    x = read_data('data.txt')
    print('The answer is',solve(x))
