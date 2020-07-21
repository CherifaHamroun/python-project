#coding:utf-8
import tkinter
app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement de widgets")
main_frame = tkinter.Frame(app,width = 300,height =200)
label_frame = tkinter.LabelFrame(app,text="Mon cadre",width = 300,height =200)
btn = tkinter.Button(app,text = "bienvenu")
label = tkinter.Label(app,text="Le label")
main_frame.pack(side ="bottom",fill="none")
label.pack(side="left",ipadx=100,ipady=100)
btn.pack(side="top",expand=1,fill="both")
label_frame.pack(side = "right",expand =1,padx=100,pady=100)
app.mainloop()