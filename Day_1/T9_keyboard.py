def t9_mapping() :
  return {
    '2' : "ABC",
    '3' : "DEF",
    '4' : "GHI",
    '5' : "JKL",
    '6' : "MNO",
    '7' : "PQRS",
    '8' : "TUV",
    '9' : "WXYZ"
  }
def text_to_t9(text):
  mapping = t9_mapping()
  result = " "
  for char in text.upper():
    for key,value in mapping.items():
      if char in value:
        result += key
        break
  return result

#Input
word = "Hello"
print(f"T9 for {word} is :{text_to_t9(word)}")