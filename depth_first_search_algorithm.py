def dfs(adj_matrix, node_label):
    n = len(adj_matrix)
    if n == 0:
        return []

    visited = [False] * n
    result = []
    stack = [node_label]

    while stack:
        node = stack.pop()

        if visited[node]:
            continue
        visited[node] = True
        result.append(node)

        for neigh in range(0, n):
            if adj_matrix[node][neigh] and not visited[neigh]:
                stack.append(neigh)

    return result
