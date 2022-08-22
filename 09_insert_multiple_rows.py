import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# create the sentence
sentence = "INSERT INTO tv_shows (title, seasons, state) VALUES (%s, %s, %s)"
# set the values
records = [("Peaky Blinders", 6, "Watching"), ("Vikings", 6, "Finished")]

# add the records to the table
mycursor.executemany(sentence, records)
# confirm the change
db.commit()


# show table content
mycursor.execute("SELECT * FROM tv_shows")

for x in mycursor:
    print(x)