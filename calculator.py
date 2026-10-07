"""Функции для выполнения математических операций."""


def add_numbers(first_number, second_number):
    """Возвращает сумму двух чисел."""
    return first_number + second_number


def subtract_numbers(first_number, second_number):
    """Возвращает разность двух чисел."""
    return first_number - second_number


def divide_numbers(dividend, divisor):
    """Возвращает результат деления двух чисел."""
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно")

    return dividend / divisor
