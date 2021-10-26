def task(epsilon=0.0001):
    sum_ = 0
    n = 1
    item_n = 1 / 2 ** n
    while item_n >= epsilon:
        sum_ += item_n
        n += 1
        item_n = 1 / 2 ** n
        print(sum_)

    return sum_

if __name__ == "__main__":
    print(task())

