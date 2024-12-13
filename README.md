# Лабораторная работа №1
## Использование
Перейдите в каталог labrab1:
```
cd labrab1
```
Сделайте файлы ```calculate_ratio.py```, ``` calculate_sqrt.py ``` и ``` generate_number.py ``` исполняемыми:
```
chmod +x calculate_ratio.py
chmod +x calculate_sqrt.py
chmod +x generate_number.py
```
Запустим:
```
./generate_number.py | ./calculate_ratio.py 2>> errors.txt | ./calculate_sqrt.py 2>> errors.txt
```
# Лабораторная работа №2
## Использование
Перейдите в каталог labrab2:
```
cd labrab2
```
Сделайте файл исполняемым ``` zadan2.py ```
```
chmod +x zadan2.py
```
Запустите в автономном режиме:
```
./zadan2.py < names.txt 2> error.txt
```
Запустите в интерактивном режиме:
```
./zadan2.py
```
