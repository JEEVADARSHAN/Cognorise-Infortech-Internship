from tkinter import*
from tkinter import messagebox
import time
from datetime import datetime
t=Tk()
t.title("Countdown timer")
t.geometry("800x600")
t.configure(bg="SteelBlue")

counter = 66600
running = False
def stopClock():
    s_scn=Frame(t,bg="SteelBlue",width=800,height=600)
    s_scn.pack()

    def counter_label(label): 
        def count(): 
            if running: 
                global counter  
                if counter==66600:             
                    display="Starting..."
                else:
                    tt = datetime.fromtimestamp(counter)
                    string = tt.strftime("%H:%M:%S")
                    display=string
                    label.config(text=display) 
 
                label.after(1000, count)  
                counter += 1 
        count()      

    def Start(label): 
        global running 
        running=True
        counter_label(label) 
        start['state']='disabled'
        start.config(bg="salmon")
        stop['state']='normal'
        stop.config(bg="lightblue1")
        reset['state']='normal'
        reset.config(bg="lightblue1")

    def Stop(): 
        global running 
        start['state']='normal'
        start.config(bg="lightblue1")
        stop['state']='disabled'
        stop.config(bg="salmon")
        reset['state']='normal'
        reset.config(bg="lightblue1")
        running = False

    def Reset(label): 
        global counter 
        counter=66600

        if running==False:       
            reset['state']='disabled'
            stop.config(bg="salmon")
            label['text']='00:00:00'
        else:                
            label['text']='Starting...'

    def loadB():
            s_scn.forget()
            mainScn()

    lbl=Label(s_scn, text="Stop Clock",bg="SteelBlue", fg="white", font="Verdana 40 bold").place(x=245,y=25) 
    label = Label(s_scn, text="00:00:00",bg="SteelBlue", fg="white", font="Verdana 40 bold") 
    label.place(x=255,y=100) 

    start =Button(s_scn, text='Start', width=6,font="times 30 bold",bg="lightblue1", command=lambda:Start(label)) 
    stop = Button(s_scn, text='Stop',width=6,font="times 30 bold",bg="lightblue1",state='disabled', command=Stop) 
    reset = Button(s_scn, text='Reset',width=6,font="times 30 bold",bg="lightblue1", state='disabled', command=lambda:Reset(label)) 
    start.place(x=325,y=200) 
    stop.place(x=325,y=300) 
    reset.place(x=325,y=400)
    backBtn=Button(s_scn, text='Back',bg="tomato",font="times 20 bold",command=lambda: loadB())
    backBtn.place(x=5,y=500)

def timer():
    t_scn=Frame(t,width=800,height=600,bg="SteelBlue")
    t_scn.pack()
    hour=StringVar()
    minute=StringVar()
    second=StringVar()

    hour.set("00")
    minute.set("00")
    second.set("00")

    Lbl=Label(t_scn,text="Hr:    Min:   Sec:", font=("Arial",30,""),bg="SteelBlue",fg="white").place(x=250,y=200)

    hourEntry= Entry(t_scn, width=3, font=("Arial",30,""),textvariable=hour)
    hourEntry.place(x=250,y=250)
  
    minuteEntry= Entry(t_scn, width=3, font=("Arial",30,""),textvariable=minute)
    minuteEntry.place(x=350,y=250)
  
    secondEntry= Entry(t_scn, width=3, font=("Arial",30,""),textvariable=second)
    secondEntry.place(x=450,y=250)

    title=Label(t_scn,text="Timer",font=("Arial 60"),bg="SteelBlue",fg="white").place(x=275,y=100)
    def submit():
        try:
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            mins,secs = divmod(temp,60) 
            hours=0
            if mins >60:
                hours, mins = divmod(mins, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            t_scn.update()
            time.sleep(1)

            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")

            temp -= 1

    def loadB():
            t_scn.forget()
            mainScn()
    btn = Button(t_scn, text='Set Time Countdown', bd='5',bg="aquamarine2",font="times 30 bold",command= submit)
    btn.place(x = 200,y = 320)
    backBtn=Button(t_scn, text='Back',bg="tomato",font="times 20 bold",command=lambda: loadB())
    backBtn.place(x=5,y=500)
    t_scn.mainloop()

def mainScn():
    scn=Frame(t,width=800,height=600,bg="SteelBlue")
    scn.pack()
    td=datetime.now().date()
    def timing():
        current_time = time.strftime("%H : %M : %S %p")
        clock.config(text=current_time)
        clock.after(1000,timing)
    def load(Screen):
        scn.forget()
        if(Screen=="tmr"):
            timer()
        else:
            stopClock()
    clock=Label(scn,font="times 70 bold",bg="SteelBlue",fg="white")
    clock.place(x=100,y=50)
    date=Label(scn,text=td,font="times 30 bold",bg="SteelBlue",fg="white").place(x=300,y=150)
    timing()
    
    _clock=Button(scn,text="Stop Clock",width=15,bg="thistle",font="times 30 bold",command=lambda:load("stpC"))
    _timer=Button(scn,text="Timer",width=15,bg="thistle",font="times 30 bold",command=lambda:load("tmr"))

    _clock.place(x=225,y=250)    
    _timer.place(x=225,y=350)

    
mainScn()
