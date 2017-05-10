from Tkinter import *
import tkMessageBox

root = Tk()
# Header for the Menu
root.title("Half Life Menu")

def start():
    import __builtin__
    __builtin__.Natoms = natoms.get()
    __builtin__.speed = speedscaler.get()
    __builtin__.Hlife = half.get()
    import halflife
        
start = Button (root,text = "START HALF LIFE SIMULATION", width = 50, height = 4, command = start)
start.pack()
# Slider that changes the value of the speed of the reaction
speedscaler = Scale(root, from_=10, to=200, orient=HORIZONTAL, length = 600, label = "Speed of Reactions")
speedscaler.pack()
#---------------------------
# Slider that changes the value of the number of atoms
natoms = Scale(root, from_=10, to=200, orient=HORIZONTAL, length = 600, label = "Number of Atoms")
natoms.pack()
#---------------------------
# Slider that changes the value of the half life
half = Scale(root, from_=5, to=50, orient=HORIZONTAL, length = 600, label = "Half Life")
half.pack()
#---------------------------
root.mainloop()
