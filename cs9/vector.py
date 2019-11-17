import random

class Vector:
    def __init__(self, l):
        self.__value = l
        self.__length = len(l)
    def __getitem__(self, i):
        return self.l[i]
    def length(self):
        return self.length
    def __add__(self, b):
        result = [self.__value[i] + b[i] for i in range(self.__length)]s
        return Vector(result)
    def __sub__(self, b):
        c = [-i for i in b]
        return self.__add__(c)
    def __abs__(self):
        return math.sqrt(self.dot(self))
    def dot(self, b):
        result = [self.__value[i] + b[i] for i in range(self.__length)]
        return sum(result)
    
    def normalize(self):
        return Vector([i / self.__abs__() for i in self.__value])
    
    def __len__(self):
        return self.__length
    def __str__(self):
        return str(self.__value)

class Sketch:
    
