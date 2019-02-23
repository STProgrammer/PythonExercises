import math

class PySolutions():
    def __init__(self):
        self.string = ""
    def get_String(self):
        self.string = input("Type in something: ")

    def print_String(self):
        print(self.string.upper())

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def find_Area(self):
        area = self.length * self.width
        return area

class Circle():
    def __init__(self, radius):
        self.r = radius

    def get_Area(self):
        area = self.r**2 * math.pi
        return round(area, 2)
    def get_Perimeter(self):
        perimeter = 2*self.r*math.pi
        return round(perimeter, 2)




string = PySolutions()

string.get_String()

string.print_String()

C1 = Circle(5)

print(C1.get_Area())
print(C1.get_Perimeter())
