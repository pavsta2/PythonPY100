def func_(n):
    list_n = list(str(n))
    list_n_dig = [int(d) for d in str(n)]
    list_n_dig_chet = [int(d) for d in str(n) if int(d) % 2 == 0]
    list_n_dig_nachet = list_n_dig[::2]
    list_n_dig_nanechet = list_n_dig[1::2]
    raznost = list_n_dig[0] - list_n_dig[-1]

    print(list_n)
    print(list_n_dig)
    print(sum(list_n_dig))
    print(sum(list_n_dig_chet))
    print(len(list_n_dig))
    print(max(list_n_dig))
    print(min(list_n_dig))
    print(list_n_dig_nachet)
    print(list_n_dig_nanechet)
    print(raznost)
    print(min(list_n_dig), list_n_dig.index(min(list_n_dig)))


if __name__ == "__main__":
    n = 123450
    func_(n)