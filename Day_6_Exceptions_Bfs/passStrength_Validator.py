class PasswordError(Exception):
    pass           #allow code to enter try block 
try :
  password = input("Enter the password: ")
  if len(password) < 8 :
    raise PasswordError(
      "Password must contain atleast 8 characters."
    )
  
  if not any(char.isupper() for char in password):
     raise PasswordError(
      "Password must contain atleast one uppercase letter."
    )
  
  if not any(char.isdigit() for char in password):
     raise PasswordError(
      "Password must contain atleast one digit."
    )
  
  print("Strong Password Accepted")

except PasswordError as e:
   print("Password Error: ", e)
finally:
   print("Password Validation Completed")