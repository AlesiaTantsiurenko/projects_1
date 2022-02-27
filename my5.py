"""
10. Даний розмір файла в байтах. Використовуючи операцію ділення без залишку,
знайти кількість повних кілобайтів, які займає даний файл ( 1 кілобайт = 1024 байта ).
Танцюренко Олеся 141 група (2 підгрупа)
"""


def main():
    print(" Добро пожаловать в программу расчета количества полных киллобайт, содержащихся в байтах!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти количество полных киллобайт, содержащихся в байтах
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    byte = int(input("Введите количество байт "))
                    if byte>0:
                        break
                    else:
                        print("Значение байт должно быть позитивным!")
                except ValueError:
                    print("Несоответствие типов!")
            kilobyte = byte // 1024
            if is_positive_byte(byte):
                print("В ", byte, " байтах содержиться ", kilobyte, " полных киллобайт(-а).")
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
