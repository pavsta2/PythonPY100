def func_(list_):
    list_chet = [i for i in list_ if i % 2 == 0]
    list_nechet = [i for i in list_ if i % 2 != 0]
    print("четных больше") if len(list_chet) > len(list_nechet) else print("нечетных больше")

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    func_(list_)
