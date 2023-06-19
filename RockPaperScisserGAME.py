import random
n = 1
m = int(input("Put how many rounds you wanna play:"))
userwin = 0
computerwin = 0
while(n<=m):
    lst = ["rock", "paper", "scisser"]
    computer = random.choice(lst)
    user = input("Enter your choice: ")
    if(computer == "rock" and user == "rock"):
        print("computer's choice is:", computer)
        userwin = userwin+0
        computerwin = computerwin+0
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif(computer == "rock" and user == "paper"):
        print("computer's choice is:", computer)
        userwin = userwin+1
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif(computer == "rock" and user == "scisser"):
        print("computer's choice is:", computer)
        computerwin = computerwin+1
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif (computer == "paper" and user == "rock"):
        print("computer's choice is:", computer)
        computerwin = computerwin+1
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif (computer == "paper" and user == "paper"):
        print("computer's choice is:", computer)
        userwin = userwin + 0
        computerwin = computerwin + 0
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif (computer == "paper" and user == "scisser"):
        print("computer's choice is:", computer)
        userwin = userwin+1
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif (computer == "scisser" and user == "rock"):
        print("computer's choice is:", computer)
        userwin =  userwin+1
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif (computer == "scisser" and user == "paper"):
        print("computer's choice is:", computer)
        computerwin = computerwin+1
        print("user Score is:", userwin, "Computer score is:", computerwin)
    elif (computer == "scisser" and user == "scisser"):
        print("computer's choice is:", computer)
        userwin = userwin + 0
        computerwin = computerwin + 0
        print("user Score is:", userwin, "Computer score is:", computerwin)
    else:
        print("wrong Input")
    n = n+1
    print()
print()
if(userwin>computerwin):
    print("FINAL SCORE OF COMPUTER IS:", computerwin)
    print("FINAL SCORE OF USER IS:", userwin)
    print("So USER WINS THE MATCH")
elif(userwin<computerwin):
    print("FINAL SCORE OF COMPUTER IS:", computerwin)
    print("FINAL SCORE OF USER IS:", userwin)
    print("So COMPUTER WINS THE MATCH")
else:
    print("FINAL SCORE OF COMPUTER IS:", computerwin)
    print("FINAL SCORE OF USER IS:", userwin)
    print("MATCH DRAW, PLAY AGAIN")


