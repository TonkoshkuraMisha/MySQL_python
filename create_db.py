import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Misha",
    password="1111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE asgard_rent_cars")
