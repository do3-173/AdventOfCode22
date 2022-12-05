from file_input import file_input
import re


def input_array():
    # Add starting position algorithm
    input_array_stacks = [['D', 'B', 'V', 'J'],
                          ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
                          ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
                          ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
                          ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
                          ['R', 'D', 'B', 'S', 'N', 'G'],
                          ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
                          ['W', 'L', 'F'],
                          ['S', 'V', 'F', 'M', 'R']]
    array = file_input('day5.txt')
    number_of_crates = []
    from_stack = []
    to_stack = []
    for i in range(len(array)):
        numbers = re.findall('[0-9]+', array[i])
        number_of_crates.append(int(numbers[0]))
        from_stack.append(int(numbers[1]) - 1)
        to_stack.append(int(numbers[2]) - 1)

    return input_array_stacks, number_of_crates, from_stack, to_stack


def first_part():
    input_array_stacks, number_of_crates, from_stack, to_stack = input_array()

    for i in range(len(number_of_crates)):
        for k in range(number_of_crates[i]):
            input_array_stacks[to_stack[i]].append(input_array_stacks[from_stack[i]].pop())

    final_message = ''
    for stack in input_array_stacks:
        final_message += stack.pop()

    return final_message


def second_part():
    input_array_stacks, number_of_crates, from_stack, to_stack = input_array()

    for i in range(len(number_of_crates)):
        temp = []
        for k in range(number_of_crates[i]):
            temp.append(input_array_stacks[from_stack[i]].pop())
        for k in range(number_of_crates[i]):
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
