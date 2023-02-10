"""This code solves the 13th challange in projecteuler.net"""


def read_data(file_name: str) -> list[int]:
    """
    This function takes a .txt with integers and returns them in groups
    of 50 digit integers.
    """
    with open(file_name, 'r', encoding='UTF-8') as file_object:
        data = file_object.read()
    all_numbers_list = [number for number in data if number.isnumeric()]
    return_list = []
    fifty_digit_number_placeholder = ''
    for number in all_numbers_list:
        fifty_digit_number_placeholder += number
        if len(fifty_digit_number_placeholder) >= 50:
            return_list.append(int(fifty_digit_number_placeholder))
            fifty_digit_number_placeholder = ''
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
    print(solve(read_data('data.txt')))
