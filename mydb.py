import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'Bini',
    password = 'Biniyam5982.'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")
print("ALL Done!")