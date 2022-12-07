from file_input import file_input

THRESHOLD_TOTAL_SIZE = 100000
FILESYSTEM_SIZE = 70000000
UNUSED_SPACE = 30000000


def input_array():
    array = file_input('day7.txt')
    current_directory = []
    files_in_directory = []
    for i in range(len(array)):
        x = array[i].split()
        if x[1] == "cd":
            if x[2] == "..":
                current_directory.pop()
            else:
                current_directory.append(x[2])
        if x[1] == "ls":
            files = []
            if i < len(array):
                i += 1
                x = array[i].split()
                while x[0] != '$' and i < len(array) - 1:
                    files.append([x[1], x[0]])
                    i += 1
                    x = array[i].split()
                files_in_directory.append([tuple(current_directory), files])

    sum_directory = []
    size_taken = 0
    for files in files_in_directory:
        sum_size = 0
        for file in files[1]:
            if file[1] != 'dir':
                sum_size += int(file[1])
        size_taken += sum_size
        sum_directory.append([tuple(files[0]), sum_size])

    for i in range(len(sum_directory)):
        sum_size = 0
        for j in range(i + 1, len(sum_directory)):
            if len(sum_directory[i][0]) < len(sum_directory[j][0]):
                for k in range(len(sum_directory[i][0])):
                    if sum_directory[i][0][k] != sum_directory[j][0][k]:
                        break
                    elif k == len(sum_directory[i][0]) - 1:
                        sum_size += sum_directory[j][1]
        sum_directory[i][1] += sum_size

    return sum_directory, size_taken


def first_part():
    sum_directory, _ = input_array()
    return_sum = 0
    for i in range(len(sum_directory)):
        if sum_directory[i][1] < THRESHOLD_TOTAL_SIZE:
            return_sum += sum_directory[i][1]
    return return_sum


def second_part():
    sum_directory, sum_size = input_array()
    space_needed = abs(FILESYSTEM_SIZE - sum_size - UNUSED_SPACE)
    sum_directory.sort(key=lambda x: x[1])
    for i in range(len(sum_directory)):
        if sum_directory[i][1] > space_needed:
            return sum_directory[i][1]


def main():
    print(first_part())
    print(second_part())


if __name__ == '__main__':
    main()
