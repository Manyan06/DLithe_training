from datetime import datetime
name = input("Enter Customer Name: ")
rating = int(input("Enter Rating (1-5): "))
feedback = input("Enter Feedback: ")
time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
file = open("feedback.txt", "a")
file.write(
  f"Name: {name} | "
  f"Rating: {rating} | "
  f"Feedback: {feedback} | "
  f"Date: {time}\n"
)
file.close()
print("\nThank you for your Feedback!")