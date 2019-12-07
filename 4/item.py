s = [10, 12, 15, 11, 14]
w = [210, 240, 270, 230, 300]
items = {}
for i, j in zip(s, w):
    v = j / i
    items[v] = i
sorted_value = sorted(items.keys(), key = lambda k:k, reverse = True)
method = {}
for i in sorted_value:
    method[i] = [0, int(i*items[i])]
# print(sorted_value)
# print(items)
result = 0
total = 48

while(total):
    for i in sorted_value:
        if items[i]:
            method[i][0] += 1
            items[i] -= 1
            result += i
            break
    total -= 1

print("Method:")
for i in method.keys():
    print("Get {}g of value {}".format(method[i][0], method[i][1]))
# print(result)
print("Finally: {}".format(result))