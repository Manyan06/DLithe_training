file = open("result.txt", "w")
name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))
file.write(f"Name: {name}\n")
file.write(f"Marks: {marks}\n")
if marks >= 40:
  file.write("Result: Pass")
else:
  file.write("Result: Fail")
file.close()
print("Result saved successfully")