#!python3 
import tkinter as tk 
from tkinter import *
window = tk.Tk()


window.title("tk")

entry1 = tk.Entry(window,text="", width=10)
label1 = tk.Label(window,text="x")
entry2 = tk.Entry(window,text="", width=10)
entry3 = tk.Label(window, text="=")
entry4 = tk.Entry(window,text="", width=20)

label1.grid(row = 1, column = 2, rowspan = 1)
entry1.grid(row = 1, column = 1, rowspan = 1)
entry2.grid(row = 1, column = 3, rowspan = 1)
entry3.grid(row = 1, column = 4, rowspan = 1)
entry4.grid(row = 1, column = 5, rowspan = 1)


window.mainloop()