def create_array(n, arr):
    result = []

    if len(arr) == 0:
        return [1]

    for i in range(n):
        if i == 0:
            result.append(1)
        elif i < len(arr):
            result.append(arr[i - 1] + arr[i])
        else:
            result.append(1)

    return result


def print_array(new_arr):
    for i in new_arr:
        print(i, " ", end="")
    print()


def main():
    n = 0
    try:
        n = int(input())
    except ValueError:
        print_array("Natural number was expected")

    old_arr = []

    for i in range(n):
        new_arr = create_array(i + 1, old_arr)
        old_arr = new_arr
        print_array(new_arr)


if __name__ == '__main__':
    main()
