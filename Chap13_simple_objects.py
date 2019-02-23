class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("I'm a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return 2*self.width + 2*self.len

class Square(Shape):
    def __init__(self,s):
        self.side = s
    def calculate_perimeter(self):
        return 4*self.side
    def change_size(self, num):
        self.side += num

class Horse():
    def __init__(self,name,h,r):
        self.name = name
        self.height = h
        self.rider = r

class Rider():
    def __init__(self, name, age):
        self.age = age
        self.name = name


a_rider = Rider("George", 25)

a_horse = Horse("At",350,a_rider)

print(a_horse.rider.name)

rec = Rectangle(3,6)
print(rec.calculate_perimeter())
rec.what_am_i()

square = Square(5)
print(square.calculate_perimeter())
square.what_am_i()
    
square.change_size(1)
print(square.calculate_perimeter())
