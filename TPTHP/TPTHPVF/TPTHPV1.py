#coding:utf-8
from dataclasses import dataclass
import sys
import copy
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" Automate section """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
etats=['so','s1','sf']
alphbt=['a','b','c','d']
etatsfn=['sf']
tbltrs=[t0,t1,t2,t3,t4,t5]
etato='so'
Automate = {} 



Automate["Alphabet"]=alphbt
Automate["etatinitial"]=etato
Automate["etats"]=etats
Automate["etatsfinaux"]=etatsfn
Automate["tbltransition"]=tbltrs
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
	
def Reconnaissance(A,mot):
    init = A["etatinitial"]
    trans = transition('','','')
    for lettre in mot :
        for elt in A["tbltransition"]:
            if init == elt.edep and elt.mot == lettre :
                trans = copy.deepcopy(elt)
                init = elt.earv
    if trans.earv in A["etatsfinaux"]:
            return True
    else: return False

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
import pygame
import time
def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))
mainClock = pygame.time.Clock()
pygame.init()
windowResolution = (740,580)
pygame.display.set_caption("Automate")
background = (30,30,70)
white = (255,255,255)
light = (170,170,170)
windowSurface = pygame.display.set_mode(windowResolution)
fill_gradient(windowSurface,(114,187,250),(53,41,229))
background_image = pygame.image.load("Capture2.PNG").convert()
background_image = pygame.transform.scale(background_image, (740, 580))
windowSurface.blit(background_image, [0, 0])
arialFont = pygame.font.SysFont("arial",32,True,True)
arialFont2 = pygame.font.SysFont("arial",15,True,True)
font = pygame.font.Font("Street Photography.otf",80)
fonti = pygame.font.Font("Street Photography.otf",32)
blue = (0,75,255)
grey = (50,50,50)
Green = (100,200,50)
Aut = font.render("Automate",True,white)
TP = arialFont.render("TP THP",True,white)
windowSurface.blit(Aut,[200,150])
windowSurface.blit(TP,[280,270])
blackcolor= (0,0,0)
myrect = pygame.Rect(200,320,20,25)
pygame.draw.rect(windowSurface,white,myrect)
pygame.display.flip()

i=0
while i<30:
    load = arialFont2.render(" Loading ...",False,(0,10,20))
    windowSurface.blit(load,[300,320])
    time.sleep(.050)
    myrect.x +=10
    pygame.draw.rect(windowSurface,white,myrect)
    i +=1
    pygame.display.flip()
fill_gradient(windowSurface,(114,187,250),(53,41,229))
background_image = pygame.image.load("Capture2.PNG").convert()
background_image = pygame.transform.scale(background_image, (740, 580))
windowSurface.blit(background_image, [0, 0])
pygame.display.flip()
fontmin = pygame.font.SysFont("arial",20,False,False)


def draw_text(text,font,color,surface,x,y,p):
    textobj = font.render(text,p,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x+40,y+10)
    surface.blit(textobj,textrect)
