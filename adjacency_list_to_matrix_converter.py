def adjacency_list_to_matrix(adj_list):
    adj_matrix = []
    n_rows = len(adj_list)

    try:
        n_columns = max(max(v) for v in adj_list.values()) + 1
    except ValueError:
        n_columns = n_rows

    for _ in range(n_rows):
        adj_matrix.append([0] * n_columns)

    for k, v in adj_list.items():
        for i in v:
            adj_matrix[k][i] = 1

    print(row for row in adj_matrix)

    return adj_matrix
