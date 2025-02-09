from tkinter import*
import tkinter as tk

t=Tk()
t.title("Calculator")
t.geometry("800x600")

window=Frame(t,width=800,height=600)
window.configure(bg='black')
header=Label(window,text="Calculator",font="times 50 bold",bg="black",fg="white").place(x=250,y=0)
window.pack()
k=1
exp=""
expression=StringVar()
paswed=Entry(window,textvariable=expression,width=30, font=('Arial 30')).place(x=50,y=100)

def press(val):
    global exp
    if(val=="="):
        try:
            result=eval(exp)
            exp=""
            expression.set(result)
        except:
            expression.set("Invalid")
    elif(val=="clear"):
        exp=""
        expression.set("")
    elif(val=="del"):
        exp=exp[0:len(exp)-1]
        expression.set(exp)
    else:
        exp+=val
        expression.set(exp)
for i in range(0,3):
    for j in range(0,3):
            button=Button(window,text=k,font="times 30",command=lambda k=k:press(str(k)),bg="salmon1",width=5).place(x=50+j*150,y=200+i*100)
            k+=1
zero=Button(window,text="0",font="times 30",command=lambda:press("0"),bg="salmon1",width=5).place(x=200,y=500)
decimal=Button(window,text=".",font="times 30",command=lambda:press("."),bg="cyan",width=5).place(x=50,y=500)
equal=Button(window,text="=",font="times 30",command=lambda:press("="),bg="cyan",width=5).place(x=350,y=500)
plus=Button(window,text="+",font="times 30",command=lambda:press("+"),bg="cyan",width=5).place(x=500,y=500)
minus=Button(window,text="-",font="times 30",command=lambda:press("-"),bg="cyan",width=5).place(x=500,y=400)
multiply=Button(window,text="*",font="times 30",command=lambda:press("*"),bg="cyan",width=5).place(x=650,y=500)
divide=Button(window,text="/",font="times 30",command=lambda:press("/"),bg="cyan",width=5).place(x=650,y=400)
clear=Button(window,text="Clear",font="times 30",command=lambda:press("clear"),bg="red",width=12).place(x=500,y=200)
delete=Button(window,text="Delete",font="times 30",command=lambda:press("del"),bg="red",width=12).place(x=500,y=300)



