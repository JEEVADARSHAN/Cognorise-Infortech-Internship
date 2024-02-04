from tkinter import *
import random as r
t=Tk()
hs=0
bs=0
t.title("GAME")
t.geometry("800x600")
t.configure(bg="black")
menu=Frame(t)
menu.configure(bg="black")
menu.pack()

l1=Label(menu,text="ROCK  PAPER  SCISOR",font= ("Helvetica 34 bold italic"),bg="black",fg='yellow')
op1=Button(menu,text="Play",font=("Times 20 bold"),command=lambda: scrn(),bg="cyan",width=31)
l1.grid(row=1,column=2,pady=50)
op1.grid(row=2,column=2,pady=100)

moves=['rock','paper','scisor']
def scrn():
    game=Frame(t)
    menu.forget()
    game.pack()
    game.configure(bg='black')
    
    rock=Button(game,text="Rock",bg='blue',command=lambda:match("rock"),font= ("Helvetica 20 bold"),height=2, width=10,fg="white")
    paper=Button(game,text="Paper",bg='blue',command=lambda: match("paper"),font= ("Helvetica 20 bold"),height=2, width=10,fg="white")
    scisor=Button(game,text="Scisor",bg='blue',command=lambda: match("scisor"),font= ("Helvetica 20 bold"),height=2, width=10,fg="white")
    d=Label(game,text="Choose Your Move",font=("Times 30"),bg="black",fg='gold')

    d.grid(row=1,column=2,pady=50)
    rock.grid(row=5,column=1,pady=50)
    paper.grid(row=5,column=2,pady=50)
    scisor.grid(row=5,column=3,pady=50)

    def match(pm):
        final=Frame(t)
        final.pack()
        final.configure(bg='black')
        game.forget()
 
        cm=r.choice(moves)
        if(cm==pm):
            result="DRAW"
        elif((cm=="rock" and pm=="paper")or(cm=="paper" and pm=="scisor")or(cm=="scisor" and pm=="rock")):
            result="PLAYER WON"
            global hs 
            hs+=1
        else:
            result="BOT WON"
            global bs
            bs+=1
        shs=str(hs)
        sbs=str(bs)
        scores="SCORE \n Player: "+shs+" \n Bot: "+sbs
        m="YOUR MOVE "+(pm.upper())+"\nBOT MOVE "+(cm.upper())
        
        d=Label(final,text=m,font=("Helvetica 20 bold italic"),bg="black",fg='yellow')
        d.grid(row=2,column=1,pady=10)
        l=Label(final,text=result,font=("Helvetica 30 bold italic"),bg="black",fg='white')
        s=Label(final,text=scores,font=("Times 20 bold"),bg="black",fg='yellow')
        s.grid(row=3,column=1)
        l.grid(row=1,column=1,pady=50)
        ch=Label(final,text="Do you wish to continue?",font=("Times 20"),bg="black",fg="salmon1")
        ch.grid(row=4,column=1)
        yes=Button(final,text="Continue",font=("Times 30 bold"),bg="LemonChiffon2",command=lambda:finish(),width=10,fg="black")
        no=Button(final,text="Exit",font=("Times 30 bold"),bg="LemonChiffon2",command=lambda:t.destroy(),width=10,fg="black")
        yes.grid(row=5,column=0,pady=50)
        no.grid(row=5,column=2,pady=50)
        def finish():
            final.forget()
            scrn()
t.mainloop()
