a = int(float.fromhex(input("Введите число от -80 до 7F: ")))
if a<-128 or a>127:
    print("Неверный диапазон")
elif a<0:
    c = str(bin(128+abs(128+a)))
    c = c[2:]
    print(c)
else:
    c = str(bin(128+abs(128+a)))
    c = c[3:]
    print(c)

