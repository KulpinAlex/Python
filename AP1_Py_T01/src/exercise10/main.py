def main():
    dict_input = {}
    try:
        n, time = (int(i) for i in input().split())
        if n < 2 or time < 1:
            print("Invalid input")
            return

        for _ in range(n):
            year, price, work_time = (int(i) for i in input().split())
            if year < 1 or price < 1 or work_time < 1:
                print("Invalid input")
                return
            if year not in dict_input.keys():
                dict_input[year] = {}

            if work_time in dict_input[year].keys():
                dict_input[year][work_time] = min(price, dict_input[year][work_time])
            else:
                dict_input[year][work_time] = price
        min_total_cost = float('inf')
        for year in dict_input.keys():
            if len(dict_input[year]) < 2:
                continue
            else:
                for work_time1 in dict_input[year].keys():
                    for work_time2 in dict_input[year].keys():
                        if work_time1 != work_time2 and work_time1 + work_time2 >= time:
                            if dict_input[year][work_time1] + dict_input[year][work_time2] < min_total_cost:
                                min_total_cost = dict_input[year][work_time1] + dict_input[year][work_time2]
        print(min_total_cost)
    except ValueError:
        print("Error input")


if __name__ == '__main__':
    main()
