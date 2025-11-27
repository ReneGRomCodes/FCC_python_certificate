def dfs(adj_matrix: list[list[int]], node_label: int) -> list[int]:
    n: int = len(adj_matrix)
    if n == 0:
        return []

    visited: list[bool] = [False] * n
    result: list[int] = []
    stack: list[int] = [node_label]

    while stack:
        node: int = stack.pop()

        if visited[node]:
            continue
        visited[node] = True
        result.append(node)

        for neigh in range(0, n):
            if adj_matrix[node][neigh] and not visited[neigh]:
                stack.append(neigh)

    return result
