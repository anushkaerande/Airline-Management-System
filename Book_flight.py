from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql
db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()
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
    query_label = Label(root, text="Booking is done!!", font=("Arial Italic", 11))
    query_label.grid(row=8, column=0, columnspan=2)
    canvas1.create_window(400, 620, window=query_label)
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