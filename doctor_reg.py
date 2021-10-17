Set as interpreter
#!C:/pythoncode/venv/Scripts/python.exe
print("Content-type:text/html\r\n\r\n")

import mysql.connector
import cgi
from = cgi.FieldStorage()

n=form.getvalue("name")
e=form.getvalue("email")
p=form.getvalue("pass")
num=form.getvalue("number")
s=form.getvalue("sector")
m=form.getvalue("medical")
a=form.getvalue("address")

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="medi"
)

mycursor=mydb.cursor()


sql= "Insert Into doctor_reg_tb (Name,Email,Password,Mobile,Sector,Medical,Address) Values (%s,%s,%s,%s,%s,%s,%s)"
val=(n, e, p, num, s, m, a)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount,"Record Inserted!")
