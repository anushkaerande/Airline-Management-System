import os
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()
root.geometry("1024x768")
root.title("Airline Management System")
root.configure(background="blue")


image1 = Image.open(r"C:\Users\Anushka\Desktop\DBMS\C9.jpg")
resize_image = image1.resize((100,100))
test = ImageTk.PhotoImage(image1,resize_image)
L=tk.Label(root,text='Welcome to Cloud9\nWhere everything is just divine!!',font=("Arial Italic",18),bg='blue',fg='white')
L.pack()
label1 = tk.Label(image=test)
label1.image = test
label1.pack(fill='both')


def addPassenger():
    os.system('python Add_passenger.py')

def bookFlight():
    os.system('python Book_flight.py')

def Display():
    os.system('python Display_ticket.py')

def Status():
    os.system('python Status.py')

def byTime():
    os.system('python flight_duration.py')

def byLoc():
    os.system('python Search_by_loc.py')
    
def timetable():
    os.system('python Flight_Timetable.py')
    
def countF():
    os.system('python Flight_from_city.py')

def countP():
    os.system('python Nationality.py')

def searchID():
    os.system('python Display_by_bookid.py')
    
def A():
   os.system('python Avail_First.py')

def B():
    os.system('python Avail_Buisness.py')

def C():
    os.system('python Avail_Eco.py')
    
def delete():
    os.system('python cancel_booking.py')
    
button = Button(root ,text = 'Add passenger',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=addPassenger)
button.place(x =150, y = 150)
button1 = Button(root,text = 'Book a flight',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=bookFlight)
button1.place(x =440, y = 150)
button2 = Button(root,text = 'Find status of flights',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=Status)
button2.place(x = 700, y = 150)
button3 = Button(root, text = 'Display flight timetable',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=timetable)
button3.place(x = 50, y = 250)
button4= Button(root,text = 'Display Ticket',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=Display)
button4.place(x = 390, y =250)
button5= Button( root,text = 'Display count of passengers',relief = RAISED, font = ('Arial Italic', 18),bg='blue',fg='white',command=countP)
button5.place(x = 650, y = 250)
button6= Button(root,text = 'Search flight details',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=searchID)
button6.place(x = 50, y = 350)
button7= Button(root,text = 'Search flight by time',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=byTime)
button7.place(x = 350, y = 350)
button8= Button(root,text = 'Search flight by location',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=byLoc)
button8.place(x = 670, y = 350)
button9= Button(root,text = 'Available First Class',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=A)
button9.place(x = 50, y = 450)
button10= Button(root,text = 'Available Business Class',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=B)
button10.place(x = 350, y = 450)
button11= Button(root,text = 'Available Economy Class',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=C)
button11.place(x = 700, y = 450)
button10= Button(root,text = 'Delete booking',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=delete)
button10.place(x = 200, y = 550)
button11= Button(root,text = 'Count flights from a city',relief = RAISED,font = ('Arial Italic', 18),bg='blue',fg='white',command=countF)
button11.place(x = 550, y = 550)


root.mainloop()
 