def int_part(value: str):
    sum = 0.0
    for ch in value:
        if ord('0') <= ord(ch) <= ord('9'):
            sum = sum * 10 + ord(ch) - ord('0')

    return sum


def fractional_part(value: str):
    sum = 0.0
    for i in range(len(value) - 1, -1, -1):
        if ord('0') <= ord(value[i]) <= ord('9'):
            sum = sum / 10 + (ord(value[i]) - ord('0')) / 10

    return sum


def str_to_float(value: str):
    sum = 0.0
    negative = 1
    if value[0] == '-':
        negative = -1
        value = value[1:]
    split = value.split('.')
    if len(split) == 1:
        sum = int_part(split[0])
    else:
        sum = int_part(split[0]) + fractional_part(split[1])

    return sum * negative


def check_split(value: str):
    if value[0] == '-':
        if len(value) > 1:
            value = value[1:]
        else:
            return False

    for ch in value:
        if ord('0') > ord(ch) or ord(ch) > ord('9'):
            return False

    return True


def check_str(value: str):
    split = value.split('.')
    for line in split:
        if len(line) == 0:
            return False
    if len(split) > 2:
        return False
    elif len(split) == 1:
        return check_split(value)
    else:
        return check_split(split[0]) and check_split(split[1])


def main():
    string_number = input()
    if check_str(string_number):
        number = str_to_float(string_number) * 2
        print('%.3f' % number)
    else:
        print('Error, input is incorrect')


if __name__ == '__main__':
    main()
