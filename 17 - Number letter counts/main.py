"""
This is the python code for the 17th challange in projecteuler.com
Definitely not my cleanest code.
"""

from dictionary import NumbersInWords

dic = NumbersInWords().num2words


def mount_number_in_words(number: int) -> int:
    """
    This function takes a integer in the (0,1000) range as it's input
    and returns the length of this number written in words.
    """
    number_in_words = ''
    separated_number = list(str(number))
    if len(separated_number) == 1:
        number_in_words += dic[int(separated_number[0])]

    if len(separated_number) == 2:
        if int(separated_number[0]) >= 2:
            number_in_words += dic[int(separated_number[0] + '0')]
            if separated_number[1] != '0':
                number_in_words += dic[int(separated_number[1])]
        else:
            number_in_words += dic[
                int(separated_number[0] + separated_number[1])
            ]

    if len(separated_number) == 3:
        number_in_words += f'{dic[int(separated_number[0])]} hundred'
        if separated_number[1] != '0' and int(separated_number[1]) >= 2:
            number_in_words += f" and {dic[int(separated_number[1] + '0')]} "
            if separated_number[2] != '0':
                number_in_words += dic[int(separated_number[2])]
        if separated_number[1] == '1':
            number_in_words += (
                f' and {dic[int(separated_number[1] + separated_number[2])]} '
            )
        if separated_number[1] == '0' and separated_number[2] != '0':
            number_in_words += f' and {dic[int(separated_number[2])]} '

    if len(separated_number) == 4:
        number_in_words += 'one thousand'

    return len(number_in_words.replace(' ', ''))


def solve(limit: int) -> int:
    """
    This function uses mount_number_in_words for all the numbers
    in a 1 to 1001 range and returns sum the function outputs.
    """
    sum_of_letters = 0
    for number in range(1, limit + 1):
        sum_of_letters += mount_number_in_words(number)
    return sum_of_letters


if __name__ == '__main__':
    print(solve(1000))
