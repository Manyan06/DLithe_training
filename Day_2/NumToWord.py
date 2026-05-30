def number_to_words(num):
  ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
  teens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
  tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
  if num == 0:
    return "Zero"
  words = " "

  #thousands
  if num >= 1000:
    words += ones[num // 1000] + "Thousand"
    num %= 1000

  #Hundreds
  if num >= 100:
    words += ones[num//100] + "Hundred"
    num %= 100

  #Tens & Ones
  if num >= 20:
    words += tens[num//10]+""
    num %= 10
  elif num >= 10:
    words += teens[num-10]+""
    num = 0
  if num > 0:
    words += ones[num]
  return words.strip()

number = int(input("Enter an integer: "))
print("In words: ",number_to_words(number))