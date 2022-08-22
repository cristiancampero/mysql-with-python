import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# create the table 'series'
mycursor.execute("CREATE TABLE IF NOT EXISTS series(id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(100) NOT NULL, seasons INT, state ENUM('Pending', 'Watching', 'Abandoned', 'Finished') NOT NULL)")

# show table columns
mycursor.execute("desc series")
for x in mycursor:
    print(x)


# create the table 'libros'
mycursor.execute("CREATE TABLE IF NOT EXISTS libros (id INT PRIMARY KEY AUTO_INCREMENT, author VARCHAR(100), title VARCHAR(100) NOT NULL, state ENUM('Pending', 'Reading', 'Abandoned', 'Finished') NOT NULL)")

# show table columns
mycursor.execute("desc libros")
for x in mycursor:
    print(x)