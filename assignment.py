#!python

import sqlite3
file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

mydb = sqlite3.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

#If this page is executed with no error, you have successfully created a database.






"""
x = str(input('pet name'))
c = str(input('pet species'))
v = str(input('pet breed'))
b = str(input('owner name'))
n = str(input('owner phone number'))
m = str(input('owner email'))
a = str(input('owner balance'))
s = str(input('date of first visit(mm/dd/yy)'))
data = [x,c,v,b,n,m,a,s]

cursor = connection.cursor()
query = 
create table if not exists customers (
    id integer primary key autoincrement,
    pet name tinytext,
    pet specices tinytext,
    owner name tinytext,
    owner phonenumber tinytext, 
    owner email tinytext,
    owner balance tinytext,
    data of first visit tinytext,
    cnum int);
"""



"""
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""