count = 0
num = 2

while count < 10:
    print(num)
    num += 2
    count += 1

# Print 10 elements using a for loop.
# for i in range(1, 11):
#     print(i)


#Write a Program to print letters of string “Silver Oak University” except e and s.
text = "Silver Oak University"
for char in text:
    if char.lower() not in ['e', 's']:
        print(char, end="")
