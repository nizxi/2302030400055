# Q2: Program to Connect Python with MySQL and Display All Records from the student_2021 Table

import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="your_database"  # Replace with your database name
)

cursor = db.cursor()

# Query to fetch all records from student_2021 table
cursor.execute("SELECT * FROM student_2021")

# Fetch all records and display
records = cursor.fetchall()
for record in records:
    print(record)

# Close the connection
cursor.close()
db.close()