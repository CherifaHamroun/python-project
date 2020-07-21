#coding:utf-8
import tkinter
#from tkinter import *
mainapp = tkinter.Tk()
mainapp.title("Ma première fenetre")
mainapp.minsize(640,480)
mainapp.maxsize(900,800)
mainapp.resizable(width = False,height = False)
mainapp.positionfrom("user")
mainapp.sizefrom("user")
#geometry("XxY+posx+posy")
screen_X = mainapp.winfo_screenwidth()
screen_Y =mainapp.winfo_screenheight()
window_X =800
window_Y =600
pos_x = (screen_X//2)-(window_X//2)
pos_y = (screen_Y//2)-(window_Y//2)
mainapp.geometry("{}x{}+{}+{}".format(window_X,window_Y,pos_x,pos_y))

mainapp.mainloop()