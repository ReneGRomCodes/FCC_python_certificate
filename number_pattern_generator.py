def number_pattern(n: int) -> str:
    """Generate an increasing number pattern from 1 to n.
    ARGS:
        n (int): The upper limit of the pattern. Must be a positive integer.
    RETURNS:
        str: A space-separated string of numbers from 1 to n. Returns an error message if n is not a valid integer or
        is < 1.
    """
    pattern: str = ""

    # Validate type
    if not isinstance(n, int):
        return "Argument must be an integer value."
    # Validate value
    elif n < 1:
        return "Argument must be an integer greater than 0."

    # Build the pattern using a for loop as required
    for i in range(1, n + 1):
        pattern += f"{i} "

    # Remove trailing space before returning
    return pattern.rstrip()
