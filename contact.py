Set as interpreter
#!C:/pythoncode/venv/Scripts/python.exe
print("Content-type:text/html\r\n\r\n")

import mysql.connector
import cgi
from = cgi.FieldStorage()

n=form.getvalue("name")
e=form.getvalue("email")
t=form.getvalue("text")

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="medi"
)

mycursor=mydb.cursor()

sql= "Insert Into contact_tb (Name,Email,Text) Values (%s.%s,%s)"
val=(n, e, t)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount,"Record Inserted!")
