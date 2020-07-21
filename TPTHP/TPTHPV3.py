#coding:utf-8
from dataclasses import dataclass
import sys
import copy
import math
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
 ######################################################var global##################################
counter=0
counteri=0
counterf=0
 ###################################################################################################
 	
 	
##t0=transition('so','a','s1')
##t1 = transition('s1','b','sf')
##t2=transition('s1','c','s1')
##t3=transition('so','c','so')
##t4=transition('so','b','sf')
##t5=transition('s1','d','so')
##etats=['so','s1','sf']
##alphbt=['a','b','c','d']
##etatsfn=['sf']
##tbltrs=[t0,t1,t2,t3,t4,t5]
##etato='so'
Automate = {} 



Automate["Alphabet"]=[]
Automate["etatinitial"]=[]
Automate["etats"]=[]
Automate["etatsfinaux"]=[]
Automate["tbltransition"]=[]
def es_final(Automate,s):
	result=False
	for  etat in Automate["etatsfinaux"]:
		if s==etat:
			result=True
	return result;
	
		
def complement(A):
	finaux=[]
	init='soo'
	for etat in A["etats"]:
		if es_final(Automate=A,s=etat)==False:
			finaux.append(etat)
	Abar={}
	Abar["Alphabet"]=A["Alphabet"]
	Abar["etatinitial"]=A["etatinitial"]
	Abar["etats"]=A["etats"]	
	#Abar["etats"].append('soo')
	Abar["etatsfinaux"]=finaux
	#Abar["etatsfinaux"].append(A["etatinitial"])
	Abar["tbltransition"]=A["tbltransition"]
	#t=transition('soo','£',A["etatinitial"])
	#Abar["tbltransition"].append(t)	
	return Abar;
	
