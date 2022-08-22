import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# delete the column 'gender'
mycursor.execute("ALTER TABLE tv_shows DROP COLUMN gender;")

# show columns
mycursor.execute("desc tv_shows")
for x in mycursor:
    print(x)