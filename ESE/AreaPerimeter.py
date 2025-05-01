# Q1: Write a Python program to find the area of a circle. (3 CO1)
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print(f"Area of the circle is: {area:.2f}")

# Q2: Write a Python program to find the perimeter of a rectangle. (3 CO1)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
print(f"Perimeter of the rectangle is: {perimeter}")