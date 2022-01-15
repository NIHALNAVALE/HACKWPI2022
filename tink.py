# image to excel

from tkinter import *

app=Tk()
app.geometry("800x600")

def callback(e):
    label= Label(app, text= "You Pressed Enter")
    label.pack()


app.bind('<Return>', callback)

label = Label(app, text="")
label.pack()

app.mainloop()
