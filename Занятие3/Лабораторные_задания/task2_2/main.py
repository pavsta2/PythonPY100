def is_pal(str_):
    str_rev = str_[::-1]
    return str_ == str_rev


if __name__ == "__main__":
    str_ = str(input())
    if is_pal(str_) is True:
        print(str_, "является палиндромом")
    else:
        print(str_, "не является палиндромом")
