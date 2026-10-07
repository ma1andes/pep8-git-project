"""Основной файл приложения."""

from calculator import (
    add_numbers,
    divide_numbers,
    multiply_numbers,
    subtract_numbers,
)


def main():
    """Демонстрирует работу математических функций."""
    first_number = 20
    second_number = 5

    print("Сложение:", add_numbers(first_number, second_number))
    print("Вычитание:", subtract_numbers(first_number, second_number))
    print("Умножение:", multiply_numbers(first_number, second_number))
    print("Деление:", divide_numbers(first_number, second_number))


if __name__ == "__main__":
    main()
