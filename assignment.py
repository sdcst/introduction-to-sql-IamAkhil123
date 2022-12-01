#!python
import sqlite3
def add():
    file = 'assignment.db'
    connection = sqlite3.connect(file)
    print(connection)
    cursor = connection.cursor()
    a = input('pet name')
    b = input('pet species')
    c = input('pet breed')
    d = input('owner name')
    e = input('owner phone number')
    f = input('owner email')
    g = input('owner balance')
    h = input('date of first visit(mm/dd/yy)')
    data = [a,b,c,d,e,f,g,h]
    query = """ create table if not exists customers ( id integer primary key autoincrement, pet tinytext, species tinytext, breed tinytext, name tinytext, phone tinytext, email tinytext, balance int, date tinytext); """
    cursor.execute(query)
    query = f"insert into customers (pet,species,breed,name,phone,email,balance,date) values ('{a}','{b}','{c}','{d}','{e}','{f}',{g},'{h}');"
    cursor.execute(query)
    connection.commit()
    connection.close ()
def id():
    file = 'assignment.db'
    connection = sqlite3.connect(file)
    print(connection)
    x = input('enter name ')
    cursor = connection.cursor()
    query = "select * from customers"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        if i[1] == x:
            print(i)
    return
def phonenumber():
    file = 'assignment.db'
    connection = sqlite3.connect(file)
    print(connection)
    x = input('phone number ')
    cursor = connection.cursor()
    query = "select * from customers"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        if i[5] == x:
            print(i)
    return
def email():
    file = 'assignment.db'
    connection = sqlite3.connect(file)
    print(connection)
    x = input('email')
    cursor = connection.cursor()
    query = "select * from customers"
    cursor.execute(query)
    result = cursor.fetchall()
    for i in result:
        if i[6] == x:
            print(i)
    return
x = input('insert a new record into the database and save it automatically [1] \n retrieve a record [2]')
if x == '1':
    add()
if x == '2':
    r = input('retrieve a record by their id and display all of the information [1] \nretrieve a record by the email and display all of the information [2] \nretrieve a record by phone number and display all of the information [3]')
    if r == '1':
        id()
    if r == '2':
        email()
    if r == '3':
        phonenumber()

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