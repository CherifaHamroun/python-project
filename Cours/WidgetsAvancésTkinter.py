#coding:utf-8
"""
Types de Modals:
showerror
showinfo
showwarning
askquestion
askokcancel
askyesno
askretrycancel
"""
import tkinter
from tkinter import messagebox
def showModalWindow():
    messagebox.askquestion("Sondage","Un probleme est survenu?")
app = tkinter.Tk()
btn = tkinter.Button(app,text = "Déclencher une erreur", command = showModalWindow)
btn.pack()
check_widget =tkinter.Checkbutton(app,text="chocher",offvalue = 2,onvalue=5,height = 2,width = 5)
radio_widget = tkinter.Radiobutton(app,text = "homme",value = 1)
radio_widget2 = tkinter.Radiobutton(app,text = "femme",value=2)
scale_w = tkinter.Scale(app,from_=100,to=1000,tickinterval=25)
spin_w= tkinter.Spinbox(app,from_=1,to = 10)
lb = tkinter.Listbox(app)
lb.insert(1,"Windows")
lb.insert(2,"linux")
lb.insert(3,"MacOs")
lb.pack()
spin_w.pack()
scale_w.pack()
radio_widget.pack()
radio_widget2.pack()
check_widget.pack()
app.mainloop()