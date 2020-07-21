#coding:utf-8
from dataclasses import dataclass

@dataclass 
class transition:
 edep: str
 mot:  str
 earv: str
 
 
 
@dataclass 
class Element:
 dep: []
 l:  str
 arv: []
 
 
 	
 	
t0=transition('so','a','s1')
t1 = transition('s1','b','sf')
t2=transition('s1','c','s1')
t3=transition('so','c','so')
t4=transition('so','b','sf')
t5=transition('s1','d','so')
t6=transition('sf','d','s2')
etats=['so','s1','sf','s2']
alphbt=['a','b','c','d']
etatsfn=['sf']
tbltrs=[t0,t1,t2,t3,t4,t5,t6]
etato='so'
Automate = {} 



Automate["Alphabet"]=alphbt
Automate["etatinitial"]=etato
Automate["etats"]=etats
Automate["etatsfinaux"]=etatsfn
Automate["tbltransition"]=tbltrs
import copy
def es_final(s):
	result=False
	for  etat in etatsfn:
		if s==etat:
			result=True
	return result;
	
		
def complement(A):
	finaux=[]
	init='soo'
	for etat in A["etats"]:
		if es_final(s=etat)==False:
			finaux.append(etat)
	Abar={}
	Abar["Alphabet"]=A["Alphabet"]
	Abar["etatinitial"]='soo'
	Abar["etats"]=A["etats"]	
	Abar["etats"].append('soo')
	Abar["etatsfinaux"]=finaux
	Abar["tbltransition"]=A["tbltransition"]
	t=transition('soo','£',A["etatinitial"])
	Abar["tbltransition"].append(t)	
	return Abar;
	
def Miroir(A):
	print('im in')
	AR={}
	AR["tbltransition"]=[]
	AR["Alphabet"]=A["Alphabet"]
	AR["etats"]=A["etats"]
	AR["etats"].append('sm')
	AR["etatinitial"]='sm'
	AR["etatsfinaux"]=A["etatinitial"]
	for etat in A["etats"]:
		if es_final(s=etat)==True:
			t=transition('sm','£',etat)
			AR["tbltransition"].append(t)
	for tra in A["tbltransition"]:
		tt=transition(tra.earv,tra.mot,tra.edep)
		AR["tbltransition"].append(tt)
	return AR;
	
def redondance(L,Element):
	res=False
	for l in L:
		if l.dep==Element.arv:
			res=True
	return res;
def existe(elt,list):
	res=False
	for i in list:
		if i==elt:
			res=True
	return res;
	
def Deterministe(A):
	L=[]
	M=[]
	F=[]
	ad=False
	prem=[]
	prem.append(A["etatinitial"])
	element=Element(prem,'',[])
	L.append(element)
	
	j=0
	while  j<(len(L)):
		elt=L[j]
		for n in A["Alphabet"]:
			for  etat in elt.dep:
				for t in A["tbltransition"]:
					if (t.mot==n)&(etat==t.edep):
						if existe(t.earv,elt.arv)==False:
							elt.arv.append(t.earv)
						elt.l=n
						ad=True
						if existe(etat,elt.dep)==False:
							elt.dep.append(etat)
			if ad==True:		
				F.append(elt)
			ad=False
			elt=Element(elt.dep,'',[])
			
		for f in F:
			if f.l!='':
				M.append(f)
			if (redondance(L=L,Element=f)==False)&(f.l!=''):
				eltt=Element([],'',[])
				eltt.dep=f.arv
				L.append(eltt)
				F=[]
		j+=1
	AD={}

	AD["Alphabet"]=A["Alphabet"]
	AD["etatinitial"]=A["etatinitial"]
	AD["etats"]=[]
	AD["etatsfinaux"]=[]
	AD["tbltransition"]=[]
	
	

	for e in M:
		debut=''
		fin=''
		ff=False
		fff=False
		for etat in e.dep:
			
			for etf in A["etatsfinaux"]:
				if etat==etf:
					ff=True
			debut=debut+etat
		
		for etat in e.arv:
			
			for etf in A["etatsfinaux"]:
				if etat==etf:
					fff=True
			fin=fin+etat
		if existe(debut,AD["etats"])==False:
			AD["etats"].append(debut)
		if existe(fin,AD["etats"])==False:
			AD["etats"].append(fin)
		t=transition(debut,e.l,fin)
		AD["tbltransition"].append(t)
		if (ff==True)&(existe(debut,AD["etatsfinaux"])==False):
			AD["etatsfinaux"].append(debut)
		if (fff==True)&(existe(fin,AD["etatsfinaux"])==False):
			AD["etatsfinaux"].append(fin)
	return AD;
