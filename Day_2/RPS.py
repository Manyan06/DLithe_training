import random

comp = random.choice(["rock","paper","scissor"])
print("Computer's choice: ",comp)
player = input("Enter you choice (Rock,Paper,Scissor): ").lower()
if comp == "rock" and player == "paper" :
  print("Player wins")
elif comp == "scissor" and player == "rock" :
  print("Player wins")
elif comp == "paper" and player == "scissor" :
  print("Player wins")
elif comp == player :
  print("Its a tie")
else:
  print("Computer wins")