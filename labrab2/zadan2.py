#!/usr/bin/env python3
import sys
import os
import signal

# Функция для проверки имени
class ValidationError(Exception):
    pass

def validate_name(name):
    if not name[0].isupper():
        raise ValidationError("Name does not start with a capital letter.")
    if not name.isalpha():
        raise ValidationError("Name contains invalid characters (only letters are allowed).")

# Функция для приветствия
def greet(name):
    print(f"Hello, {name}!")

# Функция для обработки списка имен из файла
def greet_from_file(filename):
    errors = []  # Собираем ошибки в список

    try:
        with open(filename, "r") as file:
            for line in file:
                name = line.strip()
                try:
                    validate_name(name)
                    greet(name)
                except ValidationError as e:
                    errors.append(f"Invalid name '{name}': {e}")
    except FileNotFoundError:
        sys.stderr.write(f"Error: File '{filename}' not found.\n")
        return
    except Exception as e:
        sys.stderr.write(f"Error in greet_from_file: {e}\n")
        return

    if errors:
        with open("error.txt", "a") as error_file:
            error_file.write("\n".join(errors) + "\n")
        # Записываем ошибку в stderr, но не выводим её пользователю
        sys.stderr.write(f"Errors were logged in 'error.txt'.\n")

# Функция для интерактивного режима
def interactive_greeting():
    def signal_handler(sig, frame):
        print("\nGoodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # Отключаем вывод ошибок в консоль (stderr)
    sys.stderr = open(os.devnull, 'w')

    while True:
        try:
            name = input("Please enter your name: ").strip()
            try:
                validate_name(name)
                greet(name)
            except ValidationError as e:
                # Записываем ошибку в файл
                with open("error.txt", "a") as error_file:
                    error_file.write(f"Invalid name '{name}': {e}\n")
                # Ошибка записана в файл, но не выводится в консоль
                continue  # Продолжаем цикл, чтобы запросить имя снова
        except Exception as e:
            # Записываем все неожиданные ошибки в stderr для отладки
            sys.stderr.write(f"Unexpected error: {e}\n")

# Основная программа
if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            greet_from_file(filename)
        else:
            sys.stderr.write(f"Error: '{filename}' is not a valid file.\n")
    else:
        interactive_greeting()
