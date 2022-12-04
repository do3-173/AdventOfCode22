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
        flag_break = False
        for item in backpack[:(len(backpack) - 1) // 2]:
            for item_2 in backpack[(len(backpack) - 1) // 2:]:
                if item == item_2:
                    items.append(item)
                    flag_break = True
                    break
            if flag_break:
                break
    return convert(items)


def second_part():
    array = fi.file_input('day3.txt')
    items = []
    for i in range(0, len(array), 3):
        break_flag = False
        for items_1 in array[i]:
            for items_2 in array[i + 1]:
                if items_1 == items_2:
                    for items_3 in array[i + 2]:
                        if items_3 == items_2:
                            items.append(items_3)
                            break_flag = True
                            break
                if break_flag:
                    break
    return convert(items)


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
