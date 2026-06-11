print("===Email Slicer===")
email = input("Enter your email: ")

# Check if email contains @
if "@" in email:
  username, domain = email.split("@")
  print("Username:", username)
  print("Domain:", domain)
else :
  print("Invalid email format." "\nPlease include '@' .")