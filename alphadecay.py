from Tkinter import *
from PIL import ImageTk, Image

#runs the script with image
root = Tk()
img = ImageTk.PhotoImage(Image.open("alphadecay.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
