def gen_parentheses(pairs: int) -> str | list[str]:
    if not isinstance(pairs, int):
        return "The number of pairs should be an integer"
    if pairs < 1:
        return "The number of pairs should be at least 1"

    queue: list[tuple[str, int, int]] = [("", 0, 0)]
    result: list[str] = []
    while queue:
        current, opens_used, closes_used = queue.pop(0)
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            if opens_used < pairs:
                queue.append((current + "(", opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ")", opens_used, closes_used + 1))

    return result


print(gen_parentheses(2))
print(gen_parentheses(3))
