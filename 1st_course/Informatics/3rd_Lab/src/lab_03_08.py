"""
 Анонимные функции, lambda-выражения
"""
lfunc = lambda x, y, z=1: x + y + z
print("lfunc(1,2,3): ", lfunc(1, 2, 3))
print("lfunc(1,2): ", lfunc(1, 2))
print("lfunc(x=1,y=3): ", lfunc(x=1, y=3))
print("lambda result: ",
      (lambda a, b, sep=", ":
       sep.join((a, b)))("Hello", "World!"))
print("\n")

#  Создайте lambda-выражение, присвоив его переменной lam, осуществляющее проверку
# равенства остатка от деления введенного с клавиатуры числа,
# передаваемого в качестве аргумента, на 3. При равенстве остатка от
# деления на три нулю функция выводит значение на экран
lam = lambda a: \
    print(a, "% 3 = 0") if a % 3 == 0 else print(end="")

lam(a=int(input("Введите число ")))
