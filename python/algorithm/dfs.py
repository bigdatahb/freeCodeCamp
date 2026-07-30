def dfs(adj_matrix, node_no):
    node_number = len(adj_matrix)
    stack = [node_no]
    visited = [node_no]
    while stack:
        print(stack)
        current_node = stack.pop()
        adj_nodes = [i for (i, n) in enumerate(adj_matrix[current_node]) if n == 1 and i != current_node]
        print(adj_nodes)
        new_nodes = [n for n in adj_nodes if n not in visited]
        stack.extend(new_nodes)
        visited.extend(new_nodes)

    return visited

dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)
