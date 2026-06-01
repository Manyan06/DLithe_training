print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius ")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter choice (1-6): "))
temp = float(input("Enter Temperature: "))

if choice == 1:
  print(f"{temp} Celsius = {temp * (9/5) + 32:.2f} Fahrenheit")
elif choice == 2:
  print(f"{temp} Fahrenheit = {temp * (5/9) - 32:.2f} Celsius")
elif choice == 3:
  print(f"{temp} Celsius = {temp + 273.15:.2f} Kelvin")
elif choice == 4:
  print(f"{temp} Kelvin = {temp - 273.15:.2f} Celsius")
elif choice == 5:
  print(f"{temp} Fahrenheit = {(temp - 32)* (5/9) + 273.15:.2f} Kelvin")
elif choice == 6:
  print(f"{temp} Kelvin = {(temp - 273.15)* (9/5) + 32:.2f} Fahrenheit")
else:
  print("Invalid Choice")