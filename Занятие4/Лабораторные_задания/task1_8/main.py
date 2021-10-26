def func_(list_: list):
    list_new = [i ** 2 for i in list_ if i < 0]
    return list_new

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(func_(list_))

