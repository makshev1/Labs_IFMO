b2 = {"bear", "fox", "squirrel", "woodpecker", "woodpecker", "wolf", "hedgehog"}  # без этого не работает,
# тк код дальше использует эту строку
"""
 Операции над множествами
"""
print("Check 'bear' in b2 = ", "bear" in b2)
b4 = set("123456135")
b5 = set("12367")
print("Set b4: {0}, \nSet b5: {1}".format(b4, b5))
print("b4 - b5: ", b4 - b5)  # присутствие в первом множестве, но не во втором
print("b4 difference b5 (b4-b5): ", b4.difference(b5))
print("b4 | b5: ", b4 | b5)  # присутствие хотя бы в одном множестве
print("b4 union b5 (b4 | b5): ", b4.union(b5))
print("b4 & b5: ", b4 & b5)  # присутствие в обоих множествах
print("b4 intersection b5 (b4&b5): ", b4.intersection(b5))
print("b4 ^ b5: ", b4 ^ b5)  # присутствие только в одном из множеств
# проверка на непересечение множеств
print("b4 and b5 are disjoint: ", b4.isdisjoint(b5))
b4.update(b5)  # добавить элементы другого множества
print("add b5 to b4: ", b4)
b4.add("abc")  # добавить элемент
print("add 'abc' to b4: ", b4)
b4.remove("5")  # удалить элемент
print("remove element '5' from b4: ", b4)
b4.clear()  # очистить множество
print("clear b4: ", b4)
print("\n")

set1 = set("qetuwrt")  # Создайте два множества set1 и set2 из строк "qetuwrt"
set2 = set("asfrewgq")  # и "asfrewgq" соответственно.
print("set1-set2:", set1 - set2)  # Поочередно выполните операции разности,
print("set1|set2:", set1 | set2)  # объединения,
print("set1&set2:", set1 & set2)  # пересечения и
print("set1^set2:", set1 ^ set2)  # симметричной разности, выводя значения на экран.
set1.update(set2)  # Добавьте в множество set1 элементы множества set2 с использованием функции update(),
set2.add('u')  # в множество set2 элементы "t" и "u" с использованием функции add().
set2.add('t')  # в множество set2 элементы "t" и "u" с использованием функции add().
print("set1-set2:", set1.difference(set2))  # Повторно выполните операции разности, объединения, пересечения и
print("set1|set2:", set1.union(set2))  # симметричной разности, выводя значения на экран
print("set1&set2:", set1.intersection(set2))
print("set1^set2:", set1.symmetric_difference(set2))

# Создайте неизменяемое множество set3 из множества set1. Удалите из множества set3 элемент "q".
set3 = frozenset(set1)
# set3.remove('q')
# 'frozenset' object has no attribute 'remove'
# Тк frozenset - неизменяемый тип данных -> нет методов добавления/исключения элементов
