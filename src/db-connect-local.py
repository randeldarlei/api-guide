import mysql.connector
from mysql.connector import errorcode
try:
    db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bd')
    print("Database connection made!")
except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
        elif error.errno ==errorcode.ER_ACCESS_DENIED_ERROR:
                print("Username or Password invalid!")
        else:
              print(error)
else:
        db_connection.close()