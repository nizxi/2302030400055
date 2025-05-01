def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
n = int(input("Enter a number: "))
print(even_or_odd(n))