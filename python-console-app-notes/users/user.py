import datetime
import hashlib
import users.connection as connection

# Establish connection to DB
connect = connection.connectToDB()
database = connect[0]
cursor = connect[1]

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def register(self):
        # Rncrypt password
        cypher = hashlib.sha256()
        cypher.update(self.password.encode('utf8'))
        # Query to create user
        sql = "INSERT INTO users VALUES (null, %s, %s, %s, %s)"
        user = (self.name, self.email, cypher.hexdigest(), datetime.datetime.now())
        # Execute the query
        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result

    def login(self):
        # Encrypt password
        cypher = hashlib.sha256()
        cypher.update(self.password.encode('utf8'))
        # Query to check if user exists
        sql = "SELECT * FROM users WHERE email=%s AND user_password=%s"
        user = (self.email, cypher.hexdigest())
        # Execute the query
        cursor.execute(sql, user)
        result = cursor.fetchone()
        return result