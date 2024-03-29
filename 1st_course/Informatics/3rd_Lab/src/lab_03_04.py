"""
Словари
"""
d1 = {
    "day": 18,
    "month": 6,
    "year": 1983
}
d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
d3 = dict([("street", "Kronverksky pr."), ("house", 49)])
d4 = dict.fromkeys(["1", "2"], 3)
print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")

startDict = {"ready": 3, "set": 2, "go": 1}  # Создайте словарь startDict с ключами ready, set, go и значениями 3, 2 и 1
startDict1 = dict([("ready", 3), ("set", 2), ("go", 1)])  # соответственно тремя разными способами,
startDict2 = dict(ready=3, set=2, go=1)  # добавляя индекс к имени переменной.
print("startDict:", startDict, "\nstartDict1:", startDict1, "\nstartDict2:", startDict2)  # Выведите словари

dict1 = dict.fromkeys(['key1', "key2"], input("Введите значение для ключей dict1: "))  # Создайте словарь dict1
# с ключами key1 и key2, заполнив их одинаковым значением, введенным с клавиатуры
print(dict1)  # Осуществите вывод словаря dict1 на экран
