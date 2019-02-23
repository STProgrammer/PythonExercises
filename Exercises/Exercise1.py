num = int(input("Type in a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("The number is a multiple of 4")
    else:
        print("The number is even, but not multiple of 4")
else:
    print("The number is odd")
