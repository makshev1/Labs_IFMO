# Создайте программу, которая выводит на экран все возможные уникальные строки, составленные из символов строки
# введенной с клавиатуры.


def generate(n, now, en, j):
    if now != "":en[j] -= 1
    if n == len(now):
        print(now)
    else:
        for i in range(len(en)):
            if en[i] != 0:

                generate(n, now+chr(i), en.copy(), i)
                continue


raw_str = input("In english, please: ")
letters = [0]*256
for i in raw_str:
    letters[ord(i)] += 1
generate(len(raw_str), "", letters, 0)
