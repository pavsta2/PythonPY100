def task(str1, str2, k):
    str1_k = []
    str2_k = []
    for i in range(k+1):
        str1_k = str1_k + [str1[i]]
        str2_k = str2_k + [str2[i]]
    return str1_k == str2_k



if __name__ == "__main__":
    str1 = str(input("str1"))
    str2 = str(input("str2"))
    k = int(input("к"))
    if task(str1, str2, k) == True:
        print("Да")
    else:
        print("нет")