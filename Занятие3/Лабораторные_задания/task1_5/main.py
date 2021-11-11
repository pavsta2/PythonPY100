def func_(list_: list) -> list:
    sum_ = 0
    for i in list_:
        if i != 0:
            sum_ = sum_ + i


    return sum_

def func_2():
    list_ = []
    while True:
        x = int(input("введите элемент списка"))
        if x != 0:
            list_ = list_ + [x]
            print(list_)
        elif x == 0:
            list_ = list_ + [x]
            print(list_)
            break
    return list_

if __name__ == "__main__":
    print(func_(func_2()))
