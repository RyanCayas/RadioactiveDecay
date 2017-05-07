import sys
import tkFileDialog
from tkFileDialog import askopenfilename
import Tkinter
from Tkinter import *



main=Tk()
main.title("Main Menu")


def open1():
    main.withdraw()
    import radioactive

TitlePage = Label(main, text = "Main Menu", font = "Jokerman 50")
TitlePage.pack()
alpha = Button (main, text = "Alpha Decay", width=50, height=4, command = open1)
alpha.pack()
halflife = Button (main, text = "Half Life", width=50, height=4)
halflife.pack(side= BOTTOM)
guide = Button (main, text = "User's Guide", width=50, height=4)
guide.pack(side = BOTTOM)

main.mainloop()
