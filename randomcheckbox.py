from tkinter import *
from random import choice, sample

App = Tk()
App.title("Element picker")
App.geometry("300x300")


inp = Entry(App, width=25)
inp.grid(row=0, column=0, columnspan=2, padx=25, pady=5)
no_choice = IntVar()
chk = Checkbutton(App, text='Checkbox', variable=no_choice, onvalue=2, offvalue=1)
chk.deselect()
chk.grid(row=1, column=0, columnspan=2, padx=25, pady=5)


def pick():
    inp1 = (inp.get()).split(",")
    if no_choice.get() == 2:
        chooose = "Choice: "+str(sample(inp1, 2))
    else:
        chooose = "Choice: "+str(sample(inp1, 1))
    msg = Label(App, text=chooose, width=15)
    msg.grid(row=4, column=0, columnspan=2, padx=45, pady=5)
    if quitB['state'] == DISABLED:
        quitB['state'] = NORMAL


B = Button(App, text="choose", command=pick)
B.grid(row=2, column=0, padx=35, pady=10)
quitB = Button(App, text="Cancel", command=App.quit)
quitB.grid(row=2, column=1, padx=35, pady=10)
App.mainloop()
