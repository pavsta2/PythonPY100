def main():
    numb = 0
    dig = 0
    res = 0
    while res <= 500:
        numb += 1
        dig += 1
        res = dig ** 2 + dig ** 2
        print(numb, dig, res)

    return numb

if __name__ == "__main__":
    print(main())

