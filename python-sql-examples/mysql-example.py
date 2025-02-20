import mysql.connector

# Connection
database = mysql.connector.connect(
    host="localhost",
    user="*********",
    passwd="*********",
    database="python"
)
cursor = database.cursor()

# Create tables
cursor.execute("CREATE DATABASE IF NOT EXISTS python")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id int(10) auto_increment not null,
        email varchar(40) not null,
        name varchar(40) not null,
        age int(10),
        CONSTRAINT pk_user PRIMARY KEY(id)
    )
""")

# Clear database
cursor.execute("DELETE FROM users")

# Insert values
cursor.execute("INSERT INTO users VALUES(null, 'peter@peter.com', 'Peter', 23)")
users = [
    ('John', 'john@gmail.com', 20),
    ('Cindy', 'cindy@gmail.com', 25)
]
cursor.executemany("INSERT INTO users VALUES(null, %s, %s, %s)", users)
database.commit()