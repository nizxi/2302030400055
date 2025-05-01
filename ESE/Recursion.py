def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

# Example usage:
result = sum_recursive(5)
print(f"Sum from 1 to 5 is {result}")
