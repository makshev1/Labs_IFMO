d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
"""
 Операции cо словарями
"""
d5 = d2.copy()  # создание копии словаря
print("Dict d5 copying d2 = ", d5)
# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys())  # список ключей
print("Get dict values d5.values(): ", d5.values())  # список значений
print("\n")

# Создайте словарь myInfo, содержащий информацию о Ваших
# фамилии, имени, отчестве, дне, месяце, годе рождения и университете
myInfo = {
    "surname": "Potanin",
    "name": "Lev",
    "middlename": "Antonovich",
    "day": "15",
    "month": "August",
    "year": "2001",
    "university": "IFMO"
}
# в полях surname, name, middlename, day, month, year, university соответственно.
# Получите и поочередно выведите на экран списки ключей и значений словаря myInfo.
print("MyInfo keys:", myInfo.keys())
print("MyInfo values:", myInfo.values())
