import Tkinter
from Tkinter import *

main=Tk()

firstbutton = Button (main, text = "first button", width=50, height=4)
firstbutton.pack()
secondbutton = Button (main, text = "second button", width=50, height=4)
secondbutton.pack(side= BOTTOM)
thirdbutton = Button (main, text = "third button", width=50, height=4)
thirdbutton.pack(side = BOTTOM)
main.mainloop()
