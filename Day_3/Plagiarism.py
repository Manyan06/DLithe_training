from difflib import SequenceMatcher
text1 = input("Enter first text: ")
text2 = input("Enter second text: ")
similarity = SequenceMatcher(None, text1, text2).ratio()
percentage = similarity * 100
print("\n ---Plagiarism Checker--- ")
print("Similarity Percentage: ", round(percentage, 2), "%")
if percentage > 70:
  print("High Plagiarism detected")
elif percentage > 40:
  print("Moderate Plagiarism detected")
else:
  print("Low Plagiarism detected")