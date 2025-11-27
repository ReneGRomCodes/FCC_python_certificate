def hanoi_solver(n: int) -> str:
    # Initialize the rods.
    rods: list[list[int]] = [list(range(n, 0, -1)), [], []]  # [source, auxiliary, target].
    result: list[str] = []

    def move(num_disks: int, start: int, aux: int, end: int) -> None:
        if num_disks == 0:
            return
        # Move n-1 disks from start to aux using end.
        move(num_disks - 1, start, end, aux)
        # Move the nth disk from start to end.
        disk = rods[start].pop()
        rods[end].append(disk)
        # Record the state of the rods.
        result.append(f"{rods[0]} {rods[1]} {rods[2]}")
        # Move n-1 disks from aux to end using start.
        move(num_disks - 1, aux, start, end)

    # Record initial state.
    result.append(f"{rods[0]} {rods[1]} {rods[2]}")
    move(n, 0, 1, 2)

    return "\n".join(result)
