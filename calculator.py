
import re;

ans = 0
run = True

print ("Type 'quit' to Close Calculator")

def getUserInput():
    global  run
    global  ans
    userInput = ""
    if ans == 0:
        userInput = raw_input("Enter Your Equation:")
    else:
        userInput = raw_input(str(ans))

    if userInput == 'quit':
        run = False
    else:
        userInput = re.sub('[a-zA-Z,.:()~!@#$%^&*()_=;<>?/|{}" "]', '', userInput)
        if ans == 0:
            ans = eval(userInput)
        else:
            ans = eval(str(ans) + userInput)

while run:
    getUserInput()


