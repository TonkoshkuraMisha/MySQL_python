import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Misha",
    password="1111",
    database="asgard_rent_cars"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cars;")  # customers, cars


myresult = mycursor.fetchall()
# myresult = mycursor.fetchone()

for x in myresult:
    print(x)
