from cProfile import label
from tkinter import *
from turtle import bgcolor
import random
from PIL import Image,ImageTk
#main window
root =Tk()
root.title("R/S/P")
col='light blue'
root.configure(background=col) #or enter hex value

#pics
rock_img=ImageTk.PhotoImage(Image.open('rock.jpg'))
paper_img=ImageTk.PhotoImage(Image.open('paper.png'))
sci_img=ImageTk.PhotoImage(Image.open('scissor.png'))

#insert pic
user_label=Label(root,image=rock_img,bg=col)
comp_label=Label(root,image=paper_img,bg=col)
#grid method to place label
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=6)

#scores

player_score=Label(root,text=0,font=100,bg=col,fg='black')
comp_score=Label(root,text=0,font=100,bg=col,fg='black')

comp_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

#indicator
user_indi=Label(root,font=50,text="USER").grid(row=0,column=3)
comp_indi=Label(root,font=50,text='COMP').grid(row=0,column=1)

#message
msg=Label(root,font=50,bg=col)
msg.grid(row=3,column=2)



#update message
def updateMessage(x):
    msg['text']=(x)
#update user score
def updateUserScore():
    score=int(player_score['text'])
    score+=1
    player_score['text']=str(score)
def updateCompScore():
    score=int(comp_score['text'])
    score+=1
    comp_score['text']=str(score)

#winner

def check(player,comp):
    if player==comp:
        updateMessage('Its a tie')
    elif (player=='rock'and comp=='paper') or (player=='paper' and comp=='scissor') or (player=='scissor' and comp=='rock'):
        updateMessage('You loose')
        updateCompScore()
    else:
        updateMessage('you win')
        updateUserScore()



#updatechoice

choices=['rock','paper','scissor']
def choiceupdate(x):

    #for comp
    compchoice=choices[random.randint(0,2)]
    if compchoice=='rock':
        comp_label.configure(image=rock_img)
    elif compchoice=='paper':
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=sci_img)

    #for user
    if x=='rock':
        user_label.configure(image=rock_img)
    elif x=='paper':
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=sci_img)
    check(x,compchoice)

#button
#choiceupdate passes argument 'rock'/'paper'
rock=Button(root,width=20,height=2,text='ROCK',bg='deep sky blue',fg='white',command= lambda:choiceupdate('rock'))
rock.grid(row=2,column=1)
paper=Button(root,width=20,height=2,text='PAPER',bg='deep sky blue',fg='white',command= lambda:choiceupdate('paper'))
paper.grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text='SCISSOR',bg='deep sky blue',fg='white',command= lambda:choiceupdate('scissor'))
scissor.grid(row=2,column=3)


root.mainloop()