def get_data() -> list[int]:
    with open('./data.txt', 'r') as f:
        data_brute = f.readlines()
    data = []
    for line in data_brute:
        line = line.replace('\n', '')
        for char in line:
            data.append(int(char))
    return data


def get_kernel_product(kernel: list[int]) -> int:
    kernel_product = 1
    for i in kernel:
        kernel_product *= i
    return kernel_product


def solve(data: list[int], kernel_size: int) -> int:
    total_products = []
    pointer_kernel_start = 0
    pointer_kernel_end = kernel_size
    while pointer_kernel_end < len(data):
        kernel = data[pointer_kernel_start:pointer_kernel_end]
        total_products.append(get_kernel_product(kernel))
        pointer_kernel_start += 1
        pointer_kernel_end += 1
    return max(total_products)


def get_answers() -> None:
    data = get_data()
    a1 = solve(data, 4)
    a2 = solve(data, 13)
    print(f'First answer = {a1}')
    print(f'Second answer = {a2}')


if __name__ == '__main__':
    get_answers()
