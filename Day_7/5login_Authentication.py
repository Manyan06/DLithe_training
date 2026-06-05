from datetime import datetime
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "python123"
attempts = 3

while attempts > 0:
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  login_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
  if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
    file = open("login_log.txt", "a")
    file.write(
      f"Username: {username} | "
      f"Status: SUCCESS | "
      f"Login Time: {login_time}\n"
    )

    file.close()
    print("\nLogin Successfull")
    print("Welcome,", username)
    break
  else:
    attempts -= 1

    file = open("login_log.txt", "a")
    file.write(
      f"Username: {username} | "
      f"Status: FAILED | "
      f"Login Time: {login_time}\n"
    )
    file.close()
    print("\nInvalid Username or Password")
    print("Attempts Remaining: ",attempts)

if attempts == 0:
  print("\nAccount Locked!" "Too many failed attempts")