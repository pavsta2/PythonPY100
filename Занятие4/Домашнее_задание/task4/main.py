def func_(a):
    a_list_ = list(str(a))
    a_list_digits = list(int(d) for d in a_list_)

    if a_list_digits[0] + a_list_digits[1] + a_list_digits[2] == a_list_digits[3] + a_list_digits[4] + a_list_digits[5]:
        print("happy")
    else:
        print("not happy")

if __name__ == "__main__":
     a = 123221
     func_(a)
