def readfile(filename):
    result = []
    file = open(filename, 'r')
    content = file.readlines()
    for line in content:
        result.append([int(t) for t in line.split()])
    file.close()
    return result


def dxy_array(i, j, n):
    result = []
    if i - 1 >= 0:
        result.append((-1, 0))
    if i + 1 < n:
        result.append((1, 0))
    if j - 1 >= 0:
        result.append((0, -1))
    if j + 1 < n:
        result.append((0, 1))
    return result


def check_point(values, visites, i, j, cells):
    visites[i][j] = True
    cells.append((i, j))
    dxy_values = dxy_array(i, j, len(values))
    for dx, dy in dxy_values:
        new_i = i + dx
        new_j = j + dy
        if values[new_i][new_j] == 1 and visites[new_i][new_j] == False:
            check_point(values, visites, new_i, new_j, cells)


# square = 1, cirlce = 0
def check_square_or_circle(n, sqrt_values):
    if n == 1:
        return False
    for i in range(len(sqrt_values)):
        if sqrt_values[i] == n:
            return True
    return False


def main():
    values = readfile('input.txt')
    visites = [[False] * len(values) for _ in range(len(values))]
    sqrt_values = [n * n for n in range(len(values))]
    square = 0
    circle = 0
    for i in range(len(values)):
        for j in range(len(values[i])):
            if values[i][j] == 1 and visites[i][j] == False:
                cells = []
                check_point(values, visites, i, j, cells)
                if check_square_or_circle(len(cells), sqrt_values):
                    square += 1
                else:
                    circle += 1
            else:
                continue

    print(square, circle)

if __name__ == '__main__':
    main()
