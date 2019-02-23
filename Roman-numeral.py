class RomanNumber:
    symb2 = ["I", "IV", "V", "IX", "X", "XL",
             "L", "XC", "C", "CD", "D", "CM", "M"]

    nums2 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    def __init__(self, number):
        self.roman = ""
        self.value = number
        self.number = number
        for i in range(1,14):
            x = self.number // self.nums2[-i]
            self.number -= self.nums2[-i]*x
            self.roman += self.symb2[-i]*x

    def __repr__(self):
        return self.roman

    def __gt__(self, r2):
        if self.value > r2.value:
            return True
        else:
            return False

    def __lt__(self, r2):
        if self.value < r2.value:
            return True
        else:
            return False

    def __add__(self, r2):
        num = (self.value + r2.value)
        return RomanNumber(num)
        

while True:
    try:
        num = input("Type in a number: ")
        num = int(num)
    except ValueError:
        print("Please type in an integer")
        continue

    rum1 = RomanNumber(num)
    print(rum1)
    rum2 = RomanNumber(num)
    print(rum2)

    rum3 = rum1 + rum2

    print(rum1, "+",rum2, "=",rum3)
