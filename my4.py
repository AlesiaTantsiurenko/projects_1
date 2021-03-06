"""
19. Знайти корені квадратного рівняння Ах+Вx=0, заданого своїми коефіцієнтами А,В,С(А>0),
  якщо відомо, що дискримінанат рівняння позитивний. Вивести спочатку менший, а потім більший
із знайдених коренів. Коріння квадратного рівняння знаходяться за формулою х1,2=(-В+-(D)^1\2)/(2A),
       де D - дискримінант, що дорівнює В^2-4AC.
Танцюренко Олеся 141 група (2 підгрупа)
"""


def discriminant(num1, num2, num3):
    """ Функция для расчета дискриминанта """
    dis = num2 ** 2 - 4 * num1 * num3
    return dis


def root_1(num1, num2, num3):
    """ Функция расчета первого корня уравнения """
    root1 = (-num2 + (discriminant(num1, num2, num3)) ** (1 / 2)) / (2 * num1)
    return root1


def root_2(num1, num2, num3):
    """ Функция расчета второго корня уравнения """
    root2 = (-(num2) - (discriminant(num1, num2, num3)) ** (1 / 2)) / (2 * num1)
    return root2


def is_positive_d(d):
    """ Функция для проверки значения дискриминанта """
    if d >= 0:
        return d
    else:
        print("Дискриминант уровнения должен быть больше нуля!")


def main():
    print(" Добро пожаловать в программу расчета корней уровнения!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти корни уровнения
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    a = float(input("Введите коефициент A = "))
                    if a > 0:
                        break
                    else:
                        print("Коефициент А не может быть отридцательным!")
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    b = float(input("Введите коефициент B = "))
                    break
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    c = float(input("Введите коефициент C = "))
                    break
                except ValueError:
                    print("Несоответствие типов!")

            d = discriminant(a, b, c)
            if is_positive_d(d):
                x1 = root_1(a, b, c)
                x2 = root_2(a, b, c)
                if x1 < x2:
                    print("Меньший корень = ", x1)
                    print("Больший корень = ", x2)
                else:
                    print("Меньший корень = ", x2)
                    print("Больший корень = ", x1)

        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
