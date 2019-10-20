import math
def calc(a, b, c):
    l = [a, b, c]
    l.sort()
    a, b, c = l
    if a + b <= c:
        return False, 0, 0
    C = a + b + c
    p = C / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return True, C, S

if __name__ == "__main__":
    a = float(input("Input a:"))
    b = float(input("Input b:"))
    c = float(input("Input c:"))
    _ , C, S = calc(a, b, c)
    if _:
        print("C is {0}, S is {1}".format(C, S))
    else:
        print("Imposible")