def Accessible(A):
	Aacc={}
	Aacc["Alphabet"]=A["Alphabet"]
	Aacc["etatinitial"]=A["etatinitial"]
	Aacc["etats"]=[]
	Aacc["etatsfinaux"]=[]
	Aacc["tbltransition"] = []
	s0 = A["etatinitial"]
	listetransitions = []
	for transition in A["tbltransition"]:
		if transition.edep == s0:
			listetransitions.append(transition)
	for trans in listetransitions:
		for transi in A["tbltransition"]:
			if trans.earv== transi.edep and transi not in listetransitions:
				listetransitions.append(transi)
	Aacc["tbltransition"] = listetransitions
	listeetats=[]
	listeetatsfinaux= []
	for tr in listetransitions:
		if tr.edep not in listeetats:
			listeetats.append(tr.edep)
		if tr.edep not in listeetatsfinaux and tr.edep in A['etatsfinaux']:
			listeetatsfinaux.append(tr.edep)
		if tr.earv not in listeetats :
			listeetats.append(tr.earv)
		if tr.earv not in listeetatsfinaux and tr.earv in A['etatsfinaux']:
			listeetatsfinaux.append(tr.earv)
	Aacc["etats"]=listeetats
	Aacc["etatsfinaux"]=listeetatsfinaux	
	return Aacc

def coAccessible(A):
	coAacc={}
	coAacc["Alphabet"]=A["Alphabet"]
	coAacc["etatinitial"]=A["etatinitial"]
	coAacc["etats"]=[]
	coAacc["etatsfinaux"]=[]
	coAacc["tbltransition"] = []
	sf = A["etatsfinaux"]
	listetransitions = []
	for transition in A["tbltransition"]:
		if transition.earv in sf:
			listetransitions.append(transition)
	for trans in listetransitions:
		for transi in A["tbltransition"]:
			if transi.earv== trans.edep and transi not in listetransitions:
				listetransitions.append(transi)
	coAacc["tbltransition"] = listetransitions
	listeetats=[]
	listeetatsfinaux= []
	for tr in listetransitions:
		if tr.edep not in listeetats:
			listeetats.append(tr.edep)
		if tr.edep not in listeetatsfinaux and tr.edep in A['etatsfinaux']:
			listeetatsfinaux.append(tr.edep)
		if tr.earv not in listeetats :
			listeetats.append(tr.earv)
		if tr.earv not in listeetatsfinaux and tr.earv in A['etatsfinaux']:
			listeetatsfinaux.append(tr.earv)
	coAacc["etats"]=listeetats
	coAacc["etatsfinaux"]=listeetatsfinaux
	
	return coAacc
def Reductible(A):
	Ared={}
	Ared["Alphabet"]=A["Alphabet"]
	Ared["etatinitial"]=A["etatinitial"]
	Ared['etats']=[]
	Ared["etatsfinaux"]=[]
	Aacc = Accessible(A)
	coAacc = coAccessible(A)
	listeetats = []
	listeetatsfinaux = []
	listetrans = []
	for it in coAacc["etats"]:
		if it in Aacc["etats"]:
			listeetats.append(it)
	for item in coAacc["etatsfinaux"]:
		if item in Aacc["etatsfinaux"]:
			listeetatsfinaux.append(item)
	for i in coAacc["tbltransition"]:
		if i in Aacc["tbltransition"]:
			listetrans.append(i)
	Ared["etats"] = listeetats
	Ared["etatsfinaux"] = listeetatsfinaux
	Ared["tbltransition"] = listetrans
	return Ared
def Reconnaissance(A,mot):
    init = A["etatinitial"]
    trans = transition('','','')
    for lettre in mot :
        for elt in A["tbltransition"]:
            if init == elt.edep and elt.mot == lettre :
                trans = copy.deepcopy(elt)
                init = elt.earv
    if trans.earv in A["etatsfinaux"]:
            print("done")
    else: print("not done")
print(Reductible(Automate))

