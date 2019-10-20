def calc(x):
    if x > 1:
        return 3 * x - 5
    elif x < -1:
        return 5 * x + 3
    else:
        return x + 2

if __name__ == "__main__":
    x = float(input("Input x:"))
    print(calc(x))

