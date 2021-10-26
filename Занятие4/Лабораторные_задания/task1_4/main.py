def list_func(list_1: list):
    n = sum(list_1) / len(list_1)
    print(n)
    list_new = [i for i in list_1 if i > n]
    return list_new

if __name__ == "__main__":
    print(list_func([1, 2, 5, 6, 7, 8, 12]))
