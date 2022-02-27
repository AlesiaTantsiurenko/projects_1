"""
14. Обчислити довжину окружності, площу кола та об'єм кулі одного і того ж заданого радіусу.
Танцюренко Олеся 141 група (2 підгрупа)
"""
import math


def length(r):
    """ Функция расчета длины окружности """
    l = 2 * math.pi * r
    return l


def area(r):
    """ Функция расчета площади окружности """
    s = math.pi * r ** 2
    return s


def volume(r):
    """ Функция расчета объема сферы """
    v = (4 * math.pi * r ** 3) / 3
    return v


def main():
    print(" Добро пожаловать в программу расчета длины, площади окружности и объема сферы!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти длину окружности
            2 - Найти площадь окружности
            3 - Найти объем сферы
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    radius = float(input("Введите радиус "))
                    if radius > 0:
                        break
                    else:
                        print("Радиус не может быть отридцательным!")
                except ValueError:
                    print("Несоответствие типов!")

            print("Длина окружности равна ", length(radius))
        elif choice == "2":
            while True:
                try:
                    radius = float(input("Введите радиус "))
                    if radius > 0:
                        break
                    else:
                        print("Радиус не может быть отридцательным!")
                except ValueError:
                    print("Несоответствие типов!")

            print("Площадь окружности равна ", area(radius))
        elif choice == "3":
            while True:
                try:
                    radius = float(input("Введите радиус "))
                    if radius > 0:
                        break
                    else:
                        print("Радиус не может быть отридцательным!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Объем сферы равен ", volume(radius))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
