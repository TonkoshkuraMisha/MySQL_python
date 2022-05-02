import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Misha",
    password="1111",
    database="asgard_rent_cars"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("CREATE TABLE cars (id INT AUTO_INCREMENT PRIMARY KEY, model VARCHAR(255), gov_number VARCHAR(255))")

# changed table
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
