def dfs(adjacency_matrix, node_label):

    visited = []
    stack = [node_label]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbor, is_connected in enumerate(adjacency_matrix[current_node]):
                if is_connected == 1:
                    stack.append(neighbor)

    return visited



if __name__ == '__main__':
    print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))