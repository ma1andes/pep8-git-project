"""Тесты для математических функций."""

import unittest

from calculator import (
    add_numbers,
    divide_numbers,
    subtract_numbers,
)


class CalculatorTests(unittest.TestCase):
    """Проверяет работу функций калькулятора."""

    def test_add_numbers(self):
        """Проверяет сложение."""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        """Проверяет вычитание."""
        self.assertEqual(subtract_numbers(10, 4), 6)

    def test_divide_numbers(self):
        """Проверяет деление."""
        self.assertEqual(divide_numbers(10, 2), 5)

    def test_divide_by_zero(self):
        """Проверяет ошибку деления на ноль."""
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)


if __name__ == "__main__":
    unittest.main()
