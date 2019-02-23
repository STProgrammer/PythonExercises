Numbers = [1, 5, 34, 7, 23, 5, 9, 45, 92, 54,
           13, 32, 73, 69, 21, 24, 64, 57, 24]
    

while True:
    answer = input("guess a number: (or press \'q\' to quit)")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a numbner or q to quit.")
        continue
    if answer in Numbers:
        print("Your guessed correctly!")
    else:
        print("You guessed wrong, try again")        

