def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

# Print factorials from 1 to 10
for n in range(1, 11):
    print(f"Factorial of {n} is {factorial(n)}")


# Recursive Factorial Function
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")