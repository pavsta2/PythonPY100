if __name__ == "__main__":
    list_ = [1,7,-6,70,5,9,-1,3,90,-41]
    max_value_index = 0
    max_value = list_[0]
    current_value = 0
    for i in list_:
        if i > max_value:
            max_value_index = current_value
            max_value = list_[max_value_index]
        current_value = current_value + 1
    list_[0], list_[max_value_index] = list_[max_value_index], list_[0]
    print(list_, "конец")

