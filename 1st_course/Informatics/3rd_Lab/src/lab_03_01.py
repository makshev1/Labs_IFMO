"""
 Кортежи
"""
# создание кортежа
a1 = tuple()
a2 = 1, 2, 3, "abc"
a3 = (1, 2, 3, "abc")
print("Tuple a1 = ", a1)
print("Tuple a2 = ", a2)
print("Tuple a3 = ", a3)
# создание кортежа из других структур данных
l = [1, 2, 3, "abc"]  # из списка
a4 = tuple(l)
print("Tuple a4 from list l = ", a4)
a5 = tuple("Hello, World!")  # из строки
print("Tuple a5 from string = ", a5)
# вложенность кортежей
a6 = a2, a3
print("Tuple a6 formed by a2 and a3 = ", a6)
# объединение кортежей
a7 = a2 + a3
print("Tuple a7 by combining a2 and a3 = ", a7)
# доступ к элементам кортежей
print("a6[0]: ", a6[0])
print("a6[0][3]: ", a6[0][3])
print("\n")


# Раскомментируйте строку '# a6[0][3] = "cba"'. Объясните поведение программы.
# Программа крашится, тк мы пытаемся поменять значение в проинициализированном элементе котрежа
# a6[0][3] = "cba"

k1 = (int(input("Введите день: ")), int(input("Введите месяц: ")), int(input("Введите год: ")))  # Создайте кортеж k1,
# содержащий значения дня, месяца и года Вашего рождения, введенные с клавиатуры,
k2 = (input("Введите фамилию: "), input("Введите имя: "), input("Введите отчество: "))
# и кортеж k2 со значениями Ваших фамилии, имени и отчества.
k3 = k1 + k2  # Объедините кортежи k1 и k2, записав результат в k3.
print("k3:", k3)  # Осуществите вывод значения переменной k3 на экран


k4 = (k1, k2)  # Создайте кортеж k4, в который будут вложены кортежи k1 и k2.
print("k4:", k4)  # Осуществите вывод значения переменной k4,
print("k4[1][1]:", k4[1][1])  # а также второго элемента второго вложенного кортежа на экран






