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
d=form.getvalue("date")
a=form.getvalue("address")
g=form.getvalue("Gender")

mydb=mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="medi"
)

mycursor=mydb.cursor()

sql= "Insert Into patient_reg_tb (Name,Email,Password,Mobile,Date_of_Birth,Address,Gender) Values (%s,%s,%s,%s,%s,%s,%s)"
val=(n, e, p, num, d, a, g)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount,"Record Inserted!")
