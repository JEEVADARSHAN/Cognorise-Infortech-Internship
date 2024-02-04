import random as r
from tkinter import*
from tkinter.ttk import*

def generator():
    entry.delete(0,END)
    length=var1.get()

    weak=list(range(97,123))
    medium=list(range(97,123))+list(range(65,90))
    strong="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password=""

    if(var.get()=="w"):
        for i in range(0,length):
            password=password+chr(r.choice(weak))
        return password
    elif(var.get()=="m"):
        for i in range(0,length):
            password=password+chr(r.choice(medium))
        return password
    elif(var.get()=="s"):
        for i in range(0,length):
            password=password+r.choice(strong)
        return password
    
def generate():
    password1 = generator()
    entry.insert(10, password1)
    
t=Tk()
var=StringVar()
var.set("m")
var1=IntVar()
t.title("Password Generator")
t.geometry("1090x200")

r_word=Label(t,text="Password",font='Arial 30').grid(row=0)
entry = Entry(t,font='Arial 30')
entry.grid(row=0, column=1)
import tkinter as tkk
p_len=Label(t,text="Length",font='Arial 30').grid(row=1,pady=50)
g_button=tkk.Button(t,text="Generate",font='Arial 20',command=generate).grid(row=0,column=2)

radio_weak=tkk.Radiobutton(t,text="Weak",font='Arial 20',variable=var,value="w").grid(row=1, column=2)
radio_medium=tkk.Radiobutton(t,text="Medium",font='Arial 20',variable=var, value="m").grid(row=1, column=3, sticky='E')
radio_strong=tkk.Radiobutton(t,text="Strong",font='Arial 20',variable=var, value="s").grid(row=1, column=4, sticky='E')

l = Combobox(t, textvariable=var1,font='Arial 30')
l['values']=(4,6,8,12,16,"Custom")
l.current(0)
l.bind('<<ComboboxSelected>>')
l.grid(column=1,row=1)

t.mainloop()



