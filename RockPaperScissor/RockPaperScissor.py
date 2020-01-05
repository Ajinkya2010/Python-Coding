import random
import tkinter as tk
from tkinter import PhotoImage
import os
from tkinter import *

window = tk.Tk()
window.geometry("600x800")
blank_space =" " # One empty space
window.title(40*blank_space+"Rock Paper Scissors")


My_Score = 0
Comp_Score = 0
My_Choice = ""
Comp_Choice = ""


def choice_to_number(choice):
    my_choice = {'rock':0,'paper':1,'scissor':2}
    return my_choice[choice]

def number_to_choice(number):
    my_choice={0:'rock',1:'paper',2:'scissor'}
    return my_choice[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,Comp_Choice):
    global My_Score
    global Comp_Score
    answer = ""
    user=choice_to_number(human_choice)
    comp=choice_to_number(Comp_Choice)
    if(user==comp):
        answer = "{w}\n\n Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n".format(uc=My_Choice,cc=Comp_Choice,u=My_Score,c=Comp_Score,w ="It's a Tie")
    elif((user-comp)%3==1):
        My_Score+=1
        answer = "{w} Win \n\n Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c}".format(uc=My_Choice,cc=Comp_Choice,u=My_Score,c=Comp_Score,w ="You")
    else:
        Comp_Score+=1
        answer = "{w} Win \n\n Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} \n".format(uc=My_Choice,cc=Comp_Choice,u=My_Score,c=Comp_Score,w ="Computer")

    text_area = tk.Text(master=window,height=8,width=30,bg="#C68383")
    text_area.grid(column=1,row=1)
    text_area.insert(tk.END,answer)



def rock():
    global My_Choice
    global Comp_Choice
    My_Choice='rock'
    Comp_Choice=random_computer_choice()
    result(My_Choice,Comp_Choice)

def paper():
    global My_Choice
    global Comp_Choice
    My_Choice='paper'
    Comp_Choice=random_computer_choice()
    result(My_Choice,Comp_Choice)

def scissor():
    global My_Choice
    global Comp_Choice
    My_Choice='scissor'
    Comp_Choice=random_computer_choice()
    result(My_Choice,Comp_Choice)

print(os.getcwd())
rock_path = os.path.join(os.getcwd(),'rock.png')
scissor_path = os.path.join(os.getcwd(),'scissors.png')
paper_path = os.path.join(os.getcwd(),'paper.png')

# Creating a photoimage object to use image
photo_rock = PhotoImage(file = rock_path)
photo_scissor = PhotoImage(file = scissor_path)
photo_paper = PhotoImage(file = paper_path)


photo_rock = photo_rock.zoom(25)
photo_rock = photo_rock.subsample(70)

photo_scissor = photo_scissor.zoom(25)
photo_scissor = photo_scissor.subsample(70)

photo_paper = photo_paper.zoom(25)
photo_paper = photo_paper.subsample(70)


label = Label(window, text="Rock")
label.grid(column=1, row=6)
button1 = tk.Button(text="Rock",image = photo_rock,command=rock)
button1.grid(column=1,row=7)
label = Label(window, text="Paper")
label.grid(column=1, row=8)
button2 = tk.Button(text="Paper",image = photo_paper,command=paper)
button2.grid(column=1,row=9)
label = Label(window, text="Scissor")
label.grid(column=1, row=10)
button3 = tk.Button(text="Scissor",image = photo_scissor ,command=scissor)
button3.grid(column=1,row=11)

window.mainloop()
