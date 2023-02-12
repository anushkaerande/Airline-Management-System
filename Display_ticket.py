from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()
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
    canvas1.create_window(360, 300, window=query_label)

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
