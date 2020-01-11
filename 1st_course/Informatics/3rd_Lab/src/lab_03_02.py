"""
 Множества
"""
# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker", "woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)
# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")

# Создайте строковую переменную s со значением
s = "Electricity is the set of physical phenomena associated with the presence of electric charge. Lightning is one " \
    "of the most dramatic effects of electricity"
set1 = set(s)  # Создайте множество set1 из строки s.
print("set1:", set1)  # Осуществите вывод множества set1 на экран.

# Для множества set1 осуществите проход по всем его элементам с выводом на экран гласных букв
print("Гласные буквы в set:", end=" ")
for i in set1:
    if i == "a" or i == "A" or i == "e" or i == "E" \
            or i == "u" or i == "U" or i == "i" or i == "I" or i == "o" or i == "O":
        print(i, end=" ")
print("\n")
