#coding:utf-8
class Lapin:
    def __init__(self,name,weight):
        self.name = name 
        self.weight = weight
    def __repr__(self):
        return f"Lapin {self.name} qui pèse {self.weight} kg"
    def __eq__(self,other):
        if self.weight == other.weight:
            return True
        else:
            return False

lp = Lapin("Coco",24)
lp2 = Lapin("Kiki",7)
print(lp)
print(lp==lp2)