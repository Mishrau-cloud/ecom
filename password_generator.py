import argparse
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
    """Generate a random password using cryptographically secure randomness."""
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

    password = [secrets.choice(charset) for charset in char_sets]
    pool = "".join(char_sets)
    password.extend(secrets.choice(pool) for _ in range(length - len(char_sets)))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        include_uppercase=not args.no_uppercase,
        include_lowercase=not args.no_lowercase,
        include_digits=not args.no_digits,
        include_symbols=not args.no_symbols,
    )
    print(password)


if __name__ == "__main__":
    main()
