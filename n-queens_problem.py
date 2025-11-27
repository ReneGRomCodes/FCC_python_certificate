def dfs_n_queens(n: int) -> list[int]:
    if n < 1:
        return []

    solutions: list[int] = []
    # Track used columns and diagonals for O(1) conflict checks
    cols: set = set()               # columns already occupied
    diag_1: set = set()             # (row - col) for occupied major diagonals
    diag_2: set = set()             # (row + col) for occupied minor diagonals
    board: list[int] = [-1] * n     # board[row] = col

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if col in cols or (row - col) in diag_1 or (row + col) in diag_2:
                continue

            # place queen
            cols.add(col)
            diag_1.add(row - col)
            diag_2.add(row + col)
            board[row] = col

            backtrack(row + 1)

            # remove queen (backtrack)
            cols.remove(col)
            diag_1.remove(row - col)
            diag_2.remove(row + col)
            board[row] = -1

    backtrack(0)
    return solutions
