import math

class Shape:
    def area():
        pass

    def perimeter():
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def area(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))

    def perimeter(self):
        return self.l1 + self.l2 + self.l3

circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())