def define(A):
    screen = pygame.display.set_mode((900,700))
    background_image = pygame.image.load("Capture2.PNG").convert()
    background_image = pygame.transform.scale(background_image, (900, 700))
    screen.blit(background_image, [0, 0])
    inputfont = pygame.font.Font(None, 25)
    clock = pygame.time.Clock()
    draw_text('Options',fonti,(255,255,255),screen,350,110,1)
    done = False
    while not done:
        mx,my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(380,180,115,40)
        button_2 = pygame.Rect(380,230,115,40)
        button_3 = pygame.Rect(380,280,115,40)
        button_4 = pygame.Rect(380,330,115,40)
        button_5 = pygame.Rect(380,380,115,40)
        button_6 = pygame.Rect(380,430,115,40)
        pygame.draw.rect(screen,(255,255,255),button_1)
        draw_text('Réduire ',fontmin,(0,10,20),screen,350,180,1)
        pygame.draw.rect(screen,(255,255,255),button_2)
        draw_text('Déterministe ',fontmin,(0,10,20),screen,350,230,1)
        pygame.draw.rect(screen,(255,255,255),button_3)
        draw_text('Complément ',fontmin,(0,10,20),screen,350,280,1)
        pygame.draw.rect(screen,(255,255,255),button_4)
        draw_text('Mirroir ',fontmin,(0,10,20),screen,350,330,1)
        pygame.draw.rect(screen,(255,255,255),button_5)
        draw_text('Reconnaitre ',fontmin,(0,10,20),screen,350,380,1)
        pygame.draw.rect(screen,(255,255,255),button_6)
        draw_text('Afficher ',fontmin,(0,10,20),screen,350,430,1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(mx,my):
                    launched = True
                    while launched:
                        Reductible(A)
                        afficherauth(A)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_2.collidepoint(mx,my):
                    launched = True
                    while launched:
                        Deterministe(A)
                        afficherauth(A)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_3.collidepoint(mx,my):
                    launched = True
                    while launched:
                        complement(A)
                        afficherauth(A)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_4.collidepoint(mx,my):
                    launched = True
                    while launched:
                        Miroir(A)
                        afficherauth(A)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_5.collidepoint(mx,my):
                    mot = ''
                    color_inactive = (255,255,255)#pygame.Color('lightskyblue3')
                    color_active = pygame.Color('dodgerblue2')
                    input_box = pygame.Rect(500,390, 150, 32)
                    color = color_inactive
                    active = False
                    text = ''
                    done = False
                    while not done:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                done = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if input_box.collidepoint(event.pos):
                                    # Toggle the active variable.
                                    active = not active
                                else:
                                    active = False
                                if active:
                                    color = color_active
                                else : color = color_inactive
                            if event.type == pygame.KEYDOWN:
                                if active:
                                    if event.key == pygame.K_RETURN:
                                        mot = text
                                        if Reconnaissance(Automate,mot):
                                            text ="Reconnu"
                                            pygame.display.flip()
                                            done = True
                                            
                                        else:
                                            text = "Non Reconnu"
                                            pygame.display.flip()
                                            done = True
                                            
                                    elif event.key == pygame.K_BACKSPACE:
                                        text = text[:-1]
                                    else:
                                        text += event.unicode
                        background_image = pygame.image.load("Capture2.PNG").convert()
                        background_image = pygame.transform.scale(background_image, (900, 700))
                        windowSurface.blit(background_image, [0, 0])
                        draw_text('Options',fonti,(255,255,255),screen,350,110,1)
                        pygame.draw.rect(screen,(255,255,255),button_1)
                        draw_text('Réduire ',fontmin,(0,10,20),screen,350,180,1)
                        pygame.draw.rect(screen,(255,255,255),button_2)
                        draw_text('Déterministe ',fontmin,(0,10,20),screen,350,230,1)
                        pygame.draw.rect(screen,(255,255,255),button_3)
                        draw_text('Complément ',fontmin,(0,10,20),screen,350,280,1)
                        pygame.draw.rect(screen,(255,255,255),button_4)
                        draw_text('Mirroir ',fontmin,(0,10,20),screen,350,330,1)
                        pygame.draw.rect(screen,(255,255,255),button_5)
                        draw_text('Reconnaitre ',fontmin,(0,10,20),screen,350,380,1)
                        pygame.draw.rect(screen,(255,255,255),button_6)
                        draw_text('Afficher ',fontmin,(0,10,20),screen,350,430,1)
                        # Render the current text.
                        txt_surface = inputfont.render(text, True, color)
                        # Resize the box if the text is too long.
                        width = max(80, txt_surface.get_width()+10)
                        input_box.w = width
                        # Blit the text.
                        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                        # Blit the input_box_1 rect.
                        pygame.draw.rect(screen, color, input_box, 2)
                        pygame.display.flip()
                        
                    

                    
                if button_6.collidepoint(mx,my):
                    launched = True
                    while launched:
                        afficherauth(A)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                    # 1 is the left mouse button, 2 is middle, 3 is right.
                                if event.button == 1:
                                    # `event.pos` is the mouse position.
                                    if button_1.collidepoint(event.pos):
                                            # Increment the number.
                                        pass
                                        pygame.display.flip()
                            pygame.display.flip()
            done = True
    pygame.display.flip()
    clock.tick(30)
def afficherauth(Automate):
    i1 = 0
    i2= 0
    i3 = 0
    
    newscreen = pygame.display.set_mode((900,700))
    background_image = pygame.image.load("Capture2.PNG").convert()
    background_image = pygame.transform.scale(background_image, (900, 700))
    newscreen.blit(background_image, [0, 0])
    draw_text('Etat initial',fontmin,(255,255,255),newscreen,130,150,1)
    draw_text('Etats',fontmin,(255,255,255),newscreen,290,150,1)
    draw_text('Etats finaux',fontmin,(255,255,255),newscreen,450,150,1)
    draw_text('Transitions',fontmin,(255,255,255),newscreen,590,150,1)
    init_surface = fontmin.render(Automate["etatinitial"], True, (0,10,20))
    button_init = pygame.Rect(170,200,50+init_surface.get_width(),30)
    pygame.draw.rect(newscreen,(0,10,40),button_init)
    draw_text(Automate["etatinitial"],fontmin,(255,255,255),newscreen,150,190,1)
    for etat in Automate["etats"]:
        etat_surface = fontmin.render(etat, True, (0,10,20))
        button_etat = pygame.Rect(330,200+i1,50+etat_surface.get_width(),30)
        pygame.draw.rect(newscreen,(0,10,40),button_etat)
        draw_text(etat,fontmin,(255,255,255),newscreen,310,190+i1,1)
        i1+=40
    for etatfinal in Automate["etatsfinaux"]:
        etatfinal_surface = fontmin.render(etatfinal, True, (0,10,20))
        button_etatfinal = pygame.Rect(490,200+i2,50+etatfinal_surface.get_width(),30)#630
        pygame.draw.rect(newscreen,(0,10,40),button_etatfinal)
        draw_text(etatfinal,fontmin,(255,255,255),newscreen,310,190+i2,1)
        i2+=40
    for trans in Automate["tbltransition"]:
        trans_surface = fontmin.render(trans.edep+','+trans.mot+','+trans.earv, True, (0,10,20))
        button_trans = pygame.Rect(630,200+i3,50+trans_surface.get_width(),30)#630
        pygame.draw.rect(newscreen,(0,10,40),button_trans)
        draw_text(trans.edep+','+trans.mot+','+trans.earv,fontmin,(255,255,255),newscreen,310,190+i3,1)
        i3+=40
    tab = pygame.Rect(0,190,850,max(i1,i2,i3)+10)
    pygame.draw.rect(newscreen,(0,10,20),tab)
    i1 = 0
    i2= 0
    i3 = 0
    init_surface = fontmin.render(Automate["etatinitial"], True, (0,10,20))
    button_init = pygame.Rect(170,200,50+init_surface.get_width(),30)
    pygame.draw.rect(newscreen,(0,10,40),button_init)
    draw_text(Automate["etatinitial"],fontmin,(255,255,255),newscreen,150,190,1)
    for etat in Automate["etats"]:
        etat_surface = fontmin.render(etat, True, (0,10,20))
        button_etat = pygame.Rect(330,200+i1,50+etat_surface.get_width(),30)
        pygame.draw.rect(newscreen,(0,10,40),button_etat)
        draw_text(etat,fontmin,(255,255,255),newscreen,310,190+i1,1)
        i1+=40
    for etatfinal in Automate["etatsfinaux"]:
        etatfinal_surface = fontmin.render(etatfinal, True, (0,10,20))
        button_etatfinal = pygame.Rect(490,200+i2,50+etatfinal_surface.get_width(),30)#630
        pygame.draw.rect(newscreen,(0,10,40),button_etatfinal)
        draw_text(etatfinal,fontmin,(255,255,255),newscreen,470,190+i2,1)
        i2+=40
    for trans in Automate["tbltransition"]:
        trans_surface = fontmin.render(trans.edep+','+trans.mot+','+trans.earv, True, (0,10,20))
        button_trans = pygame.Rect(630,200+i3,50+trans_surface.get_width(),30)#630
        pygame.draw.rect(newscreen,(0,10,40),button_trans)
        draw_text(trans.edep+','+trans.mot+','+trans.earv,fontmin,(255,255,255),newscreen,620,190+i3,1)
        i3+=40
    pygame.display.flip()


launched = True
while launched:
    define(Automate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # `event.pos` is the mouse position.
                if button_1.collidepoint(event.pos):
                        # Increment the number.
                    pass
                    pygame.display.flip()
        pygame.display.flip()

