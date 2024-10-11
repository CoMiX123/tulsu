#!/usr/bin/env python3
import sys
import random

try:
    # Получаем число A из stdin
    A = int(sys.stdin.read().strip())
    
    # Генерируем случайное число B в диапазоне [-10, 10]
    B = random.randint(-10, 10)
    
    # Проверка, что B не равно 0, чтобы избежать деления на 0
    if B == 0:
        raise ValueError("Division by zero is undefined.")
    
    # Вычисляем отношение A/B
    result = A / B
    print(result)
except Exception as e:
    # Записываем все ошибки в файл errors.txt
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error in calculate_ratio.py: {e}\n")
