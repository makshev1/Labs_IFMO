"""
 Логические операции
"""
f = True
g = False
print("f: ", f)
print("not f: ", not f)
print("f and g: ", f and g)
print("f or g: ", f or g)
print("f == g: ", f == g)
print("f != g: ", f != g)
print("\n")
h = 3
i = 5
print("h = ", h)
print("i = ", i)
print("h > i: ", h > i)
print("h < i: ", h < i)
print("h >= i: ", h >= i)
print("0 < h <= i: ", 0 < h <= i)
print("\n\n")
'''
 Побитовые операции
'''
j = 7
k = 20
print("j = %d; j in binary format: %s" % (j, bin(j)))
print("k = %d; k in binary format: %s" % (k, bin(k)))
print("j & k: %d; binary: %s" % (j & k, bin(j & k)))
# побитовое AND
print("j | k: %d; binary: %s" % (j | k, bin(j | k)))
# побитовое OR
print("j ^ k: %d; binary: %s" % (j ^ k, bin(j ^ k)))
# побитовое XOR
print("~k: %d; binary: %s" % (~k, bin(~k)))  # инверсия двоичного числа
print("k>>1: %d; binary: %s" % (k >> 1, bin(k >> 1)))  # сдвиг на один бит вправо
print("k<<1: %d; binary: %s" % (k << 1, bin(k << 1)))  # сдвиг на один бит влево
print("\n\n")

# Дополните код программы lab_01_02.py. Создайте переменные A
# и B с неравными целочисленными значениями, переменные C и D со
# значениями True и False соответственно
A = 8
B = 9
C = True
D = False

# Дополните код программы lab_01_02.py. Осуществите вывод на
# экран значений следующих логических выражений:
print("not (C and D): ", not (C and D))  # ¬(C∧D)
print("(C and D) or not (C and D): ", True)  # C∧D∨¬(C∧D)
print("not C or D: ", not C or D)  # ¬C∨D

# Дополните код программы lab_01_02.py. Осуществите вывод в
# консоль значений следующих выражений:
print("A<=B: ", A <= B)  # A<=B
print("A>B or A==B: ", A > B or A == B)  # A>B ∨ A==B
print("not (A < B): ", not (A < B))  # ¬(A<B)

# Дополните код программы lab_01_02.py. Создайте переменную s со значением 154 и переменную p со значением 6.
s = 154
p = 6
# Осуществите вывод ее значения в десятичном и двоичном виде на экран.
print("s = %d; binary: %s" % (s, bin(s)))
print("p = %d; binary: %s" % (p, bin(p)))

# Дополните код программы lab_01_02.py.
s = s | p  # Выполните операцию побитового ИЛИ над переменными s и p с записью результата в переменную s.
print("s | p: %d; binary: %s" % (s, bin(s)))  # Осуществите вывод значения в десятичном и двоичном виде на экран.

# Дополните код программы lab_01_02.py.
s = s >> 2  # Выполните операцию побитового сдвига вправо на 2 бита над переменными s и p
p = p >> 2  # с записью результатов в соответствующие переменные.
print("s>>2: %d; binary: %s" % (s, bin(s)))  # Осуществите вывод значений в десятичном и
print("p>>2: %d; binary: %s" % (p, bin(p)))  # двоичном виде на экран
