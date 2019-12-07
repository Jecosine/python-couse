# filename:mymodel.py
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def myprint(mydata):
    for i in mydata:
        print(i)

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)