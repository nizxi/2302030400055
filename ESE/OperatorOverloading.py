class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Creating two Point objects
point1 = Point(2, 3)
point2 = Point(4, 5)

# Adding two Point objects using the overloaded + operator
result = point1 + point2

# Displaying the result
print(f"Result: ({result.x}, {result.y})")
