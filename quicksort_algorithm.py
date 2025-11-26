def quick_sort(sequence: list[int]) -> list[int]:
    if len(sequence) <= 1:
        return sequence

    pivot: int = sequence[0]

    less_than_pivot: list[int] = [i for i in sequence if i < pivot]
    equal_to_pivot: list[int] = [i for i in sequence if i == pivot]
    higher_than_pivot: list[int] = [i for i in sequence if i > pivot]

    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(higher_than_pivot)
