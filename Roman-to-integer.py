class PySolutions:
    def roman_to_int(self, rnum):
        symb = ["IV", "IX", "XL", "XC",
                "CD", "CM","I", "V", "X",
                "L", "C", "D", "M"]
        nums = [4, 9, 40, 90, 400, 900,
                1, 5, 10, 50, 100, 500, 1000]
        number = int()
        rnum = rnum.upper()
        for i in range(0,6):
            if symb[i] in rnum:
                number += nums[i]
                rnum = rnum.replace(symb[i], "")

        for i in range(6,13):
            x = rnum.count(symb[i])  # x is number of a character in the string
            number += nums[i]*x
        return number

    def int_to_roman(self, num2):
        symb2 = ["I", "IV", "V", "IX",
                 "X", "XL","L", "XC",
                 "C", "CD", "D", "CM", "M"]
        nums2 = [1, 4, 5, 9, 10, 40, 50,
                 90, 100, 400, 500, 900, 1000]  
        roman = ""
        for i in range(1,14):
            x = num2 // nums2[-i]
            num2 -= nums2[-i]*x
            roman += symb2[-i]*x
        return roman    



    

while True:
    rnum = input("Type in roman number: ")
    num2 = input("Type in a number: ")
    num2 = int(num2)

    print(PySolutions().roman_to_int(rnum))
    print(PySolutions().int_to_roman(num2))




