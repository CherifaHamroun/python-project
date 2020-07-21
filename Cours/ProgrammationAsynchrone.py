#coding:utf-8
import time
import threading
mylock = threading.RLock()
class myProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        i =0
        while i<3:
            with mylock:
                lettres = "ABC"
                for it in lettres:
                    print(it)
                    time.sleep(0.3)
            i +=1

th1 = myProcess()
th2 = myProcess()

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin du programme")
"""def process_1():
    i =0
    while i<3:
        print("Process one")
        time.sleep(0.3)
        i +=1
def process_2():
    i =0
    while i<3:
        print("Process two")
        time.sleep(0.3)
        i +=1
#programmation parallèle = thread
th1 = threading.Thread(target = process_1)
th2 = threading.Thread(target = process_2)

th1.start()
th2.start()

th1.join()
th2.join()
print("Fin du programme")"""