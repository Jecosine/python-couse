n = int(input("Input n: "))
def f(max):
    i, a, n = 1, 0, 1
    while (i < max):
        a, n = n, a + n
        i += 1
    return n 
print ("The Nth is :{0}".format(f(n)))