def Miroir(A):
    finaux=[]
    
	
    AR={}
    AR["etatinitial"]=[]
        
    for etat in A["etatinitial"]:
        finaux.append(etat)
    init=A["etatinitial"]
    AR["tbltransition"]=[]
    AR["Alphabet"]=A["Alphabet"]
    AR["etats"]=A["etats"]
    
    AR["etatinitial"].append('sm')
    AR["etatsfinaux"]=finaux
    for etat in A["etats"]:
        if es_final(Automate=A,s=etat)==True:
            t=transition('sm','£',etat)
            AR["tbltransition"].append(t)
    for tra in A["tbltransition"]:
        tt=transition(tra.earv,tra.mot,tra.edep)
        AR["tbltransition"].append(tt)
    #AR["etats"].append('sm')
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
    init = A["etatinitial"][0]
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
	s0 = A["etatinitial"][0]
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
	prem.append(A["etatinitial"][0])
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
	print("ACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
	print(Aacc)
	print("coooooooooooooooooooooooooooACCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
	print(coAacc)
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
import sys
 

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
background = (105,105,105)
white = (255,255,255)
light = (170,170,170)
windowSurface = pygame.display.set_mode(windowResolution)
################################################My Code###############################################################################################

white=(255,255,255)
font=(114,153,183)
pink=(233,144,144)
black=(47,9,9)
light_pink=(232,165,165)
COLOR_INACTIVE=light
COLOR_ACTIVE=light
FONT = pygame.font.Font(None,20)
font_40 = pygame.font.Font(None, 40)
                        ################################textbox s ###################################################
class InputBoxs:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font_40.render(text, True, self.color)
        self.active = False
        self.var=False

    def handle_event(self, event):
        gooo=False
        tr=''
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("down")
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                #print("collide")
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            #print("keydown")
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print("enter")
                    print(self.text)
                    tr=self.text
                    self.text = ""
                    self.var=True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    #print("unicode")
                # Re-render the text.
                if self.var==False:
                    #print("yooooo esleee")
                    self.txt_surface = font_40.render(self.text, True, blackcolor)
                    windowSurface.blit(self.txt_surface, (self.rect.x, self.rect.y))
                    pygame.display.flip()
                    
                else:
                    #print("vqrrqrrrrrr")
                    
                    r=pygame.draw.rect(windowSurface, self.color, self.rect, 2)
                    s = pygame.display.get_surface()
                    s.fill(white, r)
                    
        gooo=self.var
        self.var=False       
        return tr,gooo

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        r=pygame.draw.rect(screen, self.color, self.rect, 2)
        s = pygame.display.get_surface()
        s.fill(white, r)
        ##################################################textbox###############################################################

class InputBox:

    def __init__(self, x, y, w, h,a, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.alpha=a
        

    def handle_event(self, event):
        outside=True
        rett=''
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print('event.mousebuttondown')
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                #print('self.rect.collidepoint(event.pos)')
                # Toggle the active variable.
                self.active = not self.active
            else:
                #print("I got the else")
                self.active = False
            # Change the current color of the input box.
            self.color = black if self.active else COLOR_INACTIVE
        #print(self.active)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.alpha:
                        rett=self.text
                        #print("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffa")
                        self.text = ''
                    outside=False
                    
                elif event.key == pygame.K_BACKSPACE:
                    #print('event.key.k_backspace')
                    self.text = self.text[:-1]
                else:
                    #print("codeeeeeeeeeuni")
                    self.text += event.unicode
                # Re-render the text.
                #print("self.text")
                #print(self.text)
                if self.text=='':
                    #print("plintttttttttttttttttttt")
                    self.txt_surface = FONT.render("", True, self.color)
                else:
                    self.txt_surface = FONT.render(self.text, True, self.color)
                windowSurface.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
                pygame.display.flip()
        #print('rerender')
        #print(rett)
        return self.text,outside
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        r=pygame.draw.rect(screen, self.color, self.rect, 2)
        s = pygame.display.get_surface()
        s.fill(white, r)
              ###################################################################################################


def in_range(x,y,w,h):
    ins=False
    mouse=pygame.mouse.get_pos()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        ins=True         
    return ins;
    
def text_objects(text,font):
    textSurface=font.render(text,True,blackcolor)
    return textSurface,textSurface.get_rect();
def adding_text(text,x,y,w,h):
    font = pygame.font.SysFont("comicsansms", 30)
    text_ajouter,supp =text_objects(text,font)
    supp.center=(int(x+(w/2)),int(y+(h/2)))
    windowSurface.blit(text_ajouter,supp)

def move_state(x,y,w,h,event):
    drag=False
    mouse=pygame.mouse.get_pos()
    i=0
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        if event.type==pygame.MOUSEBUTTONDOWN:
            drag=True
               
    return drag;
    

def generate_click(xpos,ypos,width,height,event):
    global counter
    mouse=pygame.mouse.get_pos()
    text=''
    x_etat=150
    y_etat=60
    w_etat=70
    h_etat=40
    if xpos+width>mouse[0]>xpos and ypos+height>mouse[1]>ypos:
        pygame.draw.rect(windowSurface,light,[xpos,ypos,width,height])

        if event.type==pygame.MOUSEBUTTONUP :
            text='s'+str(counter)
            counter+=1
            x_etat=150
            y_etat=60
            w_etat=70
            h_etat=40
            pygame.draw.ellipse(windowSurface,white,[x_etat,y_etat,w_etat,h_etat])
            adding_text(text,x_etat,y_etat,w_etat,h_etat)
            pygame.display.update()

    else:
        pygame.draw.rect(windowSurface,background ,[xpos,ypos,width,height])
    return x_etat,y_etat,w_etat,h_etat,text;


def initial(xpos,ypos,width,height,event):
    global counteri
    mouse=pygame.mouse.get_pos()
    text=''
    x_etat=150
    y_etat=60
    w_etat=70
    h_etat=40
    if xpos+width>mouse[0]>xpos and ypos+height>mouse[1]>ypos:
        pygame.draw.rect(windowSurface,light,[xpos,ypos,width,height])

        if event.type==pygame.MOUSEBUTTONUP :
            text='si'+str(counteri)
            counteri+=1
            x_etat=150
            y_etat=60
            w_etat=70
            h_etat=40
            pygame.draw.ellipse(windowSurface,white,[x_etat,y_etat,w_etat,h_etat])
            adding_text(text,x_etat,y_etat,w_etat,h_etat)
            pygame.display.update()

    else:
        pygame.draw.rect(windowSurface,light,[xpos,ypos,width,height])
       
        
         
    return x_etat,y_etat,w_etat,h_etat,text;
def final(xpos,ypos,width,height,event):
    global counterf
    mouse=pygame.mouse.get_pos()
    text=''
    x_etat=150
    y_etat=60
    w_etat=70
    h_etat=40
    if xpos+width>mouse[0]>xpos and ypos+height>mouse[1]>ypos:
        pygame.draw.rect(windowSurface,light,[xpos,ypos,width,height])

        if event.type==pygame.MOUSEBUTTONUP :
            text='sf'+str(counterf)
            counterf+=1
            x_etat=150
            y_etat=60
            w_etat=70
            h_etat=40
            pygame.draw.ellipse(windowSurface,white,[x_etat,y_etat,w_etat,h_etat])
            adding_text(text,x_etat,y_etat,w_etat,h_etat)
            pygame.display.update()

    else:
        pygame.draw.rect(windowSurface,background ,[xpos,ypos,width,height])
       
        
         
    return x_etat,y_etat,w_etat,h_etat,text;

def button(x,y,w,h,text):
    mouse=pygame.mouse.get_pos()
    pygame.draw.rect(windowSurface,background ,[x,y,w,h])
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(windowSurface,light,[x,y,w,h])
    else:
        pygame.draw.rect(windowSurface,background ,[x,y,w,h])
    font = pygame.font.SysFont("comicsansms", 15)
    text_ajouter,supp =text_objects(text,fontii)
    supp.center=(int(x+(w/2)),int(y+(h/2)))
    windowSurface.blit(text_ajouter,supp)
    pygame.display.update()
def generate_trans(event,mouse):
    x=10
    y=80
    w=100
    h=50
    trans=False
    mouse=pygame.mouse.get_pos()
    if x+w>mouse[0]>x and y+h>mouse[1]>y and event.type==pygame.MOUSEBUTTONUP:
        trans=True
    return trans;
def image_transition(x,y):
    arrow=pygame.image.load('15480059.jpg')
    windowResolution.blit(arrow,(x,y))



def arrow(screen, lcolor, tricolor, start, end, trirad, thickness):
    rad=math.pi/180
    pygame.draw.line(screen,lcolor, start, end,thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    pygame.draw.polygon(screen, tricolor, ((end[0] + trirad * math.sin(rotation),
                                        end[1] + trirad * math.cos(rotation)),
                                       (end[0] + trirad * math.sin(rotation - 120*rad),
                                        end[1] + trirad * math.cos(rotation - 120*rad)),
                                       (end[0] + trirad * math.sin(rotation + 120*rad),
                                        end[1] + trirad * math.cos(rotation + 120*rad))))


class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font(None, 50)
    self.image = self.font.render("Enter your name", False, [0, 0, 0])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [0, 0, 0])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos





######################################################################################################################################################
fill_gradient(windowSurface,(114,187,250),(53,41,229))
background_image = pygame.image.load("Capture2.PNG").convert()
background_image = pygame.transform.scale(background_image, (740, 580))
windowSurface.blit(background_image, [0, 0])
arialFont = pygame.font.SysFont("arial",32,True,True)
arialFont2 = pygame.font.SysFont("arial",15,True,True)
font = pygame.font.Font("Street Photography.otf",80)
fonti = pygame.font.Font("Street Photography.otf",32)
fontii = pygame.font.Font("Street Photography.otf",15)
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
    screen = pygame.display.set_mode((740,580))
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
                        Qred=Reductible(A)
                        
                        afficherauth(Qred)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_2.collidepoint(mx,my):
                    launched = True
                    while launched:
                        Qdd=Deterministe(A)
                       
                        afficherauth(Qdd)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_3.collidepoint(mx,my):
                    launched = True
                    while launched:
                        Qbar=complement(A)
                        afficherauth(Qbar)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                launched=False
                            pygame.display.flip()
                if button_4.collidepoint(mx,my):
                    launched = True
                    while launched:
                        Qmr=Miroir(A)
                        afficherauth(Qmr)
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
    #pygame.display.flip()
    clock.tick(30)
def afficherauth(Automate):
    i1 = 0
    i2= 0
    i3 = 0
    i6=0
    newscreen = pygame.display.set_mode((740, 580))
    background_image = pygame.image.load("Capture2.PNG").convert()
    background_image = pygame.transform.scale(background_image, (900, 700))
    newscreen.blit(background_image, [0, 0])
    draw_text('Alphabet',fontmin,(255,255,255),newscreen,10,150,1)
    draw_text('Etat initial',fontmin,(255,255,255),newscreen,130,150,1)
    draw_text('Etats',fontmin,(255,255,255),newscreen,290,150,1)
    draw_text('Etats finaux',fontmin,(255,255,255),newscreen,450,150,1)
    draw_text('Transitions',fontmin,(255,255,255),newscreen,590,150,1)
    init_surface = fontmin.render(Automate["etatinitial"][0], True, (0,10,20))
    button_init = pygame.Rect(170,200,50+init_surface.get_width(),30)
    pygame.draw.rect(newscreen,(0,10,40),button_init)
    
    draw_text(Automate["etatinitial"][0],fontmin,(255,255,255),newscreen,150,190,1)
    for a in Automate["Alphabet"]:
        a_surface = fontmin.render(a, True, (0,10,20))
        button_a = pygame.Rect(10,200+i6,50+a_surface.get_width(),30)
        pygame.draw.rect(newscreen,(0,10,40),button_a)
        draw_text(a,fontmin,(255,255,255),newscreen,-10,190+i6,1)
        i6+=40
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
    tab = pygame.Rect(0,190,850,max(i1,i2,i3,i6)+10)
    pygame.draw.rect(newscreen,(0,10,20),tab)
    i1 = 0
    i2= 0
    i3 = 0
    i6 = 0
    init_surface = fontmin.render(Automate["etatinitial"][0], True, (0,10,20))
    button_init = pygame.Rect(170,200,50+init_surface.get_width(),30)
    pygame.draw.rect(newscreen,(0,10,40),button_init)
    draw_text(Automate["etatinitial"][0],fontmin,(255,255,255),newscreen,150,190,1)
    for a in Automate["Alphabet"]:
        a_surface = fontmin.render(a, True, (0,10,20))
        button_a = pygame.Rect(20,200+i6,50+a_surface.get_width(),30)
        pygame.draw.rect(newscreen,(0,10,40),button_a)
        draw_text(a,fontmin,(255,255,255),newscreen,-10,190+i6,1)
        i6+=40
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
#########################################################################################################################
drag=False
text=''
textf=''
posx=0
posy=0
click_trans=0
event_prec=pygame.MOUSEMOTION
dic={}
dic["nom"]=[]
dic["x"]=[]
dic["y"]=[]
dic["w"]=[]
dic["h"]=[]
xi=10
yi=150
ht=100
wt=50
yf=230
ya=300
terminer=False
mouse_prec=pygame.mouse.get_pos()
start=(0,0)
end=(0,0)
liste_text_box=[]
liste_text=[]
clock = pygame.time.Clock()
nouvel_transition=False
word_prec=''
word=''
out=False
nob=True
normal=False
nnormal=True
rien=False
input_box =InputBoxs(120,300,40,50,'')
input_box.draw(windowSurface)
pygame.display.update()

##########################################################################################################################

launched = True
while launched:
    ##############################################################################################################################
    
    
    button(10,10,100,50,"Ajouter un nouvel etat")
    button(10,80,100,50,"Ajouter une transition")
    button(xi,yi,ht,wt,"Ajouter un etat initial")
    button(xi,yf,ht,wt,"Ajouter un etat final")
    button(xi,ya,ht,wt,"Ajouter un alphabet")
    button(500,500,150,50,"Suivant")
    
    
    shiftDown = False
    abj=True
    #input_box.rect.center = [320, 240]
    pygame.display.update()
    
    for event in pygame.event.get():


        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(xi,ya, wt, ht).collidepoint(event.pos):
                abj=True
            if pygame.Rect(500,500, 150, 50).collidepoint(event.pos):
                print(Automate)
                launched = False
               

        if abj:
            
            alpha,rien=input_box.handle_event(event)
            #pygame.display.update()
            if alpha!='':
                if rien==True:
                    Automate["Alphabet"].append(alpha)
        if nouvel_transition :
            word,out=liste_text_box[0].handle_event(event)
            
            if  out== False:
                liste_text.append(word)
                nouvel_transition=False
                liste_text_box.remove(liste_text_box[0])
                t.mot=word
                
                
                nob=True
                Automate["tbltransition"].append(t)
        word_prec=word   
        mouse_current=pygame.mouse.get_pos()
        x,y,w,h,text=generate_click(10,10,100,50,event)
        if text!='':
            textf=text
            Automate["etats"].append(text)
        else:
            x,y,w,h,text=initial(xi,yi,ht,wt,event)
            if text!='':
                textf=text
                Automate["etatinitial"].append(text)
                Automate["etats"].append(text)
            else:
                x,y,w,h,text=final(xi,yf,ht,wt,event)
                if text!='':
                    textf=text
                    Automate["etatsfinaux"].append(text)
                    Automate["etats"].append(text)
                
                
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            drag=move_state(x,y,w,h,event)
        if event.type==pygame.MOUSEBUTTONUP:
            if drag:
                drag=False
                pygame.draw.ellipse(windowSurface,blackcolor,[x,y,w,h])
                posx,posy=pygame.mouse.get_pos()
                pygame.draw.ellipse(windowSurface,white,[posx,posy,w,h])
                adding_text(textf,posx,posy,w,h)
                dic["nom"].append(textf)
                dic["x"].append(posx)
                dic["y"].append(posy)
                dic["w"].append(w)
                dic["h"].append(h)
                pygame.display.update()
        if terminer:
            en_cours=True
        else:
            en_cours=generate_trans(event_prec,mouse_prec)
        if en_cours==True:
            terminer=True
            if nob==True:
                t=transition('','','')
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                k=0
                for key in dic["nom"]:
                    if dic["x"][k]+dic["w"][k]>mouse[0]>dic["x"][k] and dic["y"][k]+dic["h"][k]>mouse[1]>dic["y"][k]:
                        t.edep=key
                        #Automate["etats"].append(key)
                        nob=False
                        start=(dic["x"][k]+22,dic["y"][k]+4)
                        break
                    k+=1
                        
            
            if event.type==pygame.MOUSEBUTTONUP:
                         
                mouse=pygame.mouse.get_pos()
                k=0
                for key in dic["nom"]:
                   
                    if dic["x"][k]+dic["w"][k]>mouse[0]>dic["x"][k] and dic["y"][k]+dic["h"][k]>mouse[1]>dic["y"][k]:
                        t.earv=key
                        #Automate["etats"].append(key)
                        end=(dic["x"][k]+24,dic["y"][k]+10)
                        
                        terminer=False
                        
                        break    
                    k+=1
            if start!=(0,0) and end!=(0,0):
                nouvel_transition=True
                start1=(0,0)
                end1=(0,0)
                start1=(start[0],start[1])
                end1=(end[0]-10,int(end[1]+30))
                #pygame.draw.line(windowResolution,white, start, end,2)
                
                fleche=arrow(windowSurface, white, white,start1,end1,5, 2)
                text_box=InputBox(int((start1[0]+end1[0])/2),int((start1[1]+end1[1])/2), 15, 15,normal, text='')
                text_box.draw(windowSurface)
                liste_text_box.append(text_box)
                
                
                #fleche.move_ip(end[0],start[1]-50)
                

                start=(0,0)
                end=(0,0)
                pygame.display.update()
        
        for text_box in liste_text_box:
            text_box.update()
        pygame.display.update()
        event_prec=event
        mouse_prec=mouse_current

        
        if event.type==pygame.QUIT:
            continu=False
    pygame.display.update()
    clock.tick(60)

    
    ##############################################################################################################################
print(Automate)
launched = True
while launched :
    define(Automate)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            launched=False
        
        pygame.display.flip()
    pygame.display.flip()

