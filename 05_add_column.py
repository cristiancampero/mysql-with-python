import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# add a new column 'genero'
mycursor.execute("ALTER TABLE tv_shows ADD COLUMN genero VARCHAR(50);")

# show columns
mycursor.execute("desc tv_shows")
for x in mycursor:
    print(x)