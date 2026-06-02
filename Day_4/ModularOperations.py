a = int(input("Enter First num: "))
b = int(input("Enter Second num: "))
m = int(input("Enter Modulus value: "))
mod_add = ((a % m) + (b % m)) % m
mod_sub = ((a % m) - (b % m) - m) % m
mod_mul = ((a % m) * (b % m)) % m

print("Modular_add: ",mod_add)
print("Modular_sub: ",mod_sub)
print("Modular_mul: ",mod_mul)