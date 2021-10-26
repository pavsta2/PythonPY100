def func_(list_):
    list_new = [i for i in list_ if i > list_[0]]
    print(len(list_new))
    #print(len(list_new = [i for i in list_ if i > list_[0]]))

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    func_(list_)
