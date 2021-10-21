def func(a, s, b):
    m = 0
    while s > 0:
        s = s - b + a
        b = b * 1.05
        m = m + 1
    return m

if __name__ == "__main__":
    a = int(input("Стипендия"))
    s = int(input("Накопления"))
    b = int(input("Расходы"))
    print(func(a, s, b))
