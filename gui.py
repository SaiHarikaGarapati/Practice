from tkinter import *
from random import choice

App = Tk()
App.title("Element picker")
App.geometry("300x300")
App["background"] = 'grey'

inp = Entry(App, background='black', foreground="white")
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=10)


def pick():
    inp1 = (inp.get()).split(",")
    choose = "chose:" + str(choice(inp1))
    msg = Label(App, text=choose, font=('Courier', 12), background="black", foreground="yellow")
    msg.grid(row=2, column=0, columnspan=2, padx=45, pady=5)


B = Button(App, text="choose", command=pick, background="black", foreground="yellow")
B.grid(row=1, column=0, padx=25, pady=10)
quitB = Button(App, text="Cancel", command=App.quit, background="black", foreground="yellow")
quitB.grid(row=1, column=1, padx=25, pady=10)
App.mainloop()
