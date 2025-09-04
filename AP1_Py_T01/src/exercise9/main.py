def main():
    line = input().split()
    n = int(line[0])
    point = float(line[1])
    result = 0.0
    for i in range(n):
        value = float(input())
        result += value * (n - i) * (point ** (n - i - 1))
    input()
    print("%.3f" % result)


if __name__ == '__main__':
    main()
