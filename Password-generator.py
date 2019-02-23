import random
import pyperclip

print("Password generator")

Characters = "qwertyuiopasdfghjklzxcvbnm1234567890øæå,*^_:@£$€{[]}´<>.-|+§!§!#¤%&/()=?"

CharList = list(Characters)

CharList2 = list(CharList[0:36])

Answer = input("""Would you like to exclude special characters?
               (answer "yes" if so) """)

while True:
    PasswordChars = []
    try:
        Lenght = input("What will be the lenght of the password? ")
        Lenght = int(Lenght)
    except ValueError:
        print("Please type in valid input")
        continue

    if Answer == "yes":
        while Lenght > len(PasswordChars):
            char = random.choice(CharList2)
            PasswordChars.append(char)

    else:
        while Lenght > len(PasswordChars):
            char = random.choice(CharList)
            PasswordChars.append(char)
    Password = str()

    Password = "".join(PasswordChars)
    pyperclip.copy(Password)
    print(Password)
