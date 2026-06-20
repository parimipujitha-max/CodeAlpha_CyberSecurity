import sqlite3
import hashlib

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

hashed_password = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, hashed_password))

if cursor.fetchone():
    print("Login Successful")
else:
    print("Invalid Credentials")
    