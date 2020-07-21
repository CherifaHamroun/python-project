#coding:utf8
#Examination et analyse d'objets leurs meths attributs fonctions et services
class  Item:
    """
    Classe définissant un objet d'un jeu
    """
    def __init__(self,name,category,description,costvalue=1):
        self.name = name
        self.category = category
        self.description = description
        self.costvalue = costvalue

    def toString(self):
        print("---------------------")
        print(f"{self.name}-{self.category}\n> {self.description}\n> Prix d'achat :{self.costvalue}")
        print("---------------------")
"""
Fonctions qui permettent l'analyse d'un objet:
    hasattr()
    getattr()
    callable()
    isinstance()
    issubclass()
"""
#Code principal
it1 = Item("Epée en mousse","Arme","Magnifique épée au tranchant inexistant")
it2 = Item("Arc en bois de hetre","Arme","Magnifique arc des grands archers")
#print(dir(it1))
#print(__name__)
print(id(it1))
print(id(it2))
if isinstance(it1,Item):
    print("oui")
else:
    print("non")
print(it1.__dict__)
print(it1.__dict__["description"])
print(it1.__doc__)
#it1.toString()
#help(it1)
#help("modules")
#help("math")
#help("sys")