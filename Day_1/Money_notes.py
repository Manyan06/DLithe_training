amount = int(input("Enter the amount: "))
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
print("\nMinimum notes/coins required :")
for note in denominations:
  count = amount // note
  if count > 0 :
    print(f"{note} : {count}")
    amount %= note

#Enter the amount = 34343