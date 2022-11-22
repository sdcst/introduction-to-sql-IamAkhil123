#!python
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = """
create table if not exists customers (
    id integer primary key autoincrement,
    pet name, 
    pet species, 
    pet breed, 
    owner name, 
    owner phone number, 
    owner email, 
    owner balance, 
    data of first visit(mm/dd/yy)");
"""
cursor.execute(query)


cursor = conn.cursor()

cursor.execute("pet name, pet species, pet breed, owner name, owner phone number, owner email, owner balance, data of first visit(mm/dd/yy)")
conn.commit()

CREATE TABLE customers ("pet name, pet species, pet breed, owner name, owner phone number, owner email, owner balance, data of first visit(mm/dd/yy)");

"""
import sqlite3 

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)
x = str(input('pet name'))
c = str(input('pet species'))
v = str(input('pet breed'))
b = str(input('owner name'))
n = str(input('owner phone number'))
m = str(input('owner email'))
a = str(input('owner balance'))
s = str(input('date of first visit(mm/dd/yy)'))
data = [x,c,v,b,n,m,a,s]
Customers =  ("pet name, pet species, pet breed, owner name, owner phone number, owner email, owner balance, data of first visit(mm/dd/yy)")
query = (Customers, data)
print (query)
cursor.execute(query)
cursor = connection.cursor()
connection.commit()
result = cursor.fetchall()
print(result)
"""
"""

uery = f"create table if no exists customers(petname, species, breed, name, phonenumber, email, balance, dataoffirstvisit (VALUES('{x}','{c}','{v}','{b}','{n}','{m}','{a},','{s});"
Create a program that will store the database for a veterinary
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