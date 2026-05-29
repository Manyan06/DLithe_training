print("BMI Calculator")
height = float(input("Enter height in m: "))
weight = float(input("Enter weight in kg: "))
# BMI = height/(weight^2)
BMI = weight/(height*height)
print(f"BMI is :{BMI:.2f}")

if BMI < 18.5 :
  print("Underweight")
elif BMI >= 18.5 and BMI <24.9 :
  print("Normal")
elif BMI >= 24.9 and BMI < 29.9 :
  print("Overweight")
else:
  print("Obese")
