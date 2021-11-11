def func_(a):
    a_list_ = list(str(a))
    a_list_digits = list(int(d) for d in a_list_)
    a_list_uniqe = set(a_list_digits)
    if len(a_list_uniqe) == len(a_list_digits):
        print("нет одинак")
    else:
        print("есть одинак")
    return a_list_uniqe

if __name__ == "__main__":
     a = 1231
     print(func_(a))
     func_(a)
