def binary_search(search_list: list[int], value: int) -> tuple[list[int], str]:
    path_to_target: list[int] = []
    low: int = 0
    high: int = len(search_list) - 1

    while low <= high:
        mid: int = (low + high) // 2
        value_at_middle: int = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [], "Value not Found"


print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))
