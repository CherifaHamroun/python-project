#coding:utf-8
"""
évenements
KeyPress   :Pression
KeyRelease :Relachement

"""
import tkinter
def func(event):
    print("La touche a a été pressée")

def func2(event):
    print("ici c n'importe quelle touche et n'importe quel bouton")

def func3(event):
    print("Bah ici c'est tt ce qui est entry")

def func4(event):
    print("Bah ici c tt ce qui est double cliqué")
def func5(event):
    print("teminée le top")
def func6(event):
    """
    attributs de event:
        x,y,x_root,y_root
        width,height
        state
        keysym,keycode
        widget
    """
    print(f"{event.keysym }/{event.keycode}")
    event.widget.destroy()
def func7(event):
    print(f"déclencheur parsonnalisé")
def openwindow():
    top =tkinter.Toplevel()
    label_w = tkinter.Label(top,text = 'Bonjour')
    label_w.bind('<Destroy>',func5)
    top.bind('<Escape>',func6)
    label_w.pack()
app = tkinter.Tk()
app.geometry("320x240")
entry_w = tkinter.Entry(app)
entry_w.bind('<KeyPress-a>',func)
entry_w.bind('<Button-1>',func)
#entry_w.bind('<KP_8>',func)
entry_w.bind('<Control-Alt-b>',func)
entry_w.bind('<Double-c>',func)
entry_w.bind('<Key>',func2)
entry_w.bind('<Button>',func2)
app.bind_class('Entry','<Double-Button-1>',func3)
app.bind_all('<Double-Button-1>',func4)
button_w = tkinter.Button(app,text = 'Ouvrir',command=openwindow)
label = tkinter.Label(app,text = "Hello World")
app.event_add('<<Click>>','<Button-1>','Button-2')
#delete a la place de add pour supprimer par exemple
app.bind('<<Click>>',func7)
button_w.pack()
entry_w.pack()
app.mainloop()
