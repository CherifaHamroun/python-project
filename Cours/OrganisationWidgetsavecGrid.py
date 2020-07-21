#coding:utf-8
import tkinter
app = tkinter.Tk()
app.geometry("640x480")
app.title("Systeme de grilles")
label = tkinter.Label(app,text="Mon Text")
btn = tkinter.Button(app,text="Mon Bouton")
entry = tkinter.Entry(app)
label.grid(row = 0,column = 0,columnspan =2,rowspan =2,padx =10,pady=10,sticky="ne")
entry.grid(row = 2,column = 0)
btn.place(x=100,y=100)

app.mainloop()