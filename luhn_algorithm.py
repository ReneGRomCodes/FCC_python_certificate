def luhn(card_number: str) -> bool:
    """Verifies the validity of a credit card number 'card_number' (str) using the Luhn algorithm and returns 'True' if
    card number is valid, 'False' if not."""
    sum_of_odd_digits: int = 0
    card_number_reversed: str = card_number[::-1]
    odd_digits: str = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits: int = 0
    even_digits: str = card_number_reversed[1::2]

    for digit in even_digits:
        number: int = int(digit) * 2

        if number >= 10:
            number = (number // 10) + (number % 10)

        sum_of_even_digits += number

    total: int = sum_of_odd_digits + sum_of_even_digits

    return total % 10 == 0


def verify_card_number(card_number):
    card_translation = str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(card_translation)

    if luhn(translated_card_number):
        return "VALID!"
    else:
        return "INVALID!"
