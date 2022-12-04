import file_input as fi


def input_array():
    array_lines = fi.file_input('day2.txt')
    return [x.split() for x in array_lines], 0


def first_part():
    array, sum_points = input_array()
    for game in array:
        sum_points += ord(game[1]) - ord('W') + \
                      ((3 + (ord(game[1]) - ord('X')) -
                        (ord(game[0]) - ord('A'))) % 3 + 1) % 3 * 3

    return sum_points


def second_part():
    array, sum_points = input_array()
    for game in array:
        sum_points += (ord(game[1]) - ord('X')) * 3 + \
                      (ord(game[1]) - ord('X') + ord(game[0]) - ord('A') - 1) % 3 + 1

    return sum_points


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
