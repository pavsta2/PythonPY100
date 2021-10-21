def remove_whitespace(str_):
    list_word = str_.split()
    print(list_word)

    return " ".join(list_word)



if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
