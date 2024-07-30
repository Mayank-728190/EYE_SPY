import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
print(mydb)
<mysql.connector.connection.MySQLConnection object at 0x00DA36D0>

mycursor=mydb.cursor()
mycursor.execute("create Database Authorized_user")

mycursor.execute("show databases")
for x in mycursor:
    print(x)
('authorized_user',)
('information_schema',)
('mydatabase',)
('mysql',)
('performance_schema',)
('phpmyadmin',)
('python_database',)
('students',)

mycursor.execute("drop database hello")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_database"
)

mycursor=mydb.cursor()
mycursor.execute("create table my_table(id int primary key,Name varchar(50), Age int,Address varchar(100))")

mycursor.execute("Show Tables")
for x in mycursor:
    print(x)
('my_table',)

sql="INSERT INTO stu_table(id,name,age) values(%s,%s,%s)"
val=(1,Mayank,20)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")