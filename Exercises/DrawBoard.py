def DrawBoard(h, w):
    print(" _" * w)
    for i in range(0, h):
        print("|_" * (w) + "|")
        i += 1

 

print("In this program you'll draw a game board")

h = input("Type in the height of the board: ")
w = input("Type in the width of the board: ")

h = int(h)
w = int(w)

DrawBoard(h, w)
