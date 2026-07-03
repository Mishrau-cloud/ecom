import secrets
import string


def generate_password(
    length: int = 12,
    *,
    include_uppercase: bool = True,
    include_lowercase: bool = True,
    include_digits: bool = True,
    include_symbols: bool = True,
) -> str:
    """Generate a random password.

    Args:
        length: The number of characters in the password.
        include_uppercase: Whether to allow uppercase letters.
        include_lowercase: Whether to allow lowercase letters.
        include_digits: Whether to allow digits.
        include_symbols: Whether to allow symbols.

    Returns:
        A password containing at least one character from each enabled set.

    Raises:
        ValueError: If length is less than 1, if no character sets are enabled,
            or if length is less than the number of enabled character sets.
    """
    if length < 1:
        raise ValueError("length must be at least 1")

    char_sets = []
    if include_uppercase:
        char_sets.append(string.ascii_uppercase)
    if include_lowercase:
        char_sets.append(string.ascii_lowercase)
    if include_digits:
        char_sets.append(string.digits)
    if include_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("at least one character set must be enabled")
    if length < len(char_sets):
        raise ValueError("length must be at least the number of enabled character sets")

    pool = "".join(char_sets)
    password = [None] * length
    available_positions = list(range(length))

    for charset in char_sets:
        position = secrets.choice(available_positions)
        available_positions.remove(position)
        password[position] = secrets.choice(charset)

    for index, value in enumerate(password):
        if value is None:
            password[index] = secrets.choice(pool)

    return "".join(password)
