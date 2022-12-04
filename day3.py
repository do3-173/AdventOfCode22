import file_input as fi


def convert(items):
    sum_items = 0
    for item in items:
        if 'a' <= item <= 'z':
            sum_items += 1 + ord(item) - ord('a')
        else:
            sum_items += 27 + ord(item) - ord('A')
    return sum_items


def first_part():
    array = fi.file_input('day3.txt')
    items = []
    for backpack in array:
        for item in backpack[:(len(backpack) - 1) // 2]:
            if item in backpack[(len(backpack) - 1) // 2:]:
                items.append(item)
                break
    return convert(items)


def second_part():
    array = fi.file_input('day3.txt')
    items = []
    for i in range(0, len(array), 3):
        for item in array[i]:
            if item in array[i+1] and item in array[i+2]:
                items.append(item)
                break
    return convert(items)


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
