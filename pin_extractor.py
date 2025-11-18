def pin_extractor(poems: list[str]) -> list[str]:
    """Extract hidden PIN codes from a list of poems.
    Each poem is processed line by line. For line *i*, the function looks for
    the *i*-th word (0-indexed). The digit added to the PIN is the length of
    that word. If the line has fewer than (i + 1) words, a '0' is added instead.

    ARGS:
        poems (list[str]): A list of poem strings, each containing multiple lines.
    RETURNS:
        list[str]: A list of extracted PIN codes, one for each poem.
    """
    secret_codes = []

    for poem in poems:
        secret_code = ""
        lines = poem.split("\n")

        # Walk through each line and grab the word that matches the line index
        for line_index, line in enumerate(lines):
            words = line.split()

            # If the word exists, take its length; otherwise use '0'
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"

        secret_codes.append(secret_code)

    return secret_codes
