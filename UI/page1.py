from tkinter import *
from tkinter import  messagebox
import re
import os

window=Tk()
window.title("page1")
window.geometry("900x600" )
players = 0

def page2():
   int(str(playervalue.get()))
   players=playervalue.get()
   f = open( 'var.txt', 'w' )
   f.write( players)
   f.close()
   Label(window, 
         text=players,
         justify = LEFT,
         padx = 20).pack()
   window.destroy()
   os.system('page2.py')

heading = Label(text = "ENTER PLAYERS TO CONTINUE").pack()

Label(text="Players :").place(x=15,y=50)


playervalue = StringVar()
Entry(window, textvariable = playervalue).place(x=15,y=90)
Button(window, text = "Proceed to game", width="27",bg="grey", command=page2 ).place(x=15, y=125)

window.mainloop()
