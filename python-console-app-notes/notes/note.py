import users.connection as connection

# Establish connection to DB
connect = connection.connectToDB()
database = connect[0]
cursor = connect[1]

class Note:

    def __init__(self, user_id, title="", description=""):
        self.user_id = user_id
        self.title = title
        self.description = description

    def save(self):
        # Query to create note
        sql = "INSERT INTO notes VALUES (null, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.description)
        # Execute the query
        try:
            cursor.execute(sql, note)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
    
    def list(self):
        # Query to fetch the user's note
        sql = f"SELECT * FROM notes WHERE user_id={self.user_id}"
        # Execute the query
        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result
    
    def delete(self):
        sql = f"DELETE FROM notes WHERE user_id={self.user_id} AND note_title LIKE '%{self.title}%'"
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]