from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()

'''root = tk.Tk()
root.title("Add Passenger")
root.geometry("1024x768")
root.configure(background="Dodgerblue4")

passport_no = StringVar()
address = StringVar()
fname = StringVar()
lname = StringVar()
phno = StringVar()
email = StringVar()
age = StringVar()
nation = StringVar()
gender = StringVar()
flight_no = StringVar()

db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")


def insert():
    cursor = db.cursor()
    passport_no = int(entry1.get())
    address = entry2.get()
    fname = entry3.get()
    lname = entry4.get()
    ph_no = entry5.get()
    email = entry6.get()
    age = entry7.get()
    nation = entry8.get()
    gender = entry9.get()
    flight_no = entry10.get()

    Query = "INSERT INTO passenger VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    VAL = [passport_no, address, fname, lname, ph_no, email, age, nation, gender, flight_no]
    cursor.execute(Query, VAL)
    db.commit()


canvas1 = tk.Canvas(root, width=800, height=600, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=100, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(400, 80, window=entry1)
label1 = tk.Label(root, text="Enter passport number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 80, window=label1)

entry2 = tk.Entry(root)
canvas1.create_window(400, 120, window=entry2)
label2 = tk.Label(root, text="Enter address", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 120, window=label2)

entry3 = tk.Entry(root)
canvas1.create_window(400, 160, window=entry3)
label3 = tk.Label(root, text="Enter first name", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 160, window=label3)

entry4 = tk.Entry(root)
canvas1.create_window(400, 200, window=entry4)
label4 = tk.Label(root, text="Enter last name", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 200, window=label4)

entry5 = tk.Entry(root)
canvas1.create_window(400, 240, window=entry5)
label5 = tk.Label(root, text="Enter phone number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 240, window=label5)

entry6 = tk.Entry(root)
canvas1.create_window(400, 280, window=entry6)
label6 = tk.Label(root, text="Enter email id", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 280, window=label6)

entry7 = tk.Entry(root)
canvas1.create_window(400, 320, window=entry7)
label7 = tk.Label(root, text="Enter age", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 320, window=label7)

entry8 = tk.Entry(root)
canvas1.create_window(400, 360, window=entry8)
label8 = tk.Label(root, text="Enter nationality", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 360, window=label8)

entry9 = tk.Entry(root)
canvas1.create_window(400, 400, window=entry9)
label9 = tk.Label(root, text="Enter gender", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 400, window=label9)

entry10 = tk.Entry(root)
canvas1.create_window(400, 440, window=entry10)
label10 = tk.Label(root, text="Enter Flight number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 440, window=label10)

btn = Button(root, text="Add Passenger ", bg='midnight blue', fg='white', command=insert)
btn.pack(side='top')
btn.place(x=400, y=550)'''

'''#root.mainloop()
from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql



root = tk.Tk()
root.title("Search flight by time duration")
root.geometry("700x600")
root.configure(background="Dodgerblue4")

bid = StringVar()


def search_flight():
    bid = entry1.get()
    query = "select * from flight_details where BOOKING_ID = %s "
    val = [bid]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[0]:
        print_records += str(record) + ' | '

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(300, 250, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=600, height=500, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=50, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(400, 100, window=entry1)
label1 = tk.Label(root, text="Enter ppno", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 50, window=label1)

btn = Button(root, text="Search", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=search_flight)
btn.pack(side='top')
btn.place(x=300, y=200)

root.mainloop()

from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql

root = tk.Tk()
root.title("Book a flight")
root.geometry("1024x768")
root.configure(background="Dodgerblue4")

booking_id = StringVar()
p_name = StringVar()
date = StringVar()
loc_to = StringVar()
loc_from = StringVar()
time = StringVar()
seat = StringVar()
cLass = StringVar()
flight_no = StringVar()
passport_no = StringVar()

db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")


def insert():
    cursor = db.cursor()
    booking_id = int(entry1.get())
    p_name = entry2.get()
    date = entry3.get()
    loc_to = entry4.get()
    loc_from = entry5.get()
    time = entry6.get()
    seat = entry7.get()
    cLass = entry8.get()
    flight_no = entry9.get()
    passport_no = entry10.get()

    Query = "INSERT INTO booking VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    VAL = [booking_id, p_name, date, loc_to, loc_from, time, seat, cLass, flight_no, passport_no]
    cursor.execute(Query, VAL)
    db.commit()


canvas1 = tk.Canvas(root, width=800, height=600, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=100, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(400, 80, window=entry1)
label1 = tk.Label(root, text="Enter booking id", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 80, window=label1)

entry2 = tk.Entry(root)
canvas1.create_window(400, 120, window=entry2)
label2 = tk.Label(root, text="Enter passenger name", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 120, window=label2)

entry3 = tk.Entry(root)
canvas1.create_window(400, 160, window=entry3)
label3 = tk.Label(root, text="Enter date", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 160, window=label3)

entry4 = tk.Entry(root)
canvas1.create_window(400, 200, window=entry4)
label4 = tk.Label(root, text="Enter location to", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 200, window=label4)

entry5 = tk.Entry(root)
canvas1.create_window(400, 240, window=entry5)
label5 = tk.Label(root, text="Enter location from", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 240, window=label5)

entry6 = tk.Entry(root)
canvas1.create_window(400, 280, window=entry6)
label6 = tk.Label(root, text="Enter time", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 280, window=label6)

entry7 = tk.Entry(root)
canvas1.create_window(400, 320, window=entry7)
label7 = tk.Label(root, text="Enter seat", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 320, window=label7)

entry8 = tk.Entry(root)
canvas1.create_window(400, 360, window=entry8)
label8 = tk.Label(root, text="Enter class", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 360, window=label8)

entry9 = tk.Entry(root)
canvas1.create_window(400, 400, window=entry9)
label9 = tk.Label(root, text="Enter flight number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 400, window=label9)

entry10 = tk.Entry(root)
canvas1.create_window(400, 440, window=entry10)
label10 = tk.Label(root, text="Enter passport number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 440, window=label10)

btn = Button(root, text="Add Booking ", bg='midnight blue', fg='white', command=insert)
btn.pack(side='top')
btn.place(x=400, y=550)

root.mainloop()

from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql'''

