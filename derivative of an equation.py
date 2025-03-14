import math
import cmath

a = float(input("enter the value of a:"))
b = float(input("enter the value of b:"))
c = float(input("enter the value of c:"))

delta = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(delta)) / (2*a)
root2 = (-b - cmath.sqrt(delta)) / (2*a)

print(f"roots of the equation: {root1} and {root2}")
