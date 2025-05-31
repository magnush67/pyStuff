import random

a = random.randint(1, 10000)
b = random.randint(1, 10000)
c = random.randint(1, 10000)

print(f"Random values: a = {a}, b = {b}, c = {c}")

# Determine which variable has the largest number
if a > b and a > c:
    largest = a
    variable_name = 'a'
elif b > a and b > c:
    largest = b
    variable_name = 'b'
else:
    largest = c
    variable_name = 'c'

print(f"The largest number is {largest} (variable {variable_name})")

