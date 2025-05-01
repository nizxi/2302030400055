# Step 1: Define a Class
class Person:
    # Constructor (__init__) to initialize the object with attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display the person's details
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Step 2: Create an Object (instance of the class)
person1 = Person("John", 30)

# Step 3: Invoke the Method
person1.greet()  # This will call the greet() method and display the message

# # Define the class
# class Person:
#     def greet(self):
#         print("Hello!")

# # Create an object
# person1 = Person()

# # Call the method
# person1.greet()
