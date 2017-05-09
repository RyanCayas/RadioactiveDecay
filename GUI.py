import sys
#import tkFileDialog
#from tkFileDialog import askopenfilename
import Tkinter
from Tkinter import *
from PIL import ImageTk, Image
import os


main=Tk()
main.title("Main Menu")


def open1():
    main.withdraw()
    import radioactive

def open2():
    main.withdraw()
    import menuhalflife

img = ImageTk.PhotoImage(Image.open("atom.png"))
panel = Label(main, image = img)
panel.pack()

TitlePage = Label(main, text = "Radioactive Decay", font = ("Source Sans Pro",50))
TitlePage.pack()
alpha = Button (main, text = "Three Types of Decay", width=75, height=4, command = open1)
alpha.pack()
#guide = Button (main, text = "User's Guide", width=75, height=4)
#guide.pack(side= BOTTOM)
halflife = Button (main, text = "Half Life Simulation", width=75, height=4, command = open2)
halflife.pack(side = BOTTOM)

main.mainloop()
