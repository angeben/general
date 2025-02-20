import sqlite3

# Open connection
connection = sqlite3.connect('users.db')

# Create cursor
cursor = connection.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users(" +
               "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
               "name VARCHAR(255)," +
               "email VARCHAR(100)," +
               "age INTEGER"
               ")")

# Save changes
connection.commit()

# Insert data
cursor.execute("INSERT INTO users VALUES (null, 'Peter', 'peter@gmail.com', 24)")
cursor.execute("INSERT INTO users VALUES (null, 'Sarah', 'sarah@gmail.com', 22)")
cursor.execute("INSERT INTO users VALUES (null, 'Dave', 'dave@gmail.com', 27)")
insert_users = [
    ('John', 'john@gmail.com', 20),
    ('Cindy', 'cindy@gmail.com', 25)
]
cursor.executemany("INSERT INTO users VALUES (null, ?, ?, ?)", insert_users)
connection.commit()

# Update data
cursor.execute("UPDATE users SET age=24 WHERE name='Dave'")

# Read data
cursor.execute("SELECT * FROM users WHERE age >= 20")
users = cursor.fetchall()
for user in users:
    print(user)

# Close connection
connection.close()