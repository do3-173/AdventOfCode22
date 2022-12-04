import file_input as fi


def sum_calories():
    array = fi.file_input('day1.txt')
    sum_cal = 0
    sum_array = []
    for i in range(len(array)):
        if array[i][0] == '\n':
            sum_array.append(sum_cal)
            sum_cal = 0
        else:
            sum_cal += int(array[i][:-1])
    return sum_array


def first_part():
    return max(sum_calories())


def second_part():
    array = sorted(sum_calories())
    return sum(array[-3:])


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
