alphabet = "abcdefghijklmnopqrstuvwxyz"
sentence = input("Enter the sentence: ").lower()
is_pangram = True
for ch in alphabet:
  if ch not in sentence:
    is_pangram = False
    break
if is_pangram:
  print("Pangram")
else:
  print("Not a Pangram")
