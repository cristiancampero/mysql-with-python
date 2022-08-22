import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# rename the column 'genero' to 'gender'
mycursor.execute("ALTER TABLE tv_shows CHANGE genero gender VARCHAR(50);")

# show columns
mycursor.execute("desc tv_shows")
for x in mycursor:
    print(x)