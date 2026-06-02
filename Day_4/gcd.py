#Eucledian Algorithm

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

num1 = int(input("First Num: "))
num2 = int(input("Second Num: "))
result = gcd(num1,num2)
print("Result: ",result)