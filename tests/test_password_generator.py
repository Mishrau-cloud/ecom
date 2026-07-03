import unittest

from password_generator import generate_password


class PasswordGeneratorTests(unittest.TestCase):
    def test_password_contains_all_character_types_when_all_enabled(self) -> None:
        password = generate_password(length=12)

        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(not char.isalnum() for char in password))

    def test_password_respects_requested_character_sets(self) -> None:
        password = generate_password(
            length=6,
            include_uppercase=False,
            include_lowercase=False,
            include_digits=True,
            include_symbols=False,
        )

        self.assertEqual(len(password), 6)
        self.assertTrue(password.isdigit())

    def test_password_length_must_be_positive(self) -> None:
        with self.assertRaises(ValueError):
            generate_password(length=0)

    def test_password_rejects_negative_length(self) -> None:
        with self.assertRaises(ValueError):
            generate_password(length=-1)

    def test_password_requires_at_least_one_character_set(self) -> None:
        with self.assertRaises(ValueError):
            generate_password(
                length=4,
                include_uppercase=False,
                include_lowercase=False,
                include_digits=False,
                include_symbols=False,
            )

    def test_password_requires_length_to_cover_enabled_character_sets(self) -> None:
        with self.assertRaises(ValueError):
            generate_password(
                length=2,
                include_uppercase=True,
                include_lowercase=True,
                include_digits=True,
                include_symbols=True,
            )


if __name__ == "__main__":
    unittest.main()
