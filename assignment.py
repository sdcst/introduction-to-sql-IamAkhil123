#!python

import sqlite3

x = str(input('pet name'))
c = str(input('pet species'))
v = str(input('pet breed'))
b = str(input('owner name'))
n = str(input('owner phone number'))
m = str(input('owner email'))
a = str(input('owner balance'))
s = str(input('date of first visit(mm/dd/yy)'))

sqliteConnection = sqlite3.connect('assignment.db')
cursor = sqliteConnection.cursor()
print("Connected to SQLite")
query = """CREATE TABLE customers (petname, petspecies, petbreed, ownername, ownerphonenumber, owneremail, ownerbalance, dateoffirstvisit)"""
data = (x,c,v,b,n,m,a,s)
cursor.execute(data, query)
sqliteConnection.commit()
print("Python Variables inserted successfully into assignment.db table")

cursor.close()
sqliteConnection.close()
print("The SQLite connection is closed")
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