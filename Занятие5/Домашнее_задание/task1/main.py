if __name__ == "__main__":
    for row in range(1, 10):
        for col in range(1, 10):
            a = row * col
            print(f"{a:2}" if row * col % 10 == row * col else row * col, end=" ")
        print()

