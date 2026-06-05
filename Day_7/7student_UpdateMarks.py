file = "students.txt"
while True:
  ch = input("\n1. Add 2. View 3. Search 4. Update 5. Delete 6. Exit\n")
  if ch == "1" :
    open(file, "a").write(input('Roll: ') + "," + input("Name: ") + "\n")
  elif ch == "2":
    print(open(file, "r").read())
  elif ch == "3":
    roll = input("Roll: ")
    for line in open(file):
      if line.startswith(roll + ","):
        print(line)
  elif ch == "4":
    roll = input("Roll ")
    name = input("Name ")
    data = open(file).readlines()
    open(file, "w").writelines([f"{roll},{name}\n" if x.startswith(roll + ",") else x for x in data])
  elif ch == "5":
    roll = input("Roll:")
    data = open(file).readlines()
    open(file, "w").writelines([x for x in data if not x.startswith(roll + ",")])
  else:
    break