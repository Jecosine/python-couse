# return index of left node
def left(i):
    return 2 * i
# return index of right node
def right(i):
    return 2 * i + 1
# return index of parent node
def parent(i):
    return i // 2
# minimalize heap
def minimal_heap(e, i):
    l = left(i)
    r = right(i)
    if l <= len(e) and e[i-1] > e[l-1]:
        minimal = l
    else:
        minimal = i
    if r <= len(e) and e[minimal-1] > e[r-1]:
        minimal = r
    if minimal != i:
        e[i-1], e[minimal-1] = e[minimal-1], e[i-1]
        e = minimal_heap(e, minimal)
    return e
# print heap
def print_heap(e):
    depth = 2
    i = 0
    while i < len(e):
        
        while(i < depth-1 and i < len(e)):
            print(str(e[i]).center(81 // depth), end='')
            i += 1
        print()
        depth *= 2
    
# build heap
def build_min_heap(e):
    for i in range(len(e), 0, -1):
        e = minimal_heap(e, i)
    return e

e = [9,21,2,4,5,2]
# print Tree
print("Print Origin")
print(e)
print_heap(e)

half = e[:len(e) // 2 + 1]
half = build_min_heap(half)
for i in range(len(e) // 2 + 1, len(e)):
    if half[0] < e[i]:
        half[0] = e[i]
        half = build_min_heap(half)
print("After build:")
print_heap(half)
def get_middle(e, half):
    if len(e) == 1:
        return e[0]
    if len(e) == 2:
        return sum(e)/2
    if len(e) % 2 != 0:
        return half[0]
    else:
        return (half[0] + min(half[1], half[2])) / 2

print("Middle is: {}".format(get_middle(e, half)))