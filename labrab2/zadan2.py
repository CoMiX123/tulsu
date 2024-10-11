#!/usr/bin/env python3
import sys
import os
import signal

# Функция для проверки имени и возврата причины ошибки
def validate_name(name):
    if not name.istitle():
        return False, "Name does not start with a capital letter."
    if not name.isalpha():
        return False, "Name contains invalid characters (only letters are allowed)."
    return True, ""

# Функция для приветствия
def greet(name):
    print(f"Hello, {name}!")

# Функция для обработки списка имен из файла
def greet_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                name = line.strip()  # Убираем лишние пробелы и символы новой строки
                valid, error_msg = validate_name(name)
                if valid:
                    greet(name)
                else:
                    with open("error.txt", "a") as error_file:
                        error_file.write(f"Invalid name '{name}': {error_msg}\n")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        with open("error.txt", "a") as error_file:
            error_file.write(f"Error in greet_from_file: {e}\n")

# Функция для интерактивного режима
def interactive_greeting():
    def signal_handler(sig, frame):
        print("\nGoodbye!")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)  # Обработка Ctrl+C

    while True:
        try:
            name = input("Please enter your name: ").strip()
            valid, error_msg = validate_name(name)
            if valid:
                greet(name)
            else:
                with open("error.txt", "a") as error_file:
                    error_file.write(f"Invalid name '{name}': {error_msg}\n")
        except Exception as e:
            with open("error.txt", "a") as error_file:
                error_file.write(f"Error in interactive_greeting: {e}\n")

# Основная программа
if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Режим работы с файлом
        filename = sys.argv[1]
        if os.path.isfile(filename):
            greet_from_file(filename)
        else:
            print(f"Error: {filename} is not a valid file.")
    else:
        # Интерактивный режим
        interactive_greeting()
