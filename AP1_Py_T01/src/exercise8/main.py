def main():
    value_number = int(input())
    values = set()
    for _ in range(value_number):
        values.add(int(input()))
    print(len(values))



if __name__ =='__main__':
    main()