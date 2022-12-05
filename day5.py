from file_input import file_input
import re


def input_array():
    array = file_input('day5.txt')
    setup = move_array = []
    for i in range(len(array)):
        if array[i] == '\n':
            setup = array[:i]
            move_array = array[i + 1:]
            break
    number_of_stacks = int(max(re.findall('[0-9]+', setup[len(setup) - 1])))
    input_array_stacks = []
    for i in range(number_of_stacks):
        input_array_stacks.append([])
    for i in range(len(setup) - 2, -1, -1):
        for j in range(1, len(setup[0]), 4):
            if setup[i][j] != ' ':
                input_array_stacks[j // 4].append(setup[i][j])

    number_of_crates = []
    from_stack = []
    to_stack = []
    for i in range(len(move_array)):
        numbers = re.findall('[0-9]+', move_array[i])
        number_of_crates.append(int(numbers[0]))
        from_stack.append(int(numbers[1]) - 1)
        to_stack.append(int(numbers[2]) - 1)

    return input_array_stacks, number_of_crates, from_stack, to_stack


def first_part():
    input_array_stacks, number_of_crates, from_stack, to_stack = input_array()

    for i in range(len(number_of_crates)):
        for _ in range(number_of_crates[i]):
            input_array_stacks[to_stack[i]].append(input_array_stacks[from_stack[i]].pop())

    final_message = ''
    for stack in input_array_stacks:
        final_message += stack.pop()

    return final_message


def second_part():
    input_array_stacks, number_of_crates, from_stack, to_stack = input_array()

    for i in range(len(number_of_crates)):
        temp = []
        for _ in range(number_of_crates[i]):
            temp.append(input_array_stacks[from_stack[i]].pop())
        for _ in range(number_of_crates[i]):
            input_array_stacks[to_stack[i]].append(temp.pop())

    final_message = ''
    for stack in input_array_stacks:
        final_message += stack.pop()

    return final_message


def main():
    print(first_part())
    print(second_part())


if __name__ == "__main__":
    main()
