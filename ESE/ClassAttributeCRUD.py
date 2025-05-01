# Write a python code to create a class and its object along with attributes. Access the attributes to create, update and delete
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# Create object
s1 = Student("John", 101)

# Access attributes
print("Name:", s1.name)
print("Roll No:", s1.roll_no)

# Update attributes
s1.name = "Alice"
s1.roll_no = 202
print("\nAfter Update:")
print("Name:", s1.name)
print("Roll No:", s1.roll_no)

# Delete attributes
del s1.roll_no
print("\nAfter Deletion:")
print("Name:", s1.name)
# print("Roll No:", s1.roll_no)  # This will give an error since it's deleted
