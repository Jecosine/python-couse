from mymodule import factorial

def calc(n):
    s = 0.0
    for i in range(n):
        s += 1.0 / factorial(i + 1)
    return s
n = int(input("Input n: "))
s = calc(n)
print("When n == {}, Result is {}".format(n, s))
