if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

    # предположим, что первый элемент в нашем списке минимальный
    min_value_index = 0
    min_value = list_[min_value_index]

    # TODO заменить на enumerate
    for i, current_value in enumerate(list_):
        if current_value <= min_value:
            min_value = current_value
            min_value_index = i
    set_min_values_indexes = []
    for i, current_value in enumerate(list_):
        if current_value == min_value:
            set_min_values_indexes = set_min_values_indexes + [i]

    print("Минимальный элемент =", min_value, "находится по индексам", set_min_values_indexes)
