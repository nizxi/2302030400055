def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Example usage:
n = int(input("Enter a number: "))
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
