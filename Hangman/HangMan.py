from tkinter import*
import tkinter
import random as r

t=Tk()
life=7
result=""
lives=chance=None
hangImg=["hang0.png","hang1.png","hang2.png","hang3.png","hang4.png","hang5.png","hang6.png"]
state=-1

def game():
    global lives
    def gameOver():
        def retry():
            g_over.forget()
            game()
        global state,life
        state=-1
        life=7
        gameScn.forget()
        g_over=Frame(t,width=800,height=600)
        g_over.configure(bg="LemonChiffon2")
        g_over.pack()
        l5=Label(g_over,text=result,font="times 50 bold",bg="LemonChiffon2",fg="red").place(x=225,y=50)
        re=Button(g_over,text="Play Again",font="times 30 bold",width=10,command=lambda:retry())
        re.place(x=260,y=300)
        e=Button(g_over,text="Exit",font="times 30 bold",width=10,command=lambda:t.destroy()).place(x=260,y=400)
    def check():
        global life,result,state,chance
        letter=e1.get()
        for i in range(0,len(target)):
            if(letter.lower()==target[i] and letter!=""):
                dash[i]=letter.upper()
                l3.configure(text=dash)
                target[i]=""
                e1.delete(0,END)
                break
        else:
            if(letter!=""):           
                life-=1
                state+=1
                chance=PhotoImage(file = hangImg[state])
                chance=chance.zoom(2,2)
                c.itemconfig(temp,image=chance)
                wrong.append(letter)
                l4.configure(text=wrong)
                e1.delete(0,END)
        if(life<=0):
            result="Game Over"
            gameOver()
        elif(target.count(target[0])==len(target)):
            result="You Won"
            gameOver()
    window.forget()
    gameScn=Frame(t,width=800,height=600)
    gameScn.configure(bg='white')
    gameScn.pack()
    
    words=["apple","banana","orange","kiwi","papaya","grape","lemon"]
    target=r.choice(words)
    target=list(target)
    guesses=0
    letter=StringVar()
    dash=list("_"*len(target))
    wrong=list("WrongLetters:")
    
    l1=Label(gameScn,text="Guess the Fruit",font="times 50 bold",bg="white",fg="red").place(x=150,y=50)
    l2=Label(gameScn,text="Enter your Guess",font="times 35 bold",bg="white").place(x=375,y=150)
    l3=Label(gameScn,text=dash,font="times 55 bold",bg="white")
    l3.place(x=400,y=200)
    e1=Entry(gameScn,textvariable=letter,width=5,font='times 45',bg="LemonChiffon2")
    e1.place(x=400,y=300)
    s1=Button(gameScn,text="Submit",font="times 30",command=lambda:check())
    s1.place(x=550,y=295)
    l4=Label(gameScn,text=wrong,font="times 30 bold",bg="white")
    l4.place(x=150,y=500)

    c=Canvas(gameScn,bg="white",width=350,height=300,highlightthickness=0)
    c.place(x=0,y=200)
    temp=c.create_image(200,150,image=None)
                
t.title("Hangman Game")
t.geometry("800x600")
window=Frame(t,width=800,height=600)
window.pack()

c=Canvas(window,bg="white",width=400,height=400,highlightthickness=0)
c.place(x=0,y=200)
img=PhotoImage(file = hangImg[6])
img=img.zoom(2,2)
c.create_image(200,150,image=img)

window.configure(bg='white')
header=Label(window,text="Hangman Game",font="times 50 bold",bg="white",fg="red").place(x=150,y=100)

play=Button(window,text="Play",font="times 30 bold",width=10,command=lambda:game()).place(x=400,y=250)
exi=Button(window,text="Exit",font="times 30 bold",width=10,command=lambda:t.destroy()).place(x=400,y=350)




