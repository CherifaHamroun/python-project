#coding:utf-8
name = "Jason"
def show():
    global name
    name = "luc"
    print(name)
show()
liste = [1,2,3]
#ref 
list2 = liste
#copy
liste2 = list(liste)