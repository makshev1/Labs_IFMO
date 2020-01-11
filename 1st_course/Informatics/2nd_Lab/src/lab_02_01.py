"""
 Условия
"""
# if..else
num = int(input("How many times have you been to the Hermitage? "))
if num > 0:
    print("Wonderful!")
    print("I hope you liked this museum!")
else:
    print("You should definitely visit the Hermitage!")
# if..elif..else
course = int(input("What is your course number?"))
if course == 1:
    print("You are just at the beginning!")
elif course == 2:
    print("You learned many things, but not all of them!")
elif course == 3:
    print("The basic course is over, it's time for professional disciplines!")
else:
    print("Oh! You need to hurry! June is the month of thesis defense")
x = 5
y = 12
if y % x > 0: print("%d cannot be evenly divided by %d" % (y, x))
z = 3
x = "{} is a divider of {}".format(z, y) if y % z == 0 else "{} is not a divider of {}".format(z, y)
print(x)
print("\n\n")

# Создайте переменную p, в которую будет записано значение количества выполненных за год лабораторных по различным
# дисциплинам. Осуществите вывод значения переменной в терминал, если значение больше 10. Оператор ветвления запишите
# двумя способами: в одну строку и в несколько строк.
p = int(input("Введите количество выполненных за год лабораторных по различным дисциплинам"))
if p > 10: print("Количество выполненных за год лабораторных по различным дисциплинам:", p)
if p > 10:
    print("Количество выполненных за год лабораторных по различным дисциплинам:", p)

a = 157  # Создате переменные a со значением 157 и b со значением 525.
b = 525
# Осуществите проверку следующих условий и выполнение соответствующих действий:
if a > b:  # если a>b, рассчитайте остаток от деления a на b и выведите значение на экран;
    print("a>b -> a%b =", (a % b))
elif a < b:  # если a<b, рассчитайте остаток от деления b на a и выведите значение на экран;
    print("a<b -> b%a =", (b % a))
else:  # если a==b, рассчитайте произведение чисел a и b и выведите значение на экран.
    print("a=b -> a*b =", (a ** 2))

