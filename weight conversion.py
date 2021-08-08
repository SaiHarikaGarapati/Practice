from tkinter import *
weightWindow = Tk()
weightWindow.title("Weight Conversion")
weightWindow.geometry("600x400")
weightWindow["background"] = "silver"


def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)


e1 = Label(weightWindow, text="Enter the weight in kg:")
e2_value = StringVar()
e2 = Entry(weightWindow, textvariable=e2_value)
e3 = Label(weightWindow, text="Gram")
e4 = Label(weightWindow, text="Pounds")
e5 = Label(weightWindow, text="ounce")
t1 = Text(weightWindow, height=1, width=20)
t2 = Text(weightWindow, height=1, width=20)
t3 = Text(weightWindow, height=1, width=20)
b1 = Button(weightWindow, text="Convert", relief="raised", command=from_kg)
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
b1.grid(row=0, column=2)
weightWindow.mainloop()
