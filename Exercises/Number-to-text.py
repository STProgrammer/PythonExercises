def Hundreds(num):
    strhundred = str()
    if 1000 > num >= 100:
        num2 = num//100
        if num2 == 1:
            strhundred += Ones[(num2)]
            strhundred += Hundred + " "
        else:
            strhundred += Ones[(num2)]
            strhundred += Hundred + "s "
            
    num = num - num//100*100

    if 0 < num < 20:
        strhundred += Ones[(num)]

    if 100 > num >= 20:
        num2 = num // 10
        strhundred += Tens[(num2-1)]
        num2 = num % 10
        strhundred += Ones[(num2)]

    return strhundred

Ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ",
        "ten ", "elleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ", "nineteen "]

Tens = ["", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ",
        "eighty ", "ninety "]

Hundred = "hundred"

Big = ["thousand", "million", "billion"]


while True:
    

    try:
        num = int(input("type in a number between 0 and 999,999,999,999: "))
    except ValueError:
        print("Plese type in a valid input \n")
        continue
    string = str()
    if num == 0:
        string = "zero"
    if num >= 1000000000:
        num2 = num // 1000000000
        if num2 == 1:
            string += Ones[(num2)] + Big[2]
        else:
            string += Hundreds(num2) + Big[2] + "s"
        if (num % 1000000000) != 0:
            string += " and "
            
    num = num - num//1000000000*1000000000

    if num >= 1000000:
        num2 = num // 1000000
        if num2 == 1:
            string += Ones[(num2)] + Big[1]
        else:
            string += Hundreds(num2) + Big[1] + "s"
        if (num % 1000000) != 0:
            string += " and "

    num = num % 1000000

    if num >= 1000:
        num2 = num // 1000
        if num2 == 1:
            string += Ones[(num2)] + Big[0]
        else:
            string += Hundreds(num2) + Big[0] + "s"
        if (num % 1000) != 0:
            string += " and "

    num = num % 1000

    string += Hundreds(num)

    print(string, "\n")
