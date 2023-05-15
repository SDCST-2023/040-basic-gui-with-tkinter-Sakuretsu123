#!python3 
import tkinter as tk 
from tkinter import *
window = tk.Tk()

#title
window.title("T-Town Veterinary Clinic Database")

#all the label
dogphoto = PhotoImage(file="dog.png")
labelphoto = tk.Label(window, image=dogphoto)

labelname = tk.Label(window,text="Name")
labeltype= tk.Label(window,text="Type")
labelbreed = tk.Label(window,text="Breed")
labelowner = tk.Label(window,text="Owner")
labelbirthdate = tk.Label(window,text="Birthdate")
database = tk.Label(window,text="Client Database")

#all the button 

previous = tk.Button(window,text="< Previous")
next = tk.Button(window,text="Next >")
save = tk.Button(window,text="Save Entry")
search = tk.Button(window,text="Search by Name")

#boxes
name = tk.Entry(window,text="", width=10)
type = tk.Entry(window,text="", width=10)
breed = tk.Entry(window,text="", width=10)
owner = tk.Entry(window,text="", width=10)
birthdate = tk.Entry(window,text="", width=10)
searchbox = tk.Entry(window,text="", width=20)




#all the placement info

labelphoto.place(x=20,y=10)
labelname.place(x=32,y=120)
labeltype.place(x=104,y=120)
labelbreed.place(x=170,y=120)
labelowner.place(x=238,y=120)
labelbirthdate.place(x=320,y=120)

name.place(x=20,y=150)
type.place(x=90,y=150)
breed.place(x=160,y=150)
owner.place(x=230,y=150)
birthdate.place(x=314,y=150)
searchbox.place(x=300,y=5)

database.place(x=140,y=60)
previous.place(x=0,y=180)
next.place(x=340,y=180)
save.place(x=160,y=180)

search.place(x=200,y=0)


window.mainloop()