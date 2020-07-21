#coding:utf-8
"""
add_checkbutton()
add_radiobutton()
add_separator()
"""

import tkinter
def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    lb= tkinter.Label(about_window,text ="apropos")
    lb.pack()
app=tkinter.Tk()
app.geometry("640x480")
app.title("Menu")
mainmenu = tkinter.Menu(app)
firstmenu = tkinter.Menu(mainmenu,tearoff=0)
firstmenu.add_command(label = "A propos",command =show_about )
firstmenu.add_command(label = "option 2")
firstmenu.add_command(label = "Quitter",command = app.quit)
secondmenu = tkinter.Menu(mainmenu)
secondmenu.add_command(label = "Commande A")
secondmenu.add_command(label = "Commande B")
secondmenu.add_command(label = "Commande C")
mainmenu.add_cascade(label ="Premier",menu = firstmenu)
mainmenu.add_cascade(label="Deuxieme",menu = secondmenu)
app.config(menu = mainmenu)
app.mainloop()