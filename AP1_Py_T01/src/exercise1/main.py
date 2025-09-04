def get_vectors():
    result = []
    input_str = input().split()
    for i in range(3):
        result.append(float(input_str[i]))
    return result


def main():
    vectors_1 = get_vectors()
    vectors_2 = get_vectors()
    sum = 0.0
    for i in range(len(vectors_1)):
        sum += vectors_1[i] * vectors_2[i]
    print(sum)


if __name__ == '__main__':
    main()
