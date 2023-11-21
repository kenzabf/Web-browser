from tkinter import *

import webbrowser

def myFunction():
   link = mytext.get()
   webbrowser.open(link) 

myApp = Tk() 

myApp.title("Web Browser")
myApp.geometry("500x300")

mylabel = Label(myApp, text="Web Browser" , font="Tahoma 30 bold")
mylabel.pack(pady=30)

mytext = Entry(myApp, width= 50)
mytext.pack(pady=10)

mybutton= Button(myApp, text="Got to link" , fg= "blue" , font= " halvatica 10 bold", command=myFunction)
mybutton.pack()

myApp.mainloop()