import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
    database="testdb"
)

mycursor = db.cursor()

# rename table 'series' by 'tv_shows'
mycursor.execute("ALTER TABLE series RENAME TO tv_shows;")