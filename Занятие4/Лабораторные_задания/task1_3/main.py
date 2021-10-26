def list_func(list_1):
    list_ = [i for i in list_1 if i % 2 == 0]
    num_ = len(list_)
    return num_
if __name__ == "__main__":
    print(list_func([1, 2, 5, 6, 7, 8]))
