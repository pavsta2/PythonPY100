def list_func(n, m):
    list_ = [[i ** 2] for i in range(n, m+1)]
    return list_
if __name__ == "__main__":
    n = 1
    m = 2
    print(list_func(n, m))