db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()
'''
root = tk.Tk()
root.title("Search flight by time duration")
root.geometry("700x600")
root.configure(background="Dodgerblue4")

dept = StringVar()
nation=StringVar()

def count_nation():
    nation = entry1.get()
    flight = entry2.get()

    query = "select COUNT(*) from passenger where NATIONALITY=%s and FLIGHT_NO=%s"
    val = [nation,flight]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records, font=("Arial Italic", 11))
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(320, 300, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=650, height=550, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=25, y=25)

entry1 = tk.Entry(root)
canvas1.create_window(400, 50, window=entry1)
label1 = tk.Label(root, text="Enter Nationality", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 50, window=label1)

entry2 = tk.Entry(root)
canvas1.create_window(400, 100, window=entry2)
label2 = tk.Label(root, text="Enter Flight no", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 100, window=label2)

btn = Button(root, text="Search", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=count_nation)
btn.pack(side='top')
btn.place(x=300, y=200)

root.mainloop()


from tkinter import *
import tkinter as tk
import time

root = tk.Tk()
root.title("Display Ticket")
root.geometry("900x500")
root.configure(background="Dodgerblue4")

bid = StringVar()


def ticket():
    bid = int(entry1.get())

    query = "call ShowTicket(%s)"
    val = [bid]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records, font=("Arial Italic", 11))
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(320, 300, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=750, height=400, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=80, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(400, 80, window=entry1)
label1 = tk.Label(root, text="Enter Booking ID : ", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(200, 80, window=label1)

btn = Button(root, text="Display Ticket", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=ticket)
btn.pack(side='top')
btn.place(x=350, y=180)

root.mainloop()

from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql


root = tk.Tk()
root.title("Search flight by time duration")
root.geometry("700x600")
root.configure(background="Dodgerblue4")

bid = StringVar()


def status():
    bid = entry1.get()
    query = "select STATUS from flight_details where FLIGHT_NO=(select FLIGHT_NO from passenger where PASSPORT_NO=%s) "
    val = [bid]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[0]:
        print_records += str(record)

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(300, 300, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=600, height=500, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=50, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(400, 50, window=entry1)
label1 = tk.Label(root, text="Enter passport number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 50, window=label1)

btn = Button(root, text="Search", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=status)
btn.pack(side='top')
btn.place(x=300, y=200)
label2= tk.Label(root, text="Your Flight Status is", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(300, 250, window=label2)
root.mainloop()


root = tk.Tk()
root.title("Search by loaction")
root.geometry("700x600")
root.configure(background="Dodgerblue4")

arrivcity = StringVar()
deparcity=StringVar()

def location():
    arrivcity = entry1.get()
    deparcity = entry2.get()

    query = "Select FLIGHT_NO, ARRIVAL_CITY, DEPARTURE_CITY,ARRIVAL_TIME,DEPARTURE_TIME from flight_details where DEPARTURE_CITY= %s and ARRIVAL_CITY= %s"
    val = [arrivcity,deparcity]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records, font=("Arial Italic", 11))
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(320, 300, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=650, height=550, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=25, y=25)

entry1 = tk.Entry(root)
canvas1.create_window(400, 50, window=entry1)
label1 = tk.Label(root, text="Enter departure city", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 50, window=label1)

entry2 = tk.Entry(root)
canvas1.create_window(400, 100, window=entry2)
label2 = tk.Label(root, text="Enter arrival city", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 100, window=label2)

btn = Button(root, text="Search", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=location)
btn.pack(side='top')
btn.place(x=300, y=200)

root.mainloop()

root = tk.Tk()
root.title("Search flight by time duration")
root.geometry("1024x700")
root.configure(background="Dodgerblue4")



def flight_timetable():

    query = "select * from flight_details order by DEPARTURE_TIME ASC"


    cursor.execute(query)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[:-1]:
        print_records += str(record) + '\n'


    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(500, 250, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=1004, height=600, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=50, y=50)



btn = Button(root, text="Display timetable sequentially", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=flight_timetable)
btn.pack(side='top')
btn.place(x=450, y=200)

root.mainloop()

from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()

root = tk.Tk()
root.title("Number of flight by from  each city")
root.geometry("700x500")
root.configure(background="Dodgerblue4")



def search_city():


    query = "select count(*),FLIGHT_NO,ARRIVAL_CITY from flight_details group by ARRIVAL_CITY"



    cursor.execute(query)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records, font=("Arial Italic", 11))
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(320, 300, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=650, height=450, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=25, y=25)



btn = Button(root, text="Search count of flights from each city", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=search_city)
btn.pack(side='top')
btn.place(x=180, y=150)

root.mainloop()

root = tk.Tk()
root.title("Flight details by Booking ID")
root.geometry("1200x400")
root.configure(background="Dodgerblue4")

BID = StringVar()


def search_city():
    BID = entry.get()

    query = "select * from flight_details where FLIGHT_NO=(select FLIGHT_NO from booking where BOOKING_ID= %s)"
    val = [BID]

    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records, font=("Arial Italic", 11))
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(580, 300, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=1150, height=350, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=25, y=25)

label1 = tk.Label(root, text="Enter booking ID", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(450, 100, window=label1)
entry = tk.Entry(root)
canvas1.create_window(600, 100, window=entry)

btn = Button(root, text="Search", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=search_city)
btn.pack(side='top')
btn.place(x=550, y=200)

root.mainloop()
'''
'''root = tk.Tk()
root.title("Search Available Business Seats")
root.geometry("700x600")
root.configure(background="Dodgerblue4")


bid = StringVar()

def avail_buisness():
    bid = entry1.get()
    query = "select AVAIL_BUISNESS_SEATS from plane where FLIGHT_no = %s "
    val = [bid]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[0]:
        print_records += 'Seats available : ' + str(record)

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(300, 250, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=600, height=500, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=50, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(450, 100, window=entry1)
label1 = tk.Label(root, text="Enter flight number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 100, window=label1)

btn = Button(root, text="Search Business", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=avail_buisness)
btn.pack(side='top')
btn.place(x=270, y=200)

root.mainloop()

root = tk.Tk()
root.title("Search Available First Seats")
root.geometry("700x600")
root.configure(background="Dodgerblue4")


bid = StringVar()

def avail_first():
    bid = entry1.get()
    query = "select AVAIL_FIRST_SEATS from plane where FLIGHT_no = %s "
    val = [bid]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[0]:
        print_records += 'Seats available : ' + str(record)

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(300, 250, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=600, height=500, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=50, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(450, 100, window=entry1)
label1 = tk.Label(root, text="Enter flight number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 100, window=label1)

btn = Button(root, text="Search First", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=avail_first)
btn.pack(side='top')
btn.place(x=270, y=200)

root.mainloop()

root = tk.Tk()
root.title("Search Available Economy Seats")
root.geometry("700x600")
root.configure(background="Dodgerblue4")


bid = StringVar()

def avail_eco():
    bid = entry1.get()
    query = "select AVAIL_ECO_SEATS from plane where FLIGHT_no = %s "
    val = [bid]
    cursor.execute(query, val)
    records = cursor.fetchall()
    print(records)

    print_records = ''
    for record in records[0]:
        print_records += 'Seats available : ' + str(record)

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(300, 250, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=600, height=500, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=50, y=50)

entry1 = tk.Entry(root)
canvas1.create_window(450, 100, window=entry1)
label1 = tk.Label(root, text="Enter flight number", font=("Arial Italic", 14), bg='dodgerblue4', fg='white')
canvas1.create_window(150, 100, window=label1)

btn = Button(root, text="Search Eco", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=avail_eco)
btn.pack(side='top')
btn.place(x=270, y=200)

root.mainloop()
'''