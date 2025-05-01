# Q1: MySQL-Python Connectivity to Retrieve Data from city Table for Employees with ID Less Than 10

import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="your_database"  # Replace with your database name
)

cursor = db.cursor()

# Query to select employees with id less than 10 from city table
cursor.execute("SELECT * FROM city WHERE employee_id < 10")

# Fetch and display one record at a time
record = cursor.fetchone()
while record:
    print(record)
    record = cursor.fetchone()

# Close the connection
cursor.close()
db.close()