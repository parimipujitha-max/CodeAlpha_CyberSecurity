import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

cursor.execute(query)

if cursor.fetchone():
    print("Login Successful")
else:
    print("Invalid Credentials")