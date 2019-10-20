def selectNums(l, n):
    r = []
    if n == 1:
        return [str(i) for i in l]
    for i in range(len(l)):
        bl = l[:]
        bl.pop(i)
        for j in selectNums(bl, n-1):
             r.append(str(l[i]) + j)
    return r

if __name__ == "__main__":
    result = selectNums([1,2,3,4], 3)
    print("Count: {0}".format(len(result)))
    for i in result:
        print(i, end=" ")


