PrimeNumbers = int()

while True:
    print("""You'll type in two numbers and the program
    will find all the prime number between these two number \n""")
    PrimeNumbers = 0
    try:
        FirstNumber = int(input("Type in your first number: "))
        LastNumber = int(input("Type in your last number: "))
    except ValueError:
        print("Opps! That was not a valid number. Try again.")
        continue

    for num in range(FirstNumber, LastNumber + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)
                PrimeNumbers += 1

    print("""There are """, PrimeNumbers, """prime numbers between \
""", FirstNumber, """ and """, LastNumber, """ \n """)
