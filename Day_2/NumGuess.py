import random
number = random.randint(1000,10000)
guess = 0
attempts = 0
print("Guess a number between 1000 and 10000")
while guess != number:
  try:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < 1000 or guess > 10000:
      print("Enter number between 100 and 1000: ")
    elif guess < number:
      print("Too Low")
    elif guess > number:
      print("Too High")
    else:
      print("Correct Number")
      print(f"Attempts: {attempts}")
  except ValueError:
    print("Invalid input. Please enter a number")