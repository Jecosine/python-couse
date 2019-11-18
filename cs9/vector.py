import random, math

class Vector:
    def __init__(self, l):
        self.__value = l
        self.__length = len(l)
    def __getitem__(self, i):
        return self.__value[i]
    def length(self):
        return self.length
    def scale(self, n):
        return Vector([i * n for i in self.__value])
    def __add__(self, b):
        result = [self.__value[i] + b[i] for i in range(self.__length)]
        return Vector(result)
    def __sub__(self, b):
        c = [-i for i in b]
        return self.__add__(c)
    def __abs__(self):
        return math.sqrt(self.dot(self))
    def dot(self, b):
        result = [self.__value[i] * b[i] for i in range(self.__length)]
        return sum(result)
    def normalize(self):
        return Vector([i / self.__abs__() for i in self.__value])
    def __len__(self):
        return self.__length
    def __str__(self):
        return str(self.__value)

class sketch

if __name__ == "__main__":
    v1 = Vector((1,2))
    v2 = Vector((2,3))
    print("length of v1 is %s" % len(v1))
    print("v1 + v2 = %s" % (v1+v2))
    print("v1 · v2 = %s" % v1.dot(v2))
    print("|v1| = %s" %abs(v1))
    print("2v1 = %s" % v1.scale(2))
    
