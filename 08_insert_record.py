import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()
mycursor.execute("INSERT INTO tv_shows (title, seasons, state) VALUES (%s, %s, %s)", ("Better Call Soul", 6, "Pending"))
# confirm the change
db.commit()

# show table content
mycursor.execute("SELECT * FROM tv_shows")

for x in mycursor:
    print(x)