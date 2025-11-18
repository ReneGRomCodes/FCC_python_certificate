def caesar(text: str, shift: int, encrypt:bool=True) -> str:
    """Apply a Caesar cipher to the given text.
    ARGS:
        text (str): The text to encrypt or decrypt.
        shift (int): The shift amount (1–25). Positive values shift forward.
        encrypt (bool): If True, encrypt the text. If False, decrypt it.
    RETURNS:
        str: The encrypted/decrypted text, or an error message if the shift value is invalid.
    """
    # Validate shift input
    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    alphabet: str = "abcdefghijklmnopqrstuvwxyz"

    # If decrypting, just flip the shift direction
    if not encrypt:
        shift = -shift

    # Create the shifted alphabet
    shifted_alphabet: str = alphabet[shift:] + alphabet[:shift]

    # Build translation table for both lowercase and uppercase
    translation_table: dict[int, int] = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Apply translation
    return text.translate(translation_table)


def encrypt(text: str, shift: int) -> str:
    """Encrypt text using the Caesar cipher.
    ARGS:
        text (str): The text to encrypt.
        shift (int): The shift amount (1–25).
    RETURNS:
        str: The encrypted text.
    """
    return caesar(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text encoded with the Caesar cipher.
    ARGS:
        text (str): The text to decrypt.
        shift (int): The original shift amount used for encryption.
    RETURNS:
        str: The decrypted text.
    """
    return caesar(text, shift, encrypt=False)
