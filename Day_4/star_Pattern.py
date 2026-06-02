def half_pyramid(rows):
  for i in range(1,rows + 1):
    print("* " * i)
def full_pyramid(rows):
  for i in range(1,rows + 1):
    print(" " * (rows - i) + "* " * i)
def diamond(rows):
  # Upper half
  for i in range(1,rows + 1):
    print(" " * (rows - i) + "* " * i)
  # Lower half
  for i in range(rows - 1, 0 , -1):
    print(" " * (rows - i) + "* " * i)

#Main program
print("Choose a pattern: ")
print("1. Half Pyramid")
print("2. Full Pyramid")
print("3. Diamond")

choice = int(input("Enter your choice: "))
rows = int(input("Enter number of rows: "))

if choice == 1:
  half_pyramid(rows)
elif choice == 2:
  full_pyramid(rows)
elif choice == 3:
  diamond(rows) 
else :
  print("Invalid choice!")