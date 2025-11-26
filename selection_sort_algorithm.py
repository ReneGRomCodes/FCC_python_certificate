def selection_sort(array: list[int]) -> list[int]:
    n: int = len(array)

    for i in range(n - 1):
        min_index: int = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index: int = j

        min_value: int = array.pop(min_index)
        array.insert(i, min_value)

    return array
