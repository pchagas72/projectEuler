def reverse_string(produto) -> str :
    string = str(produto)
    newString = ""
    for i in range(len(string)):
        newString += string[len(string)-i-1]
    return newString

def check_palindrom(produto) -> bool :
    return str(produto) == reverse_string(produto)

def helper(produto, largest) -> int :
    if not check_palindrom(produto) :
        return largest
    if produto >= largest :
        return produto
    return largest

def solve() -> int :
    largest = 0
    for i in range(100, 1000):
        for k in range(100, 1000):
            produto = i * k
            largest = helper(produto, largest)

    return largest

def main() -> None :
    print(solve())


if __name__ == "__main__" :
          main()
