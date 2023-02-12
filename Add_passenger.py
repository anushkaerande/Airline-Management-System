from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql

db = mysql.connect(host="localhost", user="root", passwd="anusonu123", database="2338_db")

cursor = db.cursor()

root = tk.Tk()
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
btn.place(x=400, y=550)

root.mainloop()