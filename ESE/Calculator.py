# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Displaying menu options
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

# Taking the user's choice
choice = input("Enter choice (1/2/3/4): ")

# Performing the operation based on the user's choice
if choice == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif choice == '4':
    if num2 != 0:  # Check to prevent division by zero
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid input! Please choose a valid operation.")
