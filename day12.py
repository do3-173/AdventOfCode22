from dijkstar import Graph, find_path

from file_input import file_input


def check_compatibility(first, second):
    if second == 'S':
        return False
    if first == 'S':
        return second == 'a'
    if second == 'E':
        return first == 'z'
    if ord(second) - ord(first) <= 1:
        return True
    return False


def make_graph(second_part_flag=False):
    array = file_input('day12.txt')
    array_split = []
    for line in array:
        array_split.append(line.split()[0])
    graph = Graph()
    starting_position = []
    end_x, end_y = 0, 0
    for i in range(len(array_split)):
        for j in range(len(array_split[i])):
            if array_split[i][j] == 'S':
                starting_position.append((i, j))
            if second_part_flag:
                if array_split[i][j] == 'a':
                    starting_position.append((i, j))
            if array_split[i][j] == 'E':
                end_x, end_y = i, j
            if i > 0:
                if check_compatibility(array_split[i][j], array_split[i - 1][j]):
                    graph.add_edge((i, j), (i - 1, j), 0)
            if i < len(array_split) - 1:
                if check_compatibility(array_split[i][j], array_split[i + 1][j]):
                    graph.add_edge((i, j), (i + 1, j), 0)
            if j > 0:
                if check_compatibility(array_split[i][j], array_split[i][j - 1]):
                    graph.add_edge((i, j), (i, j - 1), 0)
            if j < len(array_split[i]) - 1:
                if check_compatibility(array_split[i][j], array_split[i][j + 1]):
                    graph.add_edge((i, j), (i, j + 1), 0)
    return graph, starting_position, (end_x, end_y)


def first_part():
    graph, starting_position, destination = make_graph()
    nodes, _, _, _ = find_path(graph, starting_position[0], destination)
    return len(nodes) - 1


def second_part():
    graph, starting_position, destination = make_graph(second_part_flag=True)
    path = []
    for start in starting_position:
        try:
            nodes, _, _, _ = find_path(graph, start, destination)
            path.append(len(nodes) - 1)
        finally:
            continue
    return min(path)


def main():
    print(first_part())
    print(second_part())


if __name__ == '__main__':
    main()
