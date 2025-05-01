# Q3: Program to Connect Python with MySQL and Display Students with Marks Greater Than 75
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your MySQL password
    database="your_database"  # Replace with your database name
)

cursor = db.cursor()

# Query to fetch students with marks greater than 75
cursor.execute("SELECT * FROM student WHERE marks > 75")

# Fetch and display records
records = cursor.fetchall()
for record in records:
    print(record)

# Close the connection
cursor.close()
db.close()
