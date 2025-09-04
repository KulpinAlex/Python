def check_palindrome(value: int):
    if value < 0:
        return False
    value_list = []
    while value != 0:
        value_list.append(value % 10)
        value //= 10
    for i in range(int(len(value_list) / 2)):
        if value_list[i] != value_list[len(value_list) - i - 1]:
            return False
    return True


def main():
    value = int(input())
    print(type(value))
    print(check_palindrome(value))


if __name__ == '__main__':
    main()
