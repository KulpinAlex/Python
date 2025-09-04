import json


def read_file(filename):
    with open(filename) as file:
        try:
            data = json.load(file)
            if len(data) != 2:
                print("Error, should be two lists")
            else:
                return [data[x] for x in data.keys()]
            print("ok")
        except json.decoder.JSONDecodeError:
            print('JSON Decode Error')


def check_list_data(values):
    last_year = 0
    for item in values:
        if 'year' not in item.keys():
            return False
        if last_year > item['year'] > 0:
            return False
        last_year = item['year']
    return True


def sort_lists(list1, list2):
    merged_lists = []
    i, j = 0, 0
    while len(list1) > i and len(list2) > j:
        if list1[i]['year'] > list2[j]['year']:
            merged_lists.append(list2[j])
            j += 1
        else:
            merged_lists.append(list1[i])
            i += 1
    merged_lists.extend(list2[j:])
    merged_lists.extend(list1[i:])
    return merged_lists


def main():
    file = 'input.txt'
    list1, list2 = read_file(file)
    if check_list_data(list1) and check_list_data(list2):
        merged_list = sort_lists(list1, list2)
        print(json.dumps(merged_list, indent=4))
    else:
        print("Error, JSON Data Error")


if __name__ == '__main__':
    main()
