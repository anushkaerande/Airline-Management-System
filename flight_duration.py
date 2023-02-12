from tkinter import *
import tkinter as tk
import time
import mysql.connector as mysql

db = mysql.connect(host = "localhost",user = "root",passwd = "anusonu123",database = "2338_db")

cursor = db.cursor()

root= tk.Tk()
root.title("Search flight by time duration")
root.geometry("700x600")
root .configure(background="Dodgerblue4")

h1 = StringVar()
m1 = StringVar()
s1 = StringVar()

h2 = StringVar()
m2 = StringVar()
s2 = StringVar()
h5=StringVar()
def search_flight():
   h1=str(entry0.get())
   m1=str(entry1.get())
   s1=str(entry1.get())
   
   h2=str(entry3.get())
   m2=str(entry4.get())
   s2=str(entry5.get())

   #t1 =int(h1+(m1*60)+(s1*3600))
   #t2 =int(h2+(m2*60)+(s2*3600))
   t1 = str(h1+':'+m1+':'+s1)
   t2 = str(h2+':'+m2 +':'+ s2)


   query = "select FLIGHT_NO, ARRIVAL_CITY, DEPARTURE_CITY from flight_details where DEPARTURE_TIME between %s and %s"
   val = [t1,t2]
   cursor.execute(query,val)
   records = cursor.fetchall()
   print(records)
   
   print_records = ''
   for record in records:
       print_records += str(record)+ '\n'
     
   query_label = Label(root,text = print_records,font=("Arial Italic",11))
   query_label.grid(row=8,column=0,columnspan=2)
   canvas1.create_window(320, 400, window=query_label)
   
   db.commit()
    
canvas1 = tk.Canvas(root, width = 650, height = 550,bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=25,y=25)

L1=tk.Label(root, text="Flight interval 1:",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(100, 50, window=L1)
entry0 = tk.Entry (root)
canvas1.create_window(200, 100, window=entry0)
label1 = tk.Label(root, text="Enter hour",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(80, 100, window=label1)
entry1 = tk.Entry (root)
canvas1.create_window(200, 150, window=entry1)
label1 = tk.Label(root, text="Enter mins",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(80, 150, window=label1)
entry2 = tk.Entry (root)
canvas1.create_window(200, 200, window=entry2)
label2 = tk.Label(root, text="Enter secs",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(80, 200, window=label2)

L2=tk.Label(root, text="Flight interval 2:",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(450, 50, window=L2)
entry3 = tk.Entry (root)
canvas1.create_window(550, 100, window=entry3)
label3 = tk.Label(root, text="Enter hour",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(430, 100, window=label3)
entry4 = tk.Entry (root)
canvas1.create_window(550, 150, window=entry4)
label4 = tk.Label(root, text="Enter mins",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(430, 150, window=label4)
entry5 = tk.Entry (root)
canvas1.create_window(550, 200, window=entry5)
label5 = tk.Label(root, text="Enter secs",font=("Arial Italic",14),bg='dodgerblue4',fg='white')
canvas1.create_window(430, 200, window=label5)

btn = Button(root, text = "Search",font=("Arial Italic",14),bg='midnight blue',fg='white',command=search_flight)
btn.pack(side = 'top')
btn.place(x=300,y=250)

root.mainloop()