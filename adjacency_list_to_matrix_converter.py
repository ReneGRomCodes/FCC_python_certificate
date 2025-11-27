def adjacency_list_to_matrix(adj_list: dict[int, list[int]]) -> list[list[int]]:
    adj_matrix: list[list[int]] = []
    n_rows: int = len(adj_list)

    try:
        n_columns: int = max(max(v) for v in adj_list.values()) + 1
    except ValueError:
        n_columns: int = n_rows

    for _ in range(n_rows):
        adj_matrix.append([0] * n_columns)

    for k, v in adj_list.items():
        for i in v:
            adj_matrix[k][i]: int = 1

    print(row for row in adj_matrix)

    return adj_matrix
