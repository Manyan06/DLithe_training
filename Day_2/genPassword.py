import random
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz" 
digits = "0123456789"
special = "*!@#$%^&*()_+-=[]{|;:,.<>?/}"
length = int(input("Enter password length(minimum 8): "))
if length<8 :
  print("Password must be at least 8 characters long.")
else:
  password=[
    random.choice(uppercase), #random = library & choice = function
    random.choice(lowercase),
    random.choice(digits),
    random.choice(special)
  ]
  all_characters = uppercase+lowercase+digits+special
  for i in range(length-4):
    password.append(random.choice(all_characters))
  random.shuffle(password)
  password = "".join(password)
  print("Generated Pass: ",password)