def list_func(list_1: list):
    sr_ar = round(sum(list_1) / len(list_1))
    print(sr_ar)
    list_new = [i - sr_ar for i in list_1]
    return list_new

if __name__ == "__main__":
    print(list_func([1, 2, 5, 6, 7, 8, 12]))
