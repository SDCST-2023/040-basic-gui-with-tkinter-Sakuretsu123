#!python3

import tkinter as tk 
from tkinter import *
window = tk.Tk()
window.title("Example")


dogphoto = PhotoImage(file="dog.png")
labelphoto = tk.Label(window, image=dogphoto)

label1 = tk.Label(window,text="Pochacco !")
label2= tk.Label(window,text=" A cuddy little little puppy! This is from the same \ncreators who brought you Keropi and Kero Kero", background= "#00ffff")



labelphoto.grid(row = 1, column = 1, sticky=tk.E)
label1.grid(row = 1, column = 2, rowspan = 1,  sticky=tk.W)
label2.grid(row = 2, column = 1, rowspan = 1, columnspan=2)

window.mainloop()