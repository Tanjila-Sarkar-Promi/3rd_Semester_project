Set as interpreter
#!C:/pythoncode/venv/Scripts/python.exe
print("Content-type:text/html\r\n\r\n")

import mysql.connector
import cgi
form = cgi.FieldStorage()

n=form.getvalue("name")
p=form.getvalue("pass")

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="medi"
)

mycursor=mydb.cursor()

sql= "INSERT INTO login_tb (Name,Password) Values (%s,%s)"
val=(n, p)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount,"Record Inserted!")
