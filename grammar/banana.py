def getValue(b, r, n):
    if n == 1:
        return (b + b * r)
    return getValue(b + b * r, r, n - 1)

if __name__ == "__main__":
    b = float(input("input b: "))
    r = float(input("input r: "))
    n = float(input("input n: "))
    print("%.2f" % getValue(b, r, n))
