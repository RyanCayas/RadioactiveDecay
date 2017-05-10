from Tkinter import *
from PIL import ImageTk, Image

global main
main=Tk()
main.title("References")


def openreferences(): #calls the script for the references
    main.destroy()
    import references

img = ImageTk.PhotoImage(Image.open("atom.png"))#image at the top
panel = Label(main, image = img) 
panel.pack()

TitlePage = Label(main, text = "Radioactive Decay", font = ("Source Sans Pro",50)) #creates the title of the page
TitlePage.pack()
ref = Button (main, text = "REFERENCES", width=75, height=4, command = openreferences) #creates the button for the references
ref.pack()


main.mainloop()
