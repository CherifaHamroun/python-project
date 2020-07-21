#coding:utf8
import tkinter
"""
<nom variable> = <nom widget>(<widget parent>,<parametres>,...)

"""
def hello():
    print("hello")
app = tkinter.Tk()
label_welcome=tkinter.Label(app,text = "Bienvenu")# au lieu de text justify qui fait meme effet que pack
print(label_welcome.cget("text"))
print(label_welcome["text"])
label_welcome.configure(text ="text")
label_welcome.pack()
message_welcome = tkinter.Message(app,text ="Bonjour\n tout le monde bienvenu sur la chaine formation vidéo")
message_welcome.pack()
entry_name = tkinter.Entry(app,width = "45",show = "*",exportselection=0)#export selection vers presse papier interdite
entry_name.pack()
button_quit = tkinter.Button(app,text = "Quitter",width =25,height =2,command =hello)
button_quit.pack()
app.mainloop()