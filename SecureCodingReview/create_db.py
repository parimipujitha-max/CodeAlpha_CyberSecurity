import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
INSERT INTO users VALUES ('codealpha', '12345')
""")

conn.commit()

print("Database and users table created successfully!")