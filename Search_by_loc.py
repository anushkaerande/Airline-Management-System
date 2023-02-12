from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
root = tk.Tk()
root.title("Search by loaction")
root.geometry("700x600")
root.configure(background="Dodgerblue4")


db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()
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
    canvas1.create_window(310, 300, window=query_label)

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
