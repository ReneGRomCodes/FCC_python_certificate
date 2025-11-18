FULL_DOT = '●'
EMPTY_DOT = '○'


def create_character(name: str, strength: int, intelligence: int, charisma: int) -> str:
    """Build and return string representing passed character."""
    stats: tuple[int, ...] = (strength, intelligence, charisma)

    # Validate name requirements.
    if not isinstance(name, str):
        return "The character name should be a string"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"

    # Validate stat requirements.
    for stat in stats:
        if not isinstance(stat, int):
            return "All stats should be integers"
        elif stat < 1:
            return "All stats should be no less than 1"
        elif stat > 4:
            return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Build return string.
    character: str = (f"{name}\n"
                      f"STR: {FULL_DOT * strength}{EMPTY_DOT * (10-strength)}\n"
                      f"INT: {FULL_DOT * intelligence}{EMPTY_DOT * (10-intelligence)}\n"
                      f"CHA: {FULL_DOT * charisma}{EMPTY_DOT * (10-charisma)}")

    return character
