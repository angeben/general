import mysql.connector

def connectToDB():
    database = mysql.connector.connect(
        host="localhost",
        user="*********",
        passwd="*********",
        database="python",
        port=3306
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]