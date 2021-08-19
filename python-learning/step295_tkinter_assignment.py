"""
# PART 1
from tkinter import *
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")

# PART 2
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)

# PART 3.1
from tkinter import *
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

# PART 3.2
l = Label(win, text="This is a label")
l.grid(row=1, column=0)

# PART 3.3
from tkinter import *
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

# PART 4.1
b1.configure(text="Uno")

# PART 4.2
def but1():
    print("Button one was pushed")
b1.configure(command=but1)

# PART 5.1
from tkinter import *
win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()

# PART 5.2
v.get()

# PART 5.3
v.set("this is set by the program")
"""

# PART 6.1
from tkinter import *
win = Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "1st entry")
lb.insert(END, "2nd entry")
lb.insert(END, "3rd entry")
lb.insert(END, "4th entry")

# PART 6.2
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)

# PART 6.3
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

# PART 6.4
lb.curselection()

