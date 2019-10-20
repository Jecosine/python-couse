import random, time

def get_rand(n):
    random.seed(time.time())
    r = []
    while n > 0:
        n -= 1
        r.append(random.randint(-100, 100))
    return r

if __name__ == "__main__":
    r = get_rand(20)
    print("Instaniate 20 random int:")
    max = r.max()
    min = r.min()
    sum = r.sum()
    a = sum / 20.0
    odd = [i for i in r if i % 2 != 0]
    oddc = len(odd)
    odds = sum(odd)
    print("\nMax: %d\tMin: %d\t\nSum: %d\tAverage: %.2f\nOdd count: %d\t Odd Average: %.2f" % (max, min, sum, a, oddc, odds))
    min = abs(r[0] - a);
    index = 0
    for i in range(20):
        if abs(float(r[i])-a) < min:
            min = abs(r[i] - a)
            index = i
    print("Most approach is the {}th element: {}".format(index, r[index]))
