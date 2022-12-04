import file_input as fi


def input_array():
    array = fi.file_input('day4.txt')
    overlapped = 0
    return_array = []
    for pair in array:
        x = pair.split(',')
        x1 = [eval(i) for i in x[0].split('-')]
        x2 = [eval(i) for i in x[1].split('-')]
        return_array.append([x1, x2])
    return return_array, overlapped


def first_part():
    array, overlapped = input_array()
    for x1, x2 in array:
        if x1[0] <= x2[0] and x1[1] >= x2[1] or \
                x1[0] >= x2[0] and x1[1] <= x2[1]:
            overlapped += 1

    return overlapped


def second_part():
    array, overlapped = input_array()
    for x1, x2 in array:
        if (x1[0] <= x2[0] <= x1[1]) or \
                (x1[0] <= x2[1] <= x1[1]) or \
                (x2[0] <= x1[0] <= x2[1]) or \
                (x2[0] <= x1[1] <= x2[1]):
            overlapped += 1

    return overlapped


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
