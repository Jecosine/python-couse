import random, time
def getRandom():
    random.seed(time.time())
    a = random.randrange(0, 101)
    b = random.randrange(0, 101)
    while(a == b):
        b = random.randrange(0, 101)
    return a, b

def getMax(a, b):
    if a < b:
        a, b = b, a
    m = a % b
    while m:
        a = b
        b = m
        m = a % b
    return b

def getMin(a, b):
    if a > b:
        a, b = b, a
    c, d = a, b
    while a != b:
        a += c
        if (a > b):
            a, b = b, a
            c, d = d, c
    return a
def test():
    word = input()
    word = word.strip().upper()
    s = input()
    print(word, s)
    s = [i.strip().upper() for i in s.split(" ")]
    i = s.count(word)
    if not i:
        print (-1)
    else:
        print ("{} {}".format(i, s.index(word)))

if __name__ == "__main__":
    test()
    # a, b = getRandom()
    # print("Random Value: {0} {1}".format(a, b))
    # print("Max divisor {0}, Min multiple {1}".format(getMax(a, b), getMin(a, b)))