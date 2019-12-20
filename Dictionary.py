from tkinter import *
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
from tkinter import messagebox
import PyInstaller
import json

data = json.load(open("076 data.json"))
window = Tk()

window.configure(background="#a1dbcd")
#window.wm_iconbitmap('dict_icon.png')
window.wm_title("My Dictionary")


def search_meaning():
    meanE.delete(0, END)
    w = textE.get()
    w = w.lower()
    if w in data:
        for i in data[w]:
            meanE.insert(END,i)
    elif len(get_close_matches(w,data.keys(),1,0.8))>0:
        word = get_close_matches(w,data.keys(),1,0.8)[0]
        word = word.upper()
        result = messagebox.askquestion("Warning",'Did You mean...  '+word,icon='warning')
        if result == 'yes':

            word = word.lower()
            textE.delete(0,END)
            textE.insert(0,word)
            for j in data[word]:
                meanE.insert(END,j)
        else:
            messagebox.showerror("Sorry", 'The word "%s" doesn\'t exist!!' % w)
            textE.delete(0, END)
    else:
        messagebox.showerror("Sorry", 'the Word "%s" doesn\'t exist!!'%w)
        textE.delete(0,END)

def clear_command():
    textE.delete(0,END)
    meanE.delete(0,END)

textL = Label(window, text='WORD', font=("Helvetica",10))
textL.grid(row=0, column=0)
textE = Entry(window)
textE.grid(row=0, columnspan=7)

meanL = Label(window, text='MEANING', font=("Helvetica",10))
meanL.grid(row=1, column=0)
mean_text = StringVar()
meanE = Listbox(window, width=80)
meanE.grid(row=1, column=2)

#list1 = Listbox(window, height=9, width=35)
#list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=1,column=8,rowspan=7)

meanE.configure(yscrollcommand=sb1.set)
sb1.configure(command=meanE.yview)

sb2 = Scrollbar(window, orient="horizontal")
sb2.grid(row=9,columnspan=9)
meanE.configure(xscrollcommand=sb2.set)
sb2.configure(command=meanE.xview)

searchB = Button(window, text='SEARCH',command=search_meaning, font=("Helvetica",10))
searchB.grid(row=11, column=1)

clearB = Button(window, text='CLEAR', command=clear_command, font=("Helvetica",10) )
clearB.grid(row=11, column=2)

closeB = Button(window, text='CLOSE', command=window.destroy, font=("Helvetica",10)) #, fg="#a1dbcd", bg="#383a39"
closeB.grid(row=11, column=3)

window.mainloop()
