#Importing tkinter package for rendering windows and frames
import tkinter as tk
#from PokerEnv import *
playercount = 0
#Main class definition
class PokerUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
#For displaying multiple frames in same window
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomeScreen, Player_Count_Screen, Player_Emotion_Screen, Poker_Table):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomeScreen")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class HomeScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Poker")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Continue", command=lambda: controller.show_frame("Poker_Table"))
        button.pack()
               

class Player_Count_Screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter Number of Players")
        label.pack(side="top", fill="x", pady=10)
        
        tk.Entry(self, textvariable = playercount).place(x=15,y=90)
        button = tk.Button(self, text="Continue",
                           command=lambda: controller.show_frame("Player_Emotion_Screen"))     
        button.pack()


class Player_Emotion_Screen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label_string = "players %d" %playercount
        label = tk.Label(self, text= label_string)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to Poker Table",
                           command=lambda: controller.show_frame("Poker_Table"))
        button.pack()

class Poker_Table(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        community_cards = ((10, "♠"),(4, "♦"))
        label_string = community_cards
        label = tk.Label(self, text= label_string)
        label.pack(side="top", fill="x", pady=10)

#♠        

if __name__ == "__main__":
    app = PokerUI()
    app.mainloop()
