from random import randint
choice = ["rock", "paper", "scissors"]

# p1 = input("Player 1 Name: ")
# p2 = input("Who is player 2? ")
p2 = "Computer"

print("Ananya vs", p2)

c1 = input("Ananya, Pls choose among: Rock, Paper, or Scissors? :").lower()
# print(c1)
# c2 = input("Player 2: rock, paper, or scissors? ")
c2 = choice[randint(0,2)]
print(p2, "choose: ", c2)

if (c1 == 'r') & (c2 == 'rock') | (c1 == 'p') & (c2 == 'paper') | (c1 == 's') & (c2 == 'scissors'):
    print("Draw!")
elif (c1 == 'r') & (c2 == 'scissors') | (c1 == 'p') & (c2 == 'rock') | (c1 == 's') & (c2 == 'paper'):
    print("Ananya Wins!")
elif (c2 == "rock") & (c1 == 's') | (c2 == 'paper') & (c1 == 'r') | (c2 == 'scissors') & (c1 == 'p'):
    print(p2, 'Wins!')
else:
    print("Pls choose an invalid option. Try again using rock, paper, or scissors")