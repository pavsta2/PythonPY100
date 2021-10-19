a = int(input("Введите значение А"))
b = int(input("Введите значение B"))
c = int(input("Введите значение C"))

if a < 45 and b >= 45 and c >= 45:
    print ("только А меньше 45")
elif a >= 45 and b < 45 and c >= 45:
    print("только B меньше 45")
elif a >= 45 and b >= 45 and c < 45:
    print("только C меньше 45")
else: print ("условие когда только одно число меньше 45 не выполняется")