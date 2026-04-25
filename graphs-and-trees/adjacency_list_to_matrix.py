def adjacency_list_to_matrix(adjacency_list: dict):
    n = len(adjacency_list)
    matrix = [[0] * n for _ in range(n)]

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    for row in matrix:
        print(row)

    return matrix

if __name__ == '__main__':
    print('Test 1:')
    adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})

    print()

    print('Test 2:')
    list1 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [2]
    }
    adjacency_list_to_matrix(list1)