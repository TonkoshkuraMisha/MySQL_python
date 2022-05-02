import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Misha",
    password="1111",
    database="asgard_rent_cars"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Thor Odinson', 'Asgard 3'),
    ('Odin Borson', 'Asgard 1'),
    ('Loki Laufeyson', 'Asgard 4'),
    ('Hella Odinson', 'Asgard 2')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
