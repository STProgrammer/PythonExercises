class ParantheseCheck:   
    def check_validity(text):
        parlist = ["(","[","{","}","]",")"]
        pars = [x for x in text if x in parlist]
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for paranthese in pars:
            if paranthese in pchar:
                stack.append(paranthese)
            elif len(stack) == 0 or pchar[stack.pop()] != paranthese:
                return False
        return len(stack) == 0



while True:
    text = input("Type in text: ")
    if ParantheseCheck.check_validity(text) == True:
        print("The parantheses are in correct order")
    else: print("The parantheses are in wrong order")
