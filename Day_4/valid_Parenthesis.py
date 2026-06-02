def is_valid_parenthesis(s):
  stack= []
  brackets = {
    ')' :'(',
    '}' :'{',
    ']' : '['
  }
  for char in s:
    if char in "({[":
      stack.append(char)
    elif char in ")}]":
      if not stack or stack[-1] != brackets[char]:
        return False
      stack.pop()
  return len(stack) == 0
print("Valid Parenthesis")
print("Examples")
print("()")
print("()[]{}")
print("(]")
print("([{}])")
print("(((")
print()
s = input("Enter the parenthesis string: ")
if is_valid_parenthesis(s):
  print("True")
else:
  print("False")