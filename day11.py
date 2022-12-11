import re

import numpy as np

from file_input import file_input


def starting_position():
    array = file_input('day11.txt')
    monkeys = []
    monkey_stats = []
    for line in array:
        if len(line.split()) >= 1:
            if line.split()[0] == 'Monkey':
                monkey_stats = [['Monkey', int(re.findall('[0-9]+', line)[0])]]
            if line.split()[0] == 'Starting':
                monkey_stats.append(['Item', [eval(i) for i in re.findall('[0-9]+', line)]])
            if line.split()[0] == 'Operation:':
                monkey_stats.append(['Operation', [line.split()[4], line.split()[5]]])
            if line.split()[0] == 'Test:':
                monkey_stats.append(['Divisible', int(re.findall('[0-9]+', line)[0])])
            if line.split()[0] == 'If':
                if line.split()[1] == 'true:':
                    monkey_stats.append(['True', int(re.findall('[0-9]+', line)[0])])
                if line.split()[1] == 'false:':
                    monkey_stats.append(['False', int(re.findall('[0-9]+', line)[0])])

        else:
            monkeys.append(dict(monkey_stats))
    monkeys.append(dict(monkey_stats))
    return monkeys


def monkey_business(n, divided=True):
    monkeys = starting_position()
    inspected = np.zeros(len(monkeys))
    divisible = [monkey['Divisible'] for monkey in monkeys]
    lcm = np.prod(divisible)
    for _ in range(n):
        for monkey in monkeys:
            inspect = 0
            for _ in range(len(monkey['Item'])):
                item = monkey['Item'].pop(0)
                inspect += 1
                if monkey['Operation'][0] == '*':
                    if monkey['Operation'][1] == 'old':
                        worry = item * item
                    else:
                        worry = item * int(monkey['Operation'][1])
                else:
                    if monkey['Operation'][1] == 'old':
                        worry = item + item
                    else:
                        worry = item + int(monkey['Operation'][1])
                if divided:
                    worry //= 3
                else:
                    worry %= lcm
                if worry % monkey['Divisible'] == 0:
                    monkeys[monkey['True']]['Item'].append(worry)
                else:
                    monkeys[monkey['False']]['Item'].append(worry)
            inspected[monkey['Monkey']] += inspect
    inspected.sort()
    return int(inspected[-2] * inspected[-1])


def first_part():
    return monkey_business(20)


def second_part():
    return monkey_business(10000, divided=False)


def main():
    print(first_part())
    print(second_part())


if __name__ == '__main__':
    main()
