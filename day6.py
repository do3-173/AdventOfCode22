import file_input as fi


def find_marker(line, n):
    for i in range(len(line[0])):
        if len(set(line[0][i:i + n])) == n:
            return i + n


def first_part():
    line = fi.file_input('day6.txt')
    return find_marker(line, 4)


def second_part():
    line = fi.file_input('day6.txt')
    return find_marker(line, 14)


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
