from tkinter import *
from tkinter import  messagebox
import re
import os

player_count = 3
player_emotion = []
wait_flag = 1

window=Tk()
window.title("Player Emotions")
window.geometry("900x600" )

scroll = Scrollbar()

scroll.pack(side=RIGHT, fill=Y)
#scrollbar(command= attributes.yview)

v = IntVar()
v.set(1)
attributes = [("No-emotion"),("Happy"),("Fear"),("Anger"),("Contempt"),("Normal",)]
##def page3():
##    window.destroy()
##    os.system('page3.py')

def player_attribute_choice():
     a=[]
     a.append(v)
     print(a)
     #print(v.get())
     wait_flag = 0

def submit_button():
     window.destroy()
     os.system('page3.py')
     
Label(window,text="Players",justify = LEFT,padx = 20).pack()

for val in range(player_count):
    wait_flag=1
    label_string = "Select the attribute of player %d" % val
    Label(window, text=label_string,justify = LEFT,padx = 20).pack()

    for val, attribute in enumerate(attributes):
        Radiobutton(window,text=attribute,padx = 20, variable=v, command=player_attribute_choice,value=val).pack(anchor=W)
        #a=v.get()
    Slide=Scale(window,orient=HORIZONTAL,length=350,from_= 0,to= 1,tickinterval=5,resolution=0.001).pack()
    a=v.get()
    
       
Button(window, text = "Submit", width="27",bg="grey", command=submit_button).pack()
   # if player_attribute == NULL:
    #wait()
    #else:
        #continue()

#page3()
window.mainloop()
