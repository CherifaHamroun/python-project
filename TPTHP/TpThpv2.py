#coding:utf-8
from dataclasses import dataclass
import pygame
import time
import sys
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
def draw_text(text,font,color,surface,x,y,p):
    textobj = font.render(text,p,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x+40,y+10)
    surface.blit(textobj,textrect)
def main_menu(windowSurface,font,A):
    while True :
        draw_text('Options',fonti,(255,255,255),screen,300,300,1)
        mx,my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(380,180,115,40)
        button_2 = pygame.Rect(380,230,115,40)
        button_3 = pygame.Rect(380,480,115,40)
        button_4 = pygame.Rect(380,530,115,40)
        button_5 = pygame.Rect(380,580,115,40)
        button_6 = pygame.Rect(380,630,115,40)
        pygame.draw.rect(screen,(255,255,255),button_1)
        draw_text('Réduire '+nomAut,fontmin,(0,10,20),screen,350,380,1)
        pygame.draw.rect(screen,(255,255,255),button_2)
        draw_text('Déterministe '+nomAut,fontmin,(0,10,20),screen,350,430,1)
        pygame.draw.rect(screen,(255,255,255),button_3)
        draw_text('Complément '+nomAut,fontmin,(0,10,20),screen,350,480,1)
        pygame.draw.rect(screen,(255,255,255),button_4)
        draw_text('Mirroir '+nomAut,fontmin,(0,10,20),screen,350,530,1)
        pygame.draw.rect(screen,(255,255,255),button_5)
        draw_text('Reconnaitre '+nomAut,fontmin,(0,10,20),screen,350,580,1)
        pygame.draw.rect(screen,(255,255,255),button_6)
        draw_text('Afficher '+nomAut,fontmin,(0,10,20),screen,350,630,1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(mx,my):
                    pass
                if button_5.collidepoint(mx,my):
                    pass
        pygame.display.update()
        mainClock.tick(60)
   
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # `event.pos` is the mouse position.
                if button_1.collidepoint(event.pos):
                        # Increment the number.
                    define()
                    pygame.display.flip()
        mx,my = pygame.mouse.get_pos()
        if button_1.collidepoint(mx,my):
            pygame.draw.rect(windowSurface,(255,0,0),button_1)
            draw_text('Définir un Automate',fontmin,light,windowSurface,250,70,1)
        else :
            pygame.draw.rect(windowSurface,(193,5,5),button_1)
            draw_text('Définir un Automate',fontmin,light,windowSurface,250,70,1)
        pygame.display.flip()

    input_box_1 = pygame.Rect(10, 185, 80, 32)
    color_inactive = (255,255,255)#pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    input_box_2 = pygame.Rect(170, 185, 80, 32)
    color2 = color_inactive
    active2 = False
    text2 = ''
    input_box_3 = pygame.Rect(330, 185, 80, 32)
    color3 = color_inactive
    active3 = False
    text3 = ''
    input_box_4 = pygame.Rect(490, 185, 80, 32)
    color4 = color_inactive
    active4 = False
    text4 = ''
    input_box_5 = pygame.Rect(630, 185, 150, 32)
    color5 = color_inactive
    active5 = False
    text5 = ''
    fill_gradient(screen,(114,187,250),(53,41,229))
    background_image = pygame.image.load("Capture2.PNG").convert()
    background_image = pygame.transform.scale(background_image, (900, 700))
    windowSurface.blit(background_image, [0, 0])
    buttonv = pygame.Rect(790, 185, 80, 32)
    pygame.display.flip()
    bool1 = False
    bool2 = False
    bool3 = False
    bool4 = False
    bool5 = False 
    valid = False
    i = 1
    nomAut =""
    done = False
    while not done:
        mx,my = pygame.mouse.get_pos()
        if buttonv.collidepoint(mx,my):
            pygame.draw.rect(screen, (200,200,200), buttonv)
            draw_text('Valider',fontmin,(0,10,20),screen,755,180,1)
        else :
            pygame.draw.rect(screen, (255,255,255), buttonv)
            draw_text('Valider',fontmin,(0,10,20),screen,755,180,1)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonv.collidepoint(event.pos):
                    valid = True
                # If the user clicked on the input_box rect.
                if input_box_1.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                if input_box_2.collidepoint(event.pos):
                    active2 = not active2
                else:
                    active2 = False
                if input_box_3.collidepoint(event.pos):
                    active3 = not active3
                else:
                    active3 = False
                if input_box_4.collidepoint(event.pos):
                    active4 = not active4
                else:
                    active4 = False
                if input_box_5.collidepoint(event.pos):
                    active5 = not active5
                else:
                    active5 = False
                # Change the current color of the input box.
                if active:
                    color = color_active
                    color2 = color_inactive 
                    color3 = color_inactive
                    color4 = color_inactive
                    color5 = color_inactive
                elif active2:
                    color2 = color_active 
                    color = color_inactive
                    color3 = color_inactive
                    color4 = color_inactive
                    color5 = color_inactive
                elif active3:
                    color3 = color_active
                    color = color_inactive
                    color2 = color_inactive
                    color4 = color_inactive
                    color5 = color_inactive
                elif active4:
                    color3 = color_inactive
                    color = color_inactive
                    color2 = color_inactive
                    color4 = color_active
                    color5 = color_inactive
                elif active5:
                    color3 = color_inactive
                    color = color_inactive
                    color2 = color_inactive
                    color4 = color_inactive
                    color5 = color_active
                else:
                    color2 = color_inactive
                    color = color_inactive
                    color3 = color_inactive
                    color4 = color_inactive
                    color5 = color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        bool1 = True
                        if i == 1:
                            A["nom"] = text
                            nomAut = text
                            i+=1
                        text = 'Enregistré'
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                if active2:
                    if event.key == pygame.K_RETURN:
                        bool2 = True
                        A["etatinitial"]=text2
                        text2 = 'Enregistré'
                    elif event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode
                if active3:
                    if event.key == pygame.K_RETURN:
                        bool3 = True
                        A["etats"].append(text3)
                        print(A["etats"])
                        text3 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text3 = text3[:-1]
                    else:
                        text3 += event.unicode
                if active4:
                    if event.key == pygame.K_RETURN:
                        bool4 = True
                        A["etatsfinaux"].append(text4)
                        print(A["etats"])
                        text4 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text4 = text4[:-1]
                    else:
                        text4 += event.unicode
                if active5:
                    if event.key == pygame.K_RETURN:
                        bool5 = True
                        A["tbltransition"].append(text5)
                        print(A["tbltransition"])
                        text5 = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text5 = text5[:-1]
                    else:
                        text5 += event.unicode
        background_image = pygame.image.load("Capture2.PNG").convert()
        background_image = pygame.transform.scale(background_image, (900, 700))
        windowSurface.blit(background_image, [0, 0])
        # Render the current text.
        txt_surface = inputfont.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(80, txt_surface.get_width()+10)
        input_box_1.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box_1.x+5, input_box_1.y+5))
        # Blit the input_box_1 rect.
        pygame.draw.rect(screen, color, input_box_1, 2)
        draw_text('Environnement',font,(255,255,255),windowSurface,150,10,5)
        draw_text('Nom Automate',fontmin,(255,255,255),windowSurface,-30,150,1)
        # Render the current text.
        txt_surface2 = inputfont.render(text2, True, color2)
        # Resize the box if the text is too long.
        width2 = max(80, txt_surface2.get_width()+10)
        input_box_2.w = width2
        # Blit the text.
        screen.blit(txt_surface2, (input_box_2.x+5, input_box_2.y+5))
        # Blit the input_box_1 rect.
        pygame.draw.rect(screen, color2, input_box_2, 2)
        draw_text('Etat initial',fontmin,(255,255,255),windowSurface,130,150,1)
        txt_surface3 = inputfont.render(text3, True, color3)
        # Resize the box if the text is too long.
        width3 = max(80, txt_surface3.get_width()+10)
        input_box_3.w = width3
        # Blit the text.
        screen.blit(txt_surface3, (input_box_3.x+5, input_box_3.y+5))
        # Blit the input_box_1 rect.
        pygame.draw.rect(screen, color3, input_box_3, 2)
        draw_text('Etats',fontmin,(255,255,255),windowSurface,290,150,1)
        txt_surface4 = inputfont.render(text4, True, color4)
        # Resize the box if the text is too long.
        width4 = max(80, txt_surface4.get_width()+10)
        input_box_4.w = width4
        # Blit the text.
        screen.blit(txt_surface4, (input_box_4.x+5, input_box_4.y+5))
        # Blit the input_box_1 rect.
        pygame.draw.rect(screen, color4, input_box_4, 2)
        draw_text('Etats finaux',fontmin,(255,255,255),windowSurface,450,150,1)
        txt_surface5 = inputfont.render(text5, True, color5)
        # Resize the box if the text is too long.
        width5 = max(150, txt_surface5.get_width()+10)
        input_box_5.w = width5
        # Blit the text.
        screen.blit(txt_surface5, (input_box_5.x+5, input_box_5.y+5))
        # Blit the input_box_1 rect.
        pygame.draw.rect(screen, color5, input_box_5, 2)
        draw_text('Transitions',fontmin,(255,255,255),windowSurface,590,150,1)
        pygame.draw.rect(screen, (255,255,255), buttonv)
        draw_text('Valider',fontmin,(0,10,20),screen,755,180,1)
        auth_surface = inputfont.render(nomAut, True, (0,10,20))
        if bool1 and bool2 and bool3 and bool4 and bool5 and valid:




            button_0 = pygame.Rect(190,60,340,460)
