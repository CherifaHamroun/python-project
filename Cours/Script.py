#coding:utf-8
#Commentaire sur une ligne 
""" 
/////////////////////////////////////////////////////////////////// Les Bases //////////////////////////////////////////////////////////////////////////////////////////////////
les types : int 
            float
            str 
            bool
les opérateurs : +
                 -
                 *
                 %
                 /
les castings :  int()
                float()
                str()
                bool()
variable op=cpt
fonctions standards : print("")
                      var = input("")
                      str.format(op)
Opérateurs de conditions :  ==
                            !=
                            <
                            >
                            <=
                            >=
Opérateurs multiples :  and 
                        or 
                        in / not in

//////////////////////////////////////////////////////// Variables et Opérations //////////////////////////////////////////////////////////////////////////
print("Bonjour world\tceci est tabulé \nceci est un saut de ligne")
varInt = 12
varStr = "12"
varFloat = 12.12
varBool = True 
print(type(varInt))
print(type(varStr))
print("la valeur de la variable",varInt,".")
texte = "l'age de la personne est {} ans"
print(texte.format(varInt))
MonJoueur = input("Nom de joueur ?\n")
age = input('age')
age = bool(age)
dateNaissance = 2020-age
age +=1
print("Bienvenu",MonJoueur,"votre age est de",age)
print("votre DN est",dateNaissance)
///////////////////////////////////////////////////////////Les conditions////////////////////////////////////////////////////////////////////////

identifiant = "Cherifa"
motDePasse = "Cherifa is a queen"
print("Interface de connexion")
userId = input("Nom d'utilisateur :")
userPwd = input("Mot de passe :")
if userId==identifiant and userPwd == motDePasse :
        print("Vous etes maintenant connectés")
else :
    print("Erreur d'authentification")
if "a"  in "oo" : print("non")
elif "a" in "zz" : print("ouno")
else : print("oui")
////////////////////////////////////////////////////////////Les Boucles/////////////////////////////////////////////////////////////////////////

cpt = 0
while cpt<5 :
    print("je suis phrase",cpt)
    cpt+=1
continu = True
while continu :
    print("voulez vous quitter")
    menu=input(">")
    if menu == "again":
        continue
    elif menu == "quit":
        break
    else:
        print("Erreur")

print("Sortie")

sentence = "Bonjour tout le monde"
for letter in sentence:
    print(letter)

print("fini")
///////////////////////////////////////////////////////////////////////Les Fonctions//////////////////////////////////////////////////////////////

def dire_bjr():
    print("bonjour")

dire_bjr()
def dire(nom ="tom", message ="salut"):
    print("{} : {}".format(nom,message))
dire("tom","salut")
dire("cherifa")
dire(message="haha",nom="mee")

def show_inventory(*items):
    for item in items:
        print(item)

show_inventory("epais")
show_inventory("hhh","tttt","tt","hh")
////////////////////////////////////////////////////////////////////La modularité////////////////////////////////////////////////////////////////////
def calculer_somme(nb1,nb2):
    resultat = nb1 + nb2
    return resultat
print(calculer_somme(20,21))


import math
resultat = math.sqrt(100)
print(resultat)

from math import *
resultat = sqrt(100)
print(resultat)

import Module.player as player
player.parler("cherifa","euuuuh")
player.reparler()
/////////////////////////////////////////////////////////////////////Gestion d'erreurs//////////////////////////////////////////////////////////////

ageUtil=input("quel age as tu ?\n")
try:
    ageUtil = int(ageUtil)
    #print("tu as {} ans".format(ageUtil))
except:
    print("Erreur")
else :
    print("tu as {} ans".format(ageUtil))
finally :
    print("fin du programe")

nombre1 = 125
nombre2 = input("diviser 125 par ? ")
try:
    nombre2 = int(nombre2)
    print("Résultat = {}".format(nombre1 / nombre2))
except ZeroDivisionError:
    print("Division par zéro")
except ValueError :
    print("Division par un caactère alphanumérique")
except :
    print("Valeur incorrecte !")
else : print("Bravo !")
                                 /////////////////////
                                //      Raise      //
                               /////////////////////

try:
    age = input("Quel age as-tu ?")
    age = int(age)
    assert age > 25
except AssertionError :
    print("Erreur")
///////////////////////////////////////////////////////////////// Classes et attributs ///////////////////////////////////////////////////////////////////////////


class Humain  :
    humaincrees = 0
    def __init__(self,prenom,age):
        
        #self c pour l'adr de création de l'ojet humain instancié
        print("création de l'humain")
        self.prenom = prenom
        self.age = age
        Humain.humaincrees += 1

print("Lancement du programme")
h1 = Humain("jojo",12)
print("Prénom : {}".format(h1.prenom))
print("Age : {}".format(h1.age))
print("Nombre : {}".format(Humain.humaincrees))
h2 = Humain("jojo",12)
print("Prénom : {}".format(h2.prenom))
print("Age : {}".format(h2.age))
print("Nombre : {}".format(Humain.humaincrees))
//////////////////////////////////////////////////////////////////////// Les méthodes ///////////////////////////////////////////////////////////////////////

class Humain :
    lieuHabitation = "La terre"
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def parler(self,message):
        #meth standard
        print( "{} a dit : {}".format(self.nom,message))
        return message
    def ChangerPlanet(cls,planet):
        #meth de classe
        Humain.lieuHabitation = planet
    ChangerPlanet = classmethod(ChangerPlanet)
    def definition():
        print("l'humain")
    definition = staticmethod(definition)
#programme principal
h1 = Humain("cherifa",21)

print(h1.parler("hello !"))
print("planete actuelle {} ".format(Humain.lieuHabitation))
Humain.ChangerPlanet("mars")
print("planete actuelle {} ".format(Humain.lieuHabitation))
Humain.definition()
//////////////////////////////////////////////////////////////////// Propriétés d'encapsulation ////////////////////////////////////////////////////////////////

class Humain :
    classe d'un humain
    lieuHabitation = "La terre"
    def __init__(self,nom,age):
        self._nom = nom
        self._age = age
    def _getnom(self) :
        return self._nom
    def _getage(self):
        try:
            if self._age <=1:
                return "{} {}".format(self._age,"an")
            else:
                return "{} {}".format(self._age,"ans")
        except AttributeError :
            print("l'age n'existe pas")
    def _setage(self,nvage):
        if nvage < 0 :
            self.age = 0
        else : self._age = nvage
    def _delage(self):
        del self._age
    #property <getter,setter,deleter,helper>
    age = property(_getage,_setage,_delage,"je suis l'age d'un humain") 
    nom = property(_getnom)     
#programme principal
h1 = Humain("cherifa",21)
print(h1.age)
h1.age=1

print(h1.age)
help(Humain.age)
del h1.age
////////////////////////////////////////////////////////////////// Héritage /////////////////////////////////////////////////////////////////////

class Vehicule :
    def __init__(self,nom,qt_essance):
        self.nom = nom
        self.qt_essance = qt_essance
    def montrerVehicule(self):
        return self.nom
    def SeDeplacer(self):
        print("ma voiture {} se déplace".format(self.nom))
class Voiture(Vehicule):
    def __init__(self,nom,qt_essance,puissance):
        Vehicule.__init__(self,nom,qt_essance)
        self.puissance = puissance

#programme principal
v1 = Voiture("haha",12,4)
v1.SeDeplacer()
////////////////////////////////////////////////////////////// Héritage multiple /////////////////////////////////////////////////////////////////////////////////////

class Enseignant:
    pass
class Etudiant :
    pass
class Doctorant(Enseignant,Etudiant):
    pass


class Animal:
    def __init__(self,nom):
        self.nom = nom
    def manger(self):
        print(self.nom,"mange")
class Reptile(Animal):
    def __init__(self,nom,regime):
        Animal.__init__(self,nom)
        self.regime = regime
    def manger(self):
        print("Le reptile mange")
#programme principal
lezard = Reptile("lezard","grenouilles")
lezard.manger()
print(isinstance(lezard,Reptile))
print(issubclass(Reptile,Animal))
//////////////////////////////////////////////////////////////////Les chaines de caractères/////////////////////////////////////////////////////

maChaine = "bonjour tlm"
print(maChaine.upper())
print(maChaine.lower())
print(maChaine.capitalize())
print(maChaine.title())
print(maChaine.center(50,"-")) 
print(maChaine.find("tlm")) #retourne l'indice ou il l'a trouvé , -1 sinon
try:
    print(maChaine.index("-"))
except ValueError: 
    print("ow")
maChaine = "            no              "
print(maChaine.strip())
maChaine ="ababababab"
print(maChaine.replace("a","z",2))
print(maChaine)
print(maChaine.split("a"))

Tester si :
        str.islower()
        str.isnumeric()
        str.isalphanum()
        str.isidentifier() /mot résérvé/
        str.isupper()
        str.isalpha()
        str.isdigit()
        str.isdecimal()
        str.iskeyword()
        ...
ch = "langage python"
if "langage" in ch:
    print("trouvé")
else:
    print("ow")
//////////////////////////////////////////////////////////////////// Les listes ///////////////////////////////////////////////////////////////////

#Création d'une liste 
inventaire = list()
inventaire = [1,1,2,3,"voiture"]
print(inventaire[:2])
print(inventaire[2:])
print(inventaire[2:4])
print(type(inventaire))
print(inventaire)
inventaire = [0] * 10
print(inventaire)
inventaire[2] = "h&h"
print(inventaire)

inventaire[:] = ["bouclier"]*10
print(inventaire)
if "bouclier" in inventaire : print("oui")
inventaire = range(20)
print(inventaire)
i = 0
while i<len(inventaire) :
    print(inventaire[i])
    i += 1
for val in inventaire:
    print(val)
print(inventaire[2])
print(inventaire[-1]) #l'element i en partant de la fin 

ville = ["TO","Alger","Mosta"]
print(ville)
ville.append("cherifa")
print(ville)
ville.insert(2,"Blida")
print(ville)
ville.remove("Blida")
print(ville)
del ville[1]
print(ville)
print(ville.index("TO"))
ville.sort()#elements de la liste meme type
ville.reverse()
print(ville)
print(len(ville))
print(ville.count("TO"))
#help(list)

print(ville)
phrase = "-".join(ville)
print(phrase)
ville.clear() # ville[:] = []
print(ville)
import copy
#inventaire = ville inventaire ref vers ville 
inventaire = copy.deepcopy(ville)#independantes
inventaire.extend(ville)
//////////////////////////////////////////////////////////Les tuples //////////////////////////////////////////////////////////////

def getposition():
    posx = 1
    posy = 2 
    return(posx,posy)
coordx = 0
coordy = 0

print("position {} {}".format(coordx,coordy))

tuplee=(coordx,coordy)
tuplee= getposition()
print(tuplee)
////////////////////////////////////////////////////////////Les dictionnaires ///////////////////////////////////////////////////////////////////////////////////////

dico = {
    "matricule":"10",
    "nom":"hamroun",
    "prenom":"cherifa"
}
print(dico["prenom"])
dico["num"]="022224"#ajout ou modif si l'elt existe 
#val=dico.pop("num")
del dico["prenom"]
print(dico)
#print(val)
#dico = dict()
if "chien" in dico : print("ow")
else:print("aha")
for key in dico.items():#dico.keys pour les cles et dico.values pour les valeurs
    print(key)#key est un tuple ici donc tu peux etre plus précise (k,v)
#dico = dic est juste une référence c le meme or :
dico2 = dico.copy() 
dico2["sel"]="oh"
print(dico2)
print(dico)
def show_inventory(**items):#parametres nommés ;* parametres variables
        print(items)

show_inventory(mama="henia",papa="brahim")
///////////////////////////////////////////////////////////////// TKINTER //////////////////////////////////////////////////////////////////////////////

from tkinter import *
mainapp = Tk()
mainapp.title("Mon premier programme avec tkinter")
mainapp.minsize(640,480)
mainapp.maxsize(1280,720)

mainapp.geometry("600x600+350+50")
#mainapp.resizable(width=False,height=False)
#mainapp.sizefrom("user") #positionfrom
mainapp.mainloop()
////////////////////////////////////////////////////////////////////Premiers widgets////////////////////////////////////////////////////////////////////////////////

from tkinter import *
app = Tk()
app.title("Script")
app.geometry("500x500+300+50")
labelWelcome =  Label(app,text = "Bienvenu!")
print(labelWelcome["text"])
print(labelWelcome.cget("text"))
labelWelcome.pack()
app.mainloop()
"""