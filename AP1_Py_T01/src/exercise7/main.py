def create_money_filed(field):
    rows = len(field)
    cols = len(field[0])
    result = [[0] * cols for _ in range(rows)]
    result[0][0] = field[0][0]
    for i in range(1, rows):
        result[i][0] = field[i][0] + result[i - 1][0]

    for j in range(1, cols):
        result[0][j] = field[0][j] + result[0][j - 1]

    for i in range(1, rows):
        for j in range(1, cols):
            result[i][j] = field[i][j] + max(result[i][j - 1], result[i - 1][j])

    return result


def get_field_values():
    result = []
    N, M = (int(i) for i in input().split())
    for i in range(N):
        result.append(list(int(i) for i in input().split()))
    return result


def main():
    field = get_field_values()
    money_field = create_money_filed(field)
    print(money_field[len(field) - 1][len(field[0]) - 1])


if __name__ == '__main__':
    main()
