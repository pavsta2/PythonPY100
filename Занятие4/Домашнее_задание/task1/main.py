def func_(a):
    a_list_ = list(str(a))
    a_list_digits = list(int(d) for d in a_list_)
    a_list_uniqe = set(a_list_digits)
    if len(a_list_uniqe) == 1:
        print("все цифры одинак")
    else:
        print("все цифры не одинак")
    return a_list_uniqe

if __name__ == "__main__":
     a = 22222222
     print(func_(a))
     func_(a)

