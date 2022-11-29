#!python
"""
import sqlite3

file = 'assignment.db'
connection = sqlite3.connect(file)
print(connection)
mydb = sqlite3.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (pet name, pet species, pet breed, owner name, owner phone number, owner email, owner balance,    ) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

cursor = connection.cursor()
query = 
create table if not exists customers (
    id integer primary key autoincrement,
    pet name tinytext,
    pet species tinytext,
    pet breed tinytext,
    owner name tinytext,
    owner phone number
    owner email
    owner balance
    date of first visit(mm/dd/yy));

cursor.execute('PRAGMA table_info(customers);')

x = str(input('pet name'))
c = str(input('pet species'))
v = str(input('pet breed'))
b = str(input('owner name'))
n = str(input('owner phone number'))
m = str(input('owner email'))
a = str(input('owner balance'))
s = str(input('date of first visit(mm/dd/yy)'))
data1 = [x,c,v,b,n,m,a,s]
data = data1
for i in data:
    query = f"insert into customers (pet name,pet species,pet breed,owner name,owner phone number,owner email,owner balance,date of first visit(mm/dd/yy)) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}','{i[5]}','{i[6]}','{i[7]}');"
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)
"""


import  sqlite3
conn  =  sqlite3 . connect ( 'assignment.db' )
cursor  =  conn.cursor ()
#create the salesman table 
cursor.execute("CREATE TABLE customers(petname,petspecies,petbreed,ownername,ownerphonenumber,owneremail,ownerbalance;")

petname = input('Salesman ID:')
petspecies = input('Name:')
petbreed = input('City:')
ownername = input('Commission:')
ownerphonenumber = input('ownerphonenumber:')
owneremail = input('owneremail:')
ownerbalance = input('ownerbalance:')
cursor.execute("""
INSERT INTO salesman(salesman_id, name, city, commission)
VALUES (?,?,?,?)
""", (petname, petspecies, petbreed, ownername, ownerphonenumber, owneremail, ownerbalance))
conn.commit ()
print ( 'Data entered successfully.' )
conn . close ()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")

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