from random import randint
choice = ["rock", "paper", "scissors"]

computer = choice[randint(0,2)]

print ('Welcome to the Rock, Paper, Scissors Game \n')
player = input("Your choice: ").lower()
print ("Computer choice: ", computer)

if computer == player:
    print("Game is draw")
elif  



