def func_(n):
    sum_n = sum([int(d) for d in list(str(n))])
    list_ = [int(d) for d in list(str(sum_n))]
    return list_

if __name__ == "__main__":
    n = 123893423423423423432234234234234234217979789
    print(func_(n))

    print(func_(n)[1])
    print((func_(n).index(func_(n)[1])) > 1)

