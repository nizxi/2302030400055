# Q1: Program to ask for name and age, then print the year they will turn 100 years old

# Ask for user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculate the year they will turn 100
current_year = 2025  # You can use the current year dynamically as well
year_turn_100 = current_year + (100 - age)

# Print the message
print(f"Hello {name}! You will turn 100 years old in the year {year_turn_100}.")

# Q2: Ask the user for a number, and print whether it is even, odd, or multiple of 4
# Ask for a number
number = int(input("Enter a number: "))

# Check even, odd, and multiple of 4
if number % 4 == 0:
    print("This number is a multiple of 4.")
elif number % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")

# Q3: Given a list, print elements less than 5 and make a new list of them

# Given list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Create a new list with elements less than 5
new_list = [x for x in a if x < 5]

# Print the new list
print(new_list)
