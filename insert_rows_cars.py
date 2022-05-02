import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Misha",
    password="1111",
    database="asgard_rent_cars"
)

mycursor = mydb.cursor()

sql = "INSERT INTO cars (model, gov_number) VALUES (%s, %s)"
val = [
    ('Nissan', 'USD0001'),
    ('BMW', 'CAD1234'),
    ('Renault', 'AI7770TM'),
    ('Range Rover', 'ENG3141'),
    ('Mercedes', 'USD1321'),
    ('BMW', 'GER1111'),
    ('Range Rover', 'AA5500HH')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
