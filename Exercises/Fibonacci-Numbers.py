def Fibonacci(num):
    Fibonacci = []
    if num > 100:
        print("Too large number, try again: ")
        return
    if num > 0:    
        Fibonacci.append(0)
    if num > 1:
        Fibonacci.append(1)
    if num > 2:
            for i in range(0, num-2):
                Fibonacci.append(Fibonacci[i] + Fibonacci[(i + 1)])
    print("\nThere are ",num," Fibonacci numbers: ")
    print(Fibonacci, " \n")
    return Fibonacci


print("This program prints Fibonacci numbers.")

while True:
    try:
        num = int(input("Type in how many Fibonacci numbers to print: "))
    except ValueError:
        print("Please type in a valid number!")
        continue

    Fibonacci(num)
