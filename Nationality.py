from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")
cursor = db.cursor()

root = tk.Tk()
root.title("Display count of passenger by nationality")
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

