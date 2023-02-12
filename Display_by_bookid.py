from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()


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