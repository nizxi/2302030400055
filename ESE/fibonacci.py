def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example: Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci_recursive(i))
