def format_line(raw_line: str) -> list[int]:
    char_list = []
    for char in raw_line:
        if char.isnumeric():
            char_list.append(char)
    integer_list = []
    integer = ''
    for char in char_list:
        integer += char
        if len(integer) == 2:
            integer = int(integer)
            integer_list.append(integer)
            integer = ''
    return integer_list


def read_data(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        data = f.readlines()
    formated_list = []
    for line in data:
        line = format_line(line)
        if len(line) > 0:
            formated_list.append(line)
    return formated_list


def list_product(list_integers: list[int]) -> int:
    product = 1
    for integer in list_integers:
        product *= integer
    return product


def return_product(
    full_list: list[int],
    cords: tuple[int, int],
    step: int,
) -> bool:
    row_pointer = cords[0]
    element_pointer = cords[1]
    operation = lambda row_fix, column_fix: list_product(
        [
            full_list[row_pointer][element_pointer],
            full_list[row_pointer + row_fix[0]][
                element_pointer + column_fix[0]
            ],
            full_list[row_pointer + row_fix[1]][
                element_pointer + column_fix[1]
            ],
            full_list[row_pointer + row_fix[2]][
                element_pointer + column_fix[2]
            ],
        ]
    )
    products = []
    if element_pointer >= step:
        products.append(operation([0, 0, 0], [-1, -2, -3]))

    if element_pointer + step <= len(full_list[row_pointer]):   # Right
        products.append(operation([0, 0, 0], [1, 2, 3]))

    if row_pointer >= step:   # Up
        products.append(operation([-1, -2, -3], [0, 0, 0]))

    if row_pointer <= len(full_list) - step:   # Down
        products.append(operation([1, 2, 3], [0, 0, 0]))

    if (
        row_pointer <= len(full_list[row_pointer]) - step and element_pointer >= step
    ):   # Down left
        products.append(operation([1, 2, 3], [-1, -2, -3]))
    if (
        row_pointer <= len(full_list[row_pointer]) - step
        and element_pointer <= len(full_list[row_pointer]) - step
    ):   # Down right
        products.append(operation([1, 2, 3], [1, 2, 3]))
    return max(products)


def solve(data: list[int], step: int) -> int:
    products = []
    for row_index in range(len(data)):
        for column_index in range(len(data[row_index])):
            products.extend([return_product(data, (row_index, column_index), step)])

    return max(products)


def main() -> None:
    data = read_data('data.txt')
    print(solve(data, 4))


if __name__ == '__main__':
    main()
