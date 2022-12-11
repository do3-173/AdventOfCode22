from file_input import file_input


def first_part():
    array = file_input('day10.txt')
    cycle = 1
    value = 1
    signal = 0
    for command in array:
        if 220 >= cycle >= 20 and (cycle - 20) % 40 == 0:
            signal += cycle * value
        if command.split()[0] == 'addx':
            cycle += 1
            if 220 >= cycle >= 20 and (cycle - 20) % 40 == 0:
                signal += cycle * value
            cycle += 1
            value += int(command.split()[1])
        else:
            cycle += 1
    return signal


def second_part():
    array = file_input('day10.txt')
    cycle = 1
    crt_row = '#'
    sprite = '###.....................................'
    for command in array:
        if cycle % 40 == 0:
            print(crt_row[:-1])
            crt_row = ''
        if command.split()[0] == 'addx':
            cycle += 1
            crt_row += sprite[(cycle - 1) % 40]
            if cycle % 40 == 0:
                print(crt_row[:-1])
                crt_row = ''
            value = int(command.split()[1])
            sprite = sprite[-value:] + sprite[:-value]
            cycle += 1
            crt_row += sprite[(cycle - 1) % 40]
        else:
            cycle += 1
            crt_row += sprite[(cycle - 1) % 40]


def main():
    print(first_part())
    second_part()


if __name__ == '__main__':
    main()
