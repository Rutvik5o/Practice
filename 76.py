import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123",
    database = "tempyet"
)

if mydb is None:

    print("Database not connected")
else:
    print("Database connected")

conn = mydb.cursor()

conn.execute("drop database tempyet")

print("database deleted succesfully")

conn.execute("show databases")

abc= conn.fetchall()

for x in abc:
    print(x)







mydb.commit()
mydb.close()


