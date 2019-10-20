import math
def get_factors(x):
    sum = 0
    for i in range(1, x // 2 + 2):
        if x % i == 0:
            sum += i
    return sum

for i in range(2, 1001):
    if i == get_factors(i):
        print(i)
