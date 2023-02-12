from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")
cursor = db.cursor()


root = tk.Tk()
root.title("Search status by passport number")
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

