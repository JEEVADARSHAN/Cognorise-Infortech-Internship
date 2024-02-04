from tkinter import*
import tkinter
import random as r

t=Tk()
t.geometry("800x600")
t.title("Dice Simulator")

window=Frame(t,width=800,height=600,bg="navy")
window.pack()

trial=IntVar()
sides=IntVar()

def roll():
    tries=trial.get()
    side=sides.get()
    result=""
    l3.configure(text=result)
    for i in range(0,tries):
        result+="Trial "+str(i+1)+"= "+str(r.randint(1,side))+"\t"
        l3.configure(text=result)
        if(i in range(2,tries,3)):
            result+="\n"

h1=Label(window,text="Welcome Back",font="times 50 bold",bg="navy",fg="white").place(x=175,y=50)
l1=Label(window,text="Enter the Number of sides:",font="times 25 bold",bg="navy",fg="white").place(x=10,y=150)
l2=Label(window,text="Enter the Number of trial:",font="times 25 bold",bg="navy",fg="white").place(x=10,y=200)

b1=Button(window,text="Generate",command=roll,font="times 25 bold")
b1.place(x=600,y=165)

l3=Label(window,font="times 25 bold",bg="navy",fg="white")
l3.place(x=50,y=250)

from tkinter import ttk
s = ttk.Combobox(t, textvariable=sides,font='Arial 25',width=5)
s['values']=(2,3,4,5,6,8,12,16,"Custom")
s.current(0)
s.bind('<<ComboboxSelected>>')
s.place(x=450,y=150)

t = ttk.Combobox(t, textvariable=trial,font='Arial 25',width=5)
t['values']=(1,2,3,4,5,6,8,12,16,"Custom")
t.current(0)
t.bind('<<ComboboxSelected>>')
t.place(x=450,y=200)

t.mainloop()
