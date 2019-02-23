import random

print("Welcome to \"Rock Paper Scissor\" game")

print("""Type in "rock", "paper", or "scissor" and see who wins.
first one that win 10 times win the game.""")

HandsList = ["rock", "paper", "scissor"]

while True:
    x = int() #Your score
    y = int() #Computer's score

    while x < 10 and y < 10:
        hand1 = input("Type in your choice:" )
        hand2 = random.choice(HandsList)
        print(hand1, " - ",hand2)
        
        if hand1 == hand2:
            print("It's a tie!")
        elif hand1 == "rock":
            if hand2 == "scissor":
                  print("Rocks beats scissor. You score!")
                  x += 1
            else:
                print("Paper beats rock, computer scores!")
                y += 1
        elif hand1 == "paper":
            if hand2 == "rock":
                print("Paper beats rock, you score!")
                x += 1
            else:
                print("Scissor beats paper, computer scores!")
                y += 1
        elif hand1 == "scissor":
            if hand2 == "paper":
                print("Scissor beats paper, you score!")
                x += 1
            else:
                print("Rock beats scissor, computer scores!")
                y += 1
        else:
            print("""Invalid input. Plese type in:
    "rock", "paper" or "scissor".""")
            continue
        print("You: ", x, " - ", y, " computer")
        


    if x == 10:
        print("You win the game!")

    if y == 10:
        print("you lose the game!")

    print("Let's play again")
