def get_winner(x,y):
    if game[x][y] == "|x":
        return 1
    elif game[x][y] == "|o":
        return 2


def is_winner(game):
    for i in range(0,3):
        if game[i][0] == game[i][1] == game[i][2]: #line win
            if game[i][0] != 0:
                return(get_winner(i,0))
        elif game[0][i] == game[1][i] == game[2][i]: #column win
            if game[0][i] != 0:
                return(get_winner(0,i))
        elif game[0][0] == game[1][1] == game[2][2]: #horizontal win "\"
            if game[0][0] != 0:
                return(get_winner(0,0))
        elif game[2][0] == game[1][1] == game[0][2]: #horizontal win "/"
            if game[2][0] != 0:
                return(get_winner(0,2))
    if 0 not in game[0] and 0 not in game[1] and 0 not in game[2]:
        return 0
    else:
        return 3

def PlayerMove(game, player):
    while True:
        coord1 = []
        if player == 1:
            print("Player one")
        elif player == 2:
            print("Player two")
        string1 = input("Please select coordinates in the form \"row,col\": ")
        coord1 = string1.split(",")          
        try:
            row = int(coord1[0]) - 1
            col = int(coord1[1]) - 1

            if game[row][col] != 0:
                print("The spot is full, try another coordinate")
                continue
            if player == 1:
                game[row][col] = "|x"
                Board[row + 1][col] = "|x"
            elif player == 2:
                game[row][col] = "|o"
                Board[row + 1][col] = "|o"
        except IndexError:
            print("The coordinates are out of range")
            continue
        except ValueError:
            print("The coordinates are not valid")
            continue
        return game

a = str()

while a != "q":
      
    print("Welcom to TicTacToe game!")


    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    Board = [[" _"," _"," _"],
         ["|_","|_","|_","|"],
         ["|_","|_","|_","|"],
         ["|_","|_","|_","|"]]

    for i in range(0,4):
        print("".join(Board[i]))

    player = 1

    winner = int(3) # if result is 0, no winners,
                    # if 1, player one wins, if 2 player two wins
                    # 3 is continue the game

    while winner == 3:
        game = PlayerMove(game, player)
        for i in range(0,4):
            print("".join(Board[i]))
        player = player % 2 + 1
        winner = is_winner(game)
        if winner == 0:
            print("There is no winner!")
        elif winner == 1:
            print("Player one won!")
        elif winner == 2:
            print("Player two won!")
    a = input(""""Do you want to play again?
(Press "q" to quit or any key to continue)""")
