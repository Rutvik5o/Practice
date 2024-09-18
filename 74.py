import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "123"
)

try:

    if mydb is None:

        print("Database is not connected")

    else:

        print("Database is connected succefully")

    
except mysql.connector.Error as e:
    print(e)


conn = mydb.cursor()

print("\n1.Create Database\n2.Show all databases\n3.Delete Database\n4.Create table\n5.show all tables\n6.Insert data in table\n7.Show all data in table\n8.Update data\n9.Delete data")

value=int(input("Enter your choice"))

if value == 1:
    conn.execute("Create database justfortest1")

    print("Entry done")

elif value == 2:

    print("Getting total database")

    conn.execute("show databases")

    result = conn.fetchall()

    for x in result:

        print(x)

elif value == 3:

    conn.execute("drop database justfortest")

    print("delted first db")

    conn.execute("drop database justfortest1")

    print("delted sesocnd db")

elif value == 4:

    conn.execute("create database temp11")

    conn.execute("use temp11")

    conn.execute("""
    create table temp(
    tempid int ,
    tempname varchar(10),
    temppage int

    )
    """)

elif value == 5:
    conn.execute("use temp11")


    conn.execute("show tables")

    result = conn.fetchall()

    for x in result:

        print(x)


elif value == 6:

    conn.execute("use temp11")

    conn.execute("""

    insert into temp value(1,'abc',10)

    """
    )
    print("Data inserted succesfullY")

    
elif value == 7:

    conn.execute("use temp11")

    conn.execute("select * from temp")

    result = conn.fetchall()

    for x in result:

        print(x)

elif value == 8:
    conn.execute("use temp11")

    conn.execute("update temp set temppage=20 where temppage=10")

    print("data updated succesfully")


elif value == 9:
    conn.execute("use temp11")

    conn.execute("delete from temp where temppage = 20")

    print("Data deleted succesfully")



else:

    print("invalid choice")











mydb.commit()
mydb.close()
