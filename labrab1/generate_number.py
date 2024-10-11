#!/usr/bin/env python3
import sys
import random

try:
    # Генерируем случайное число A в диапазоне [-10, 10]
    A = random.randint(-10, 10)
    print(A)  # Выводим число A на консоль
except Exception as e:
    # Записываем все ошибки в файл errors.txt
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error in generate_number.py: {e}\n")
