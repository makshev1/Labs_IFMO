"""
 Функции
"""


def dictUpdate(a):
    a.update([("x", 5)])
    print("dict in function: ", a)
    return


def dictNoUpdate(a):
    a = a.copy()
    a.update([("y", 3)])
    print("dict in function: ", a)
    return


def returnFunc(a):
    def f1(a):
        print("returned f1(a): ", a)

    return f1


d = {"v": 7}
dictUpdate(d)
print("dict out of function: ", d)
dictNoUpdate(d)
print("dict out of function: ", d)
f = returnFunc(d)
print("f: ", f)
f(2)
print("\n")


def returnMod(arg):  # Создайте функцию returnMod, возвращающую функцию,
    print("returnMod", arg % 15)  # которая осуществляет расчет остатка от деления переданного аргумента на 15
    return arg % 15  # и вывод этого значения на экран.


mod15 = returnMod(int(input("Введите число: ")))  # Вызовите функцию returnMod и осуществите запись возвращенного
# значения в переменную mod15. С использованием переменной mod15 добейтесь выполнения расчета остатка от деления и
# вывода значения на экран
