import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# I finished watching 'Peaky Blinders'
# Change 'Watching' to 'Finished'
mycursor.execute("UPDATE tv_shows SET state = 'Finished' WHERE id = 2")

# confirm the change
db.commit()


# show table content
mycursor.execute("SELECT * FROM tv_shows")

for x in mycursor:
    print(x)