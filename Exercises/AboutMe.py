AboutMe = dict()

AboutMe = {"height": "182 cm",
           "name": "Abdullah Karagøz",
           "weight": "70 Kg",
           "birth year": "1988",
           "education": "vocational college",
           "current occupation": "student",
           "area of study": "economics",
           "age": "30",
           "status": "single"
           }

print("Answer \"q\" to quit")

Ask = str()

while Ask != "q":

    Ask = input("What do you want to know about me? ")

    if Ask in AboutMe:
        print("My",Ask,"is",AboutMe[Ask])
    else:
        print("No information about",Ask,"here.")

    

Words = {"letters": ["A", "B", "C", "D", "E", "F"],
             "numbers": [1,2,3,4,5,6,7,8,9],
             "colors": ["red", "green", "blue", "yellow", "orange"],
             "adjectives": ["big","small","nice","beautiful","smart"],
             "cities": ["Istanbul","Oslo","Drammen","Konya","Beysehir"],
             "subjects": ["economics","psychology","math","physics","history",
                          "computer science","programming"]
             }

print("Answer \"q\" to quit")

Ask = str()

while Ask != "q":
    Ask = input("Type something: ")
    if Ask == "q":
        break
    try:
        n = input("Type a number: ")
        n = int(n)
        if Ask in Words:
            Lists = Words[Ask][n]
            print(Lists)
        else:
            print("Not found!")
    except: ValueError
    print("Please type in number: ")
    continue
