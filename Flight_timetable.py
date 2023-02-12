from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

root = tk.Tk()
root.title("Search flight by time")
root.geometry("1024x700")
root.configure(background="Dodgerblue4")


cursor = db.cursor()


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
    canvas1.create_window(500, 450, window=query_label)

    db.commit()


canvas1 = tk.Canvas(root, width=970, height=650, bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=25, y=25)



btn = Button(root, text="Display timetable sequentially", font=("Arial Italic", 14), bg='midnight blue', fg='white', command=flight_timetable)
btn.pack(side='top')
btn.place(x=350, y=200)

root.mainloop()