button_1 = pygame.Rect(200,70,320,50)
button_2 = pygame.Rect(200,130,100,100)
button_3 = pygame.Rect(200,240,100,100)
button_4 = pygame.Rect(200,350,100,100)
button_5 = pygame.Rect(310,130,100,100)
button_6 = pygame.Rect(310,240,100,100)
button_7 = pygame.Rect(310,350,100,100)
button_8 = pygame.Rect(420,130,100,100)
button_9 = pygame.Rect(420,240,100,100)
button_10 = pygame.Rect(420,350,100,100)
button_11 = pygame.Rect(200,460,320,50)
pygame.draw.rect(windowSurface,(0,10,40),button_0)
pygame.draw.rect(windowSurface,(193,5,5),button_1)
draw_text("Définir un Automate" ,fontmin,white,windowSurface,250,70,1)
pygame.draw.rect(windowSurface,(0,10,20),button_2)
draw_text('{a,b}',fontmin,light,windowSurface,190,150,1)
pygame.draw.rect(windowSurface,(0,10,20),button_3)
pygame.draw.rect(windowSurface,(0,10,20),button_4)
draw_text('{ Sfi }',fontmin,light,windowSurface,190,360,1)
pygame.draw.rect(windowSurface,(0,10,20),button_5)
pygame.draw.rect(windowSurface,(0,10,20),button_6)
draw_text('{ Si }',fontmin,light,windowSurface,290,260,1)
pygame.draw.rect(windowSurface,(0,10,20),button_7)
pygame.draw.rect(windowSurface,(0,10,20),button_8)
draw_text('{ So }',fontmin,light,windowSurface,410,150,1)
pygame.draw.rect(windowSurface,(0,10,20),button_9)
pygame.draw.rect(windowSurface,(0,10,20),button_10)
draw_text('{ (Si,a,Sj) }',fontmin,light,windowSurface,390,360,1)
draw_text('{ (Si,b,Sj) }',fontmin,light,windowSurface,390,380,1)
pygame.draw.rect(windowSurface,(0,10,40),button_11)
draw_text("Exemple d'environnement Automate",fontmin,light,windowSurface,190,460,1)
done = False
pygame.display.flip()