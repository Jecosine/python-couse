import random

def gen():
    l = [i for i in range(11)]
    random.shuffle(l)
    la = random.randint(3, 8)
    lb = 10 - la
    offseta = random.randint(0, 11 - la)
    offsetb = random.randint(0, 11 - lb)
    A = {i for i in l[offseta:offseta + la]}
    B = {i for i in l[offsetb:offsetb + lb]}
    return A, B
def Show(n, A):
    l = len(A)
    mx = max(A)
    mn = min(A)
    print("{}: {} \nLen of {}: {}\nMaximum: {}\nMinimum: {}\n".format(n, str(A), n, l, mx, mn))

if __name__ == "__main__":
    A, B = gen()
    Show('A',A)
    Show('B',B)
    print("Union: {}\nIntersection: {}\nDifference: {}".format(str(A.union(B)), str(A.intersection(B)), str(A.difference(B))))


