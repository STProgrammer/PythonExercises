import math

class Apple:
    def __init__(self, w, c, land, worm):
        self.weight = w
        self.color = c
        self.country = land
        self.worm = worm
    def getinfo(self):
        print("A",self.color,"apple weighing",self.weight,
              "grams, from the country ",self.country)
        if self.worm:
            print("The apple has a worm inside it")



apple = Apple(30,"green","Norway",True)

apple.getinfo()

class Circle:
    def __init__(self,r):
        self.radius = r
    def area(self):
        return int(self.radius**2 * math.pi)

circle = Circle(15)

print("The area of the circle is",circle.area())


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return int((self.height * self.base)/2)

triangle = Triangle(4,5)
    
print("The area of the triangle is",triangle.area())


class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

hexagon = Hexagon(5,5,6,4,3,4)

print("The perimeter of the hexagon is",hexagon.calculate_perimeter())
    
