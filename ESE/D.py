# Q13: MySQL Connection and Database Creation
# Make sure you have mysql-connector-python installed:
# pip install mysql-connector-python

import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS college")
cursor.execute("SHOW DATABASES")

# Check if 'college' is in the list
for db in cursor:
    print(db)

conn.close()