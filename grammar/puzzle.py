import random
import time
random.seed(time.time())
answer = random.randint(1, 101)
count = 0
x = 0
print("Game Start")
while x != answer:
    count += 1
    x = int(input("Input your answer:"))
    if x == answer:
        print("猜对了")
    elif x > answer:
        print("小一点")
    else:
        print("大一点")
print("你猜了{0}次".format(count))
if count > 7:
    print("你的运气不好！")
else:
    print("好运气！")
