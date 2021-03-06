"""
4. Дано катети прямокутного трикутника a i b. Знайти його гіпотенузу с і периметр P: c=(a^2+b^2)1/2, P=a+b+c
Танцюренко Олеся 141 гр (2 підгрупа)
"""


def hypotenuse(num1, num2):
    """ Функция для нахождения гипотенузы треугольника """
    num3 = (num1 ** 2 + num2 ** 2) ** (1 / 2)
    return num3


def perimetr(num1, num2, num3):
    """ Функция для нахождения периметра треугольника """
    p = num1 + num2 + num3
    return p


def main():
    print(" Добро пожаловать в программу расчета гипотенузы и периметра!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти гипотенузу и периметр треугольника
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    a = float(input("Введите первую сторону треугольника "))
                    if a > 0:
                        break
                    else:
                        print("Сторона треугольника не можеть быть с отрицательным значением!")
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    b = float(input("Введите вторую сторону треугольника "))
                    if b > 0:
                        break
                    else:
                        print("Сторона треугольника не можеть быть с отрицательным значением!")

                except ValueError:
                    print("Несоответствие типов!")

            print("Гипотенуза тругольника равна ", hypotenuse(a, b))
            print("Периметр треугольника равен ", perimetr(a, b, hypotenuse(a, b)))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
