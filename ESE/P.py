# Describe class called Shape which has three subclasses say Triangle, Rectangle, Circle. Define one method area() in the abstract class and override this area() in these three subclasses to calculate for specific object i.e. area() of Triangle subclass should calculate area of triangle etc. Same for Rectangle and Circle. 
from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass: Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Subclass: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Subclass: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
triangle = Triangle(10, 5)
rectangle = Rectangle(4, 6)
circle = Circle(7)

print("Triangle Area:", triangle.area())
print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6. 
import numpy as np

# 3D array with two 2D arrays
array_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])

print("3D Array:")
print(array_3d)

# Explain format() method of string and placeholder with example.
name = "Alice"
age = 25

# Using format() with placeholders
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

# Write a python program to count the number of candidate from total 10 candidates whose weight is less than 60 kg and height is greater than 150 cm. Use if and for loop to create a program.
count = 0

# Input data for 10 candidates
for i in range(10):
    weight = float(input(f"Enter weight of candidate {i+1} (in kg): "))
    height = float(input(f"Enter height of candidate {i+1} (in cm): "))

    if weight < 60 and height > 150:
        count += 1

print("Number of candidates with weight < 60kg and height > 150cm:", count)
