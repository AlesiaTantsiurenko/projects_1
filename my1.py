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


def is_positive(num1, num2):
    """ Функция для проверки вводимых чисел - являются ли они позитивными"""
    if num1 > 0 and num2 > 0:
        return num1, num2
    else:
        print("Сторона не может быть отрицательной длины!")


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
            try:
                a = float(input("Введите первую сторону треугольника "))
                b = float(input("Введите вторую сторону треугольника "))
            except ValueError:
                print("Несоответствие типов!")
            if is_positive(a, b):
                print("Гипотенуза тругольника равна ", hypotenuse(a, b))
                print("Периметр треугольника равен ", perimetr(a, b, hypotenuse(a,b)))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
