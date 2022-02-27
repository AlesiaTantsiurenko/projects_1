"""
9. Дано двозначне число. Знайти суму і добуток його цифр.
Танцюренко Олеся 141 група (2 підгрупа)
"""


def sum_find(num1, num2):
    """ Функция расчета суммы цифр числа """
    s = num1 + num2
    return s


def multi_find(num1, num2):
    """ Функция расчета произведения цифр числа """
    m = num1 * num2
    return m


def main():
    print(" Добро пожаловать в программу расчета суммы и произведения двузначного числа!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти сумму и производную цифр двузначного числа
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    num = int(input("Введите двузначное число "))
                    if 100 > num > 9:
                        break
                    else:
                        print("Число должно быть двузначным и позитивным !")
                except ValueError:
                    print("Несоответствие типов!")
            numeric1 = num // 10
            numeric2 = num % 10

            print("Сумма цифр числа равна ", sum_find(numeric1, numeric2))
            print("Произведение цифр числа равно ", multi_find(numeric1, numeric2))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
