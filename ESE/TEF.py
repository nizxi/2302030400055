try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error! You can't divide by zero.")
finally:
    print("This will always run.")

# Initialize the list
my_list = [10, 20, 30, 40, 50]

# Insert an element at the beginning of the list
my_list.insert(0, 5)  # Insert '5' at the beginning

# Delete the element at index 3
del my_list[3]  # Delete element at index 3 (4th position)

# Print the modified list
print(my_list)