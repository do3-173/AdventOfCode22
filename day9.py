from file_input import file_input


def rope_movement(n):
    array = file_input('day9.txt')
    rope = []
    [rope.append([0, 0]) for _ in range(n + 1)]
    visited = [(0, 0)]
    for move in array:
        for _ in range(int(move.split()[1])):
            if move.split()[0] == 'R':
                rope[0][0] += 1
            elif move.split()[0] == 'L':
                rope[0][0] -= 1
            elif move.split()[0] == 'U':
                rope[0][1] += 1
            elif move.split()[0] == 'D':
                rope[0][1] -= 1
            for i in range(len(rope) - 1):
                delta_xy = [x - y for x, y in zip(rope[i], rope[i + 1])]
                if abs(delta_xy[0]) > 1 or abs(delta_xy[1]) > 1:
                    if delta_xy[0] >= 1:
                        rope[i + 1][0] += 1
                    if delta_xy[0] <= -1:
                        rope[i + 1][0] -= 1
                    if delta_xy[1] >= 1:
                        rope[i + 1][1] += 1
                    if delta_xy[1] <= -1:
                        rope[i + 1][1] -= 1
            visited.append((rope[len(rope) - 1][0], rope[len(rope) - 1][1]))
    return len(set(tuple(visited)))


def first_part():
    return rope_movement(1)


def second_part():
    return rope_movement(9)


def main():
    print(first_part())
    print(second_part())


if __name__ == '__main__':
    main()
