#coding:utf-8
import tkinter
"""
StringVar()
IntVar()
DoubleVar()
BooleanVar()
"""
#OBSERVER
def update_label(*args):
    var_label.set(var_entry.get())
def update_radio(*args):
    if var_gender.get()==0:
        print("Sexe : Femme")
    else:
        print("Sexe : Homme")
def update_label_gender(*args):
    if var_gender.get():
        var_label_gender.set("Homme")
    else:
        var_label_gender.set("Femme")
app = tkinter.Tk()
app.geometry("480x300")
app.title("Variables de controle")
var_entry = tkinter.StringVar()
var_entry.trace("w",update_label)#modes:r ou u
entry =tkinter.Entry(app,textvariable= var_entry)
var_label = tkinter.StringVar()
var_label.set("coucou")
label = tkinter.Label(app,text = "Bonjour",textvariable = var_label)
print("label :",var_label.get())
var_gender = tkinter.IntVar()
var_gender.trace("w",update_radio)
radio1 = tkinter.Radiobutton(app,text="Homme",value=1,variable=var_gender)
radio2 = tkinter.Radiobutton(app,text="Femme",value=0,variable = var_gender)
var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app,textvariable = var_label_gender)
var_gender.trace("w",update_label_gender)
label.pack()
entry.pack()
radio1.pack()
radio2.pack()
label_gender.pack()
app.mainloop()