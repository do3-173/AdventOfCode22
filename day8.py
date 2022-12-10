import numpy
import numpy as np

from file_input import file_input


def input_matrix():
    array = file_input('day8.txt')
    matrix = []
    for row in array:
        matrix.append([int(d) for d in str(row) if d != '\n'])
    return matrix


def first_part_check(matrix, i, j, max_height):
    if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1 or matrix[i][j] > max_height:
        return True
    return False


def first_part():
    matrix = input_matrix()
    flag_matrix = np.zeros(shape=(len(matrix), len(matrix[0])))
    for i in range(len(matrix)):
        max_left = -1
        for j in range(len(matrix[0])):
            if first_part_check(matrix, i, j, max_left):
                flag_matrix[i][j] = 1
                max_left = matrix[i][j]
        max_right = -1
        for j in range(len(matrix[0]) - 1, 0, -1):
            if first_part_check(matrix, i, j, max_right):
                flag_matrix[i][j] = 1
                max_right = matrix[i][j]
    for j in range(len(matrix[0])):
        max_bottom = -1
        for i in range(len(matrix)):
            if first_part_check(matrix, i, j, max_bottom):
                flag_matrix[i][j] = 1
                max_bottom = matrix[i][j]
        max_top = -1
        for i in range(len(matrix) - 1, 0, -1):
            if first_part_check(matrix, i, j, max_top):
                flag_matrix[i][j] = 1
                max_top = matrix[i][j]
    return numpy.count_nonzero(flag_matrix)


def second_part():
    matrix = input_matrix()
    scenic_matrix = np.zeros(shape=np.shape(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            scenic_left = 0
            for k in range(j + 1, len(matrix[0])):
                if matrix[i][j] <= matrix[i][k]:
                    scenic_left += 1
                    break
                else:
                    scenic_left += 1
            scenic_right = 0
            for k in range(j - 1, -1, -1):
                if matrix[i][j] <= matrix[i][k]:
                    scenic_right += 1
                    break
                else:
                    scenic_right += 1
            scenic_bottom = 0
            for k in range(i + 1, len(matrix)):
                if matrix[i][j] <= matrix[k][j]:
                    scenic_bottom += 1
                    break
                else:
                    scenic_bottom += 1
            scenic_top = 0
            for k in range(i - 1, -1, -1):
                if matrix[i][j] <= matrix[k][j]:
                    scenic_top += 1
                    break
                else:
                    scenic_top += 1

            scenic_matrix[i][j] = scenic_top * scenic_bottom * scenic_right * scenic_left
    return int(np.max(scenic_matrix))


def main():
    print(first_part())
    print(second_part())


if __name__ == '__main__':
    main()
