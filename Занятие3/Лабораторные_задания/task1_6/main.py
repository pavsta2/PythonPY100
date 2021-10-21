def budget(b):
    total9 = 0
    for i in range(1, 10):
        b_next = b * 1.03
        total9 = total9 + b_next
        b = b_next
    return b + total9


if __name__ == "__main__":
    a = int(input("введите cтипендию"))
    b = int(input("введите расходы на проживание"))
    total_a = a * 10
    print(budget(b))
    print(budget(b) - total_a)
    print(b * 1.03)


