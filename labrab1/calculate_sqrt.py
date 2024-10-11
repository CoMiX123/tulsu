#!/usr/bin/env python3
import sys
import math

try:
    # Получаем число из stdin
    number = float(sys.stdin.read().strip())
    
    # Проверяем, что число не отрицательное, для вычисления квадратного корня
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    
    # Вычисляем квадратный корень
    result = math.sqrt(number)
    
    # Записываем результат в файл output.txt
    with open("output.txt", "w") as output_file:
        output_file.write(f"Square root: {result}\n")
except Exception as e:
    # Записываем все ошибки в файл errors.txt
    with open("errors.txt", "a") as error_file:
        error_file.write(f"Error in calculate_sqrt.py: {e}\n")
