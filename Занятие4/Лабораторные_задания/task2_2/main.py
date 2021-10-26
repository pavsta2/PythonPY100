def func_(n: int):
    list_dig = [int(d) for d in list(str(n))]
    return list_dig

if __name__ == "__main__":
    n = 123984
    print(((8 and 4) or 9) in func_(n))

