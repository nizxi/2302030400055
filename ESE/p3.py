# Q11: Multiple Inheritance - Ferrari, Benz → Car

class Ferrari:
    def ferrari_feature(self):
        print("Ferrari: Fast and sporty.")

class Benz:
    def benz_feature(self):
        print("Benz: Luxury and comfort.")

class Car(Ferrari, Benz):
    def display(self):
        print("This is a Car that combines both Ferrari and Benz features.")

# Create an object of Car
my_car = Car()
my_car.display()
my_car.ferrari_feature()
my_car.benz_feature()

# Take input from the user
num = float(input("Enter a number: "))

# Check conditions
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
