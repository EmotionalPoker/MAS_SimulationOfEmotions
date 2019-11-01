import tkinter as tk
import sys


root = tk.Tk()


def printtext():
    global e
    global val
    val = int(e.get())
    root.destroy()
    return val


def validate_entry(text):
    if text == " ":
        return True
    try:
        value = int(text)
    except ValueError:
        return False
    return 2 <= value <= 9


root.title("EmotionalPoker!")
root.state('zoomed')
t = tk.Label(root, text="Enter the Number of Players(2-9)!", font=("Comic Sans MS", 15, "bold"))
t.pack(side='top')
vcmd = (root.register(validate_entry), "%P")
e = tk.Entry(root, validate="key", validatecommand=vcmd)
e.pack()
e.focus_set()
b = tk.Button(root, text='GAMBLE!', font=("Comic Sans MS", 20, "bold"), command=printtext, bg="green")
b.pack(side='bottom')
image1 = tk.PhotoImage(file="poker_PNG107.png")
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (w, h))
panel1 = tk.Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1
tk.mainloop()

print(val)

root = tk.Tk()
root.title("EmotionalPoker!")
root.state('zoomed')
t = tk.Label(root, text="Enter the Player Emotions!", font=("Comic Sans MS", 15, "bold"))
t.pack(side='top')
player_count = val
player_emotions = []
player_emotion_values = []
v = []
v_emotions = []
for i in range(player_count):
    v.append(tk.IntVar())
    v_emotions.append(tk.DoubleVar())
for variable in v:
    variable.set(1)
for variable in v_emotions:
    variable.set(0)
attributes = [("No-emotion"), ("Happy"), ("Fear"), ("Anger"), ("Contempt"), ("Normal")]
# add no emotion for all players
for i in range(player_count):
    player_emotions.append(attributes[0])
    player_emotion_values.append(0)


def player_attribute_choice():
    return


def submit_button():
    for i in range(player_count):
        player_emotions[i] = attributes[int(v[i].get())]
        player_emotion_values[i] = v_emotions[i].get()
    print(player_emotions)
    print(player_emotion_values)
    root.destroy()


def data():
    row = 0
    for player_number in range(player_count):
        label_string = "Select the attribute of player %d" % player_number
        tk.Label(frame, text=label_string, justify=tk.LEFT, padx=20).grid(row=row, column=0)
        row += 1
        for val, attribute in enumerate(attributes):
            tk.Radiobutton(frame, text=attribute, justify=tk.RIGHT, variable=v[player_number], command=player_attribute_choice, value=val).grid(row=row, column=0)
            row += 1
        # scroll bar
        tk.Scale(frame, variable=v_emotions[player_number], orient=tk.HORIZONTAL, length=300, from_=0, to=1, tickinterval=5, resolution=0.001).grid(row=row, column=0)
        row += 1
        tk.Button(frame, text="GAMBLE!", width="27", bg="grey", command=submit_button).grid(row=row, column=0)


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=700, height=600)


sizex = 800
sizey = 650
posx = 400
posy = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
myframe = tk.Frame(root, relief=tk.GROOVE, width=150, height=150, bd=1)
myframe.place(x=10, y=10)
canvas = tk.Canvas(myframe)
frame = tk.Frame(canvas)
myscrollbar = tk.Scrollbar(myframe, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right", fill="y")
canvas.pack(side="left")
canvas.create_window((0, 0), window=frame, anchor='nw')
frame.bind("<Configure>", myfunction)
data()
root.mainloop()
