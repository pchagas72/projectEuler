"""This is the python code for the 18th challange in projecteuler.com"""


def read_data(filename: str) -> list[list[int]]:
    """
    This function reads the triangle.txt file, the file has the triangle
    provided in the challange, of course. It reads the rows and returns
    them in lists populated by integers.
    """
    with open(filename, 'r', encoding='UTF-8') as file_reader:
        triangle = file_reader.readlines()
    triangle_str = [number.replace('\n', '').split() for number in triangle]
    triangle_int = []
    for row in triangle_str:
        row_int = []
        for element in row:
            row_int.append(int(element))
        triangle_int.append(row_int)
    return triangle_int


def solve(reversed_triangle: list[int]) -> int:
    """
    This function takes the reversed triangle as input
    and then it adds the biggest value on the row above.
    """
    return_value = 0
    for row in range(1, len(reversed_triangle)):
        for index, integer in enumerate(reversed_triangle[row]):
            reversed_triangle[row][index] = integer + max(
                reversed_triangle[row - 1][index],
                reversed_triangle[row - 1][index + 1],
            )
            return_value = reversed_triangle[row][index]
    return return_value


if __name__ == '__main__':
    triangle_data = read_data('triangle.txt')
    triangle_data.reverse()
    print(solve(triangle_data))
