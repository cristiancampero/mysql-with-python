import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# delete all the movies i finished watching
mycursor.execute("DELETE FROM tv_shows WHERE state = 'Finished'")

# confirm the change
db.commit()


# show table content
mycursor.execute("SELECT * FROM tv_shows")

for x in mycursor:
    print(x)