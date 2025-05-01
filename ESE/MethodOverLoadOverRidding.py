# Method Overloading Example (using default arguments)
class Calculator:
    # Method with default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

# Create Calculator object
calc = Calculator()

# Method overloading by passing different numbers of arguments
print(calc.add(5))         # Output: 5 (one argument)
print(calc.add(5, 3))      # Output: 8 (two arguments)
print(calc.add(5, 3, 2))   # Output: 10 (three arguments)


# Method Overriding Example (in a child class)
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")  # Overriding the sound method

# Create objects
generic_animal = Animal()
dog = Dog()

# Call overridden method
generic_animal.sound()  # Output: Some generic animal sound
dog.sound()             # Output: Woof! Woof!