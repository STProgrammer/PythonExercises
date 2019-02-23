import random

def HangMan(Word):
    print("Welcome to Hangman game \n")
    Figure = ["",
              "___________         ",
              "|         |         ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    Word2 = list(Word) #Turning the word into a list to make assignment easier
    Lines = len(Word) * ["_"]
    print(" ".join(Lines),"\n")
    e = int(1) # Number of errors, starting from 1 for practial reasons
    while e < 8:
        Letter = input("\nGuess a letter: ")
        if Letter in Word2:
            while Letter in Word2:
                i = int(Word2.index(Letter))
                Lines[i] = Letter
                Word2[i] = "$"
        else:
            e += 1
        print(" ".join(Lines))
        print("\n".join(Figure[0:e]))
        if e >= 8:
            print("You lost the game. The word was: ",Word)
            return False
        if "_" not in Lines:
            print("You win the game. The word was: ", Word)
            return True

WordsList = ["cat","dog","city","computer","software","programming","bastard",
             "bitch","president","country","tourist","travel","opportunity",
             "economics","money","finances","inflation","deflation","cost",
             "mathematics","psychology","sociology","history","physics","fish",
             "zebra","elephant","giraffe","domain","doctor","professor","sport",
             "example","Python","universal","follow","random","word","negative",
             "positive","printing","input","output","engineering","astronomy",
             "logic","philosophy","numbers","panel","controls","cards","rat",
             "politics","sick","healthy","wealthy","happy","sad","angry","fat",
             "fit","soccer","rugby","awkward","silence","social","equivalent"
             "code","loop","glitch","bug","compiler","interpreter","virtual"]



a = str()

while a != "q":
    Word = random.choice(WordsList)
    HangMan(Word)
    a = input("Press 'q' to quit, or press any key to continue")


