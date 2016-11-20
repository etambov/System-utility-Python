# coding: utf-8

# Python. Быстрый старт.
# Занятие 3.

# Домашнее задание: 
#                  функциями dir и help исследовать модули os, sys, psutil
#                  вывести максимум информации о системе (ветка №2):
#                    имя текущей директории, платформа (ОС), кодировка файловой системы,
#                    логин пользователя, количество CPU


# Подключение модуля производится командой import.
# Модуль os идет в комплекте с Python'ом.
import os
import sys

# psutil - сторонний модуль, нужно установить через pip install psutil
import psutil       


print("Great Python Program!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давайте поработаем? (Y/N)")
     
if answer == 'Y':
    print("Отлично, хозяин!")
    print("Я умею:")
    print(" [1] - выведу список файлов")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Укажите номер действия: "))
    
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print("Вот что я знаю о системе")
        print("Количество процессоров: ", psutil.cpu_count())
        print("Платформа: ", sys.platform)
        print("Кодировка файловой системы: ", sys.getfilesystemencoding())
        print("Текущая директория: ", os.getcwd())
        print("Текущая пользователь: ", os.getlogin())
    elif do == 3:
        print(psutil.pids())
    else:
        pass
   
# Функция type выводит информацию о типе переменной (объекта)
# Функция dir показывает внутреннее содержимое переменной (объекта) - атрибуты, методы
# Функция help выводит встронную справку об объекте
    
elif answer == 'N':    
    print("До свидания!")
else:
    print("Неизвестный ответ")    
