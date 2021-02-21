from tkinter import *
import datetime
from tkinter.messagebox import *
from tkinter.font import *
from tkinter.ttk import *
import winsound

obj = Tk()
obj.geometry("600x400")


def alarm():
    if C1.get() == "AM":
        x = int(E1.get())
        y = int(E2.get())

    if C1.get() == "PM":
        x = int(E1.get())+12
        y = int(E2.get())

    showinfo("Notification", "Alarm has been set")

    while True:
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
            #showinfo("Notification", "WAKEUP!")
            for i in range(0,100):
                winsound.Beep(10000, 100)
            break


T1 = Label(obj, text="HOURS:", )
T2 = Label(obj, text="MINUTES:")
T1.grid(row=0, column=0)
T2.grid(row=1, column=0)
E1 = Entry(obj)
E2 = Entry(obj)
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
B1 = Button(obj, text="Set Alarm", command=alarm)
B1.grid(row=2, column=1)
C1 = Combobox(obj, values=["AM", "PM"])
C1.grid(row=0, column=2)
T3 = Label(obj, text="AM or PM")
T3.grid(row=0, column=3)
obj.mainloop()
