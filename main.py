from tkinter.messagebox import YES


print("Welcome to the Quiz game")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()  #function in python to execute the code
print("Lets get started")
s = 0

answer = input("What does CPU stand for ")
if answer.lower() == "central processing unit":
    print("correct!")
    s+=1
else:
    print("Sorry wrong answer")
answer = input("What does MU stand for ")
if answer.lower() == "memory unit":
    print("correct!")
    s+=1
else:
    print("sorry wrong answer")
answer = input("What does CAD stand for ")
if answer.lower() == "computer aided design":
    print("correct!")
    s+=1
else:
    print("sorry wrong answer")
answer = input("What does GPU stand for ")
if answer.lower() == "gaming Processing Unit":
    print("correct!")
    s+=1
else:
    print("sorry wrong answer")
print("You got "+ str(s) + " correct")
print("You got "+ str((s/4)*100) + " %" +" correct")
