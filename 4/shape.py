import math
class Shape:
    def __init__(self, n):
        self.name = n
        self.area = 0.0
        self.perimater = 0.0
    # calculate cal
    def cal_area(self):
        pass
    def cal_perimater(self):
        pass
    def display(self):
        pass

class Rectangle(Shape):
    def __init__(self, n, a, b):
        super().__init__(n)
        self.a = a
        self.b = b
        self.area = self.cal_area()
        self.perimater = self.cal_perimater()
    def cal_area(self):
        self.area = self.a*self.b
        return self.area
    def cal_perimater(self):
        self.perimater = 2 * (self.a + self.b)
        return self.perimater
    def display(self):
        print("名称是 {}\n面积是 {:.2f}\n周长是 {:.2f}\n".format(self.name, self.area, self.perimater))


class Circle(Shape):
    def __init__(self, n, a):
        super().__init__(n)
        self.a = a    
        self.area = self.cal_area()
        self.perimater = self.cal_perimater()
    def cal_area(self):
        self.area =  math.pi * self.a * self.a
        return self.area
    def cal_perimater(self):
        self.perimater = 2 * math.pi * self.a
        return self.perimater
    def display(self):
        print("名称是 {}\n面积是 {:.2f}\n周长是 {:.2f}\n".format(self.name, self.area, self.perimater))
    

if __name__ == "__main__":
    c1 = Circle("circle1", 3)
    r1 = Rectangle("rect1", 4, 7)
    c1.display()
    r1.display()
