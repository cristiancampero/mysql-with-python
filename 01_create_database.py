# create database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toor",
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdb")