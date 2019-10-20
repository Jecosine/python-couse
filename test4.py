import random
n = random.randrange(1, 11)
s = 0
for i in range(n):
    s += (n - i) * pow(10, i)
print("Random n: {0}\nSum: {1}".format(n, s))