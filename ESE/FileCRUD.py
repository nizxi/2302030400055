import os

# Create and write to the file
with open("myfile.txt", "w") as file:
    file.write("My name is OldName")

# Update the content and write it back
with open("myfile.txt", "r+") as file:
    content = file.read()
    content = content.replace("OldName", "John")
    file.seek(0)
    file.write(content)

# Read and print the updated content
with open("myfile.txt", "r") as file:
    print("Updated content:", file.read())

# Delete the file
os.remove("myfile.txt")

#### read and update your name in file
# Open the file in read mode and check its current content
with open('name.txt', 'r') as file:
    content = file.read()

# Print the current content of the file (optional)
print("Current content in the file:", content)

# Update your name in the content
updated_content = content.replace("Old Name", "New Name")

# Write the updated content back to the file
with open('name.txt', 'w') as file:
    file.write(updated_content)

print("Your name has been updated in the file.")
