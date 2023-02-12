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