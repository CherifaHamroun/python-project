import math
import pygame
import sys
import time
from dataclasses import dataclass
pygame.init()
white=(255,255,255)
font=(114,153,183)
pink=(233,144,144)
black=(47,9,9)
light_pink=(232,165,165)
COLOR_INACTIVE=pink
COLOR_ACTIVE=light_pink
FONT = pygame.font.Font(None,20)



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('event.mousebuttondown')
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                print('self.rect.collidepoint(event.pos)')
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = black if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print('event.key.k_return')
                    print('hihi')
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    print('event.key.k_backspace')
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                print(self.text)
                self.txt_surface = FONT.render(self.text, True, self.color)
                gameDisplay.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
                pygame.display.flip()
                print('rerender')
        return self.text

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




@dataclass
class transition:
    edep=''
    mot=''
    earv=''
    def __init__(self, ede,mo,ear):
        edep=ede
        mot=mo
        earv=ear
 


gameDisplay=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Automate Envirement')
counter=0
def in_range(x,y,w,h):
    ins=False
    mouse=pygame.mouse.get_pos()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        ins=True         
    return ins;
    
def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect();
def adding_text(text,x,y,w,h):
    font = pygame.font.SysFont("comicsansms", 10)
    text_ajouter,supp =text_objects(text,font)
    supp.center=(int(x+(w/2)),int(y+(h/2)))
    gameDisplay.blit(text_ajouter,supp)

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
        pygame.draw.rect(gameDisplay,light_pink,[xpos,ypos,width,height])

        if event.type==pygame.MOUSEBUTTONUP :
            counter+=1
            text='s'+str(counter)
            x_etat=150
            y_etat=60
            w_etat=70
            h_etat=40
            pygame.draw.ellipse(gameDisplay,white,[x_etat,y_etat,w_etat,h_etat])
            adding_text(text,x_etat,y_etat,w_etat,h_etat)
            pygame.display.update()

    else:
        pygame.draw.rect(gameDisplay,pink,[xpos,ypos,width,height])
       
        
         
    return x_etat,y_etat,w_etat,h_etat,text;

def button(x,y,w,h,text):
    mouse=pygame.mouse.get_pos()
    pygame.draw.rect(gameDisplay,pink,[x,y,w,h])
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay,light_pink,[x,y,w,h])
    else:
        pygame.draw.rect(gameDisplay,pink,[x,y,w,h])
    font = pygame.font.SysFont("comicsansms", 10)
    text_ajouter,supp =text_objects(text,font)
    supp.center=(int(x+(w/2)),int(y+(h/2)))
    gameDisplay.blit(text_ajouter,supp)
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
    gameDisplay.blit(arrow,(x,y))



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









Automate={}
Automate["tbltransition"]=[]

 

    
    


continu=True
gameDisplay.fill(font)
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
while continu:
    
    button(10,10,100,50,"Ajouter un nouvel etat")
    button(10,80,100,50,"Ajouter une transition")
    input_box =TextBox()
    shiftDown = False
    input_box.rect.center = [320, 240]
    pygame.display.update()
    
    for event in pygame.event.get():

        print(liste_text_box)
        
        if len(liste_text_box)!=0 :
            word=liste_text_box[-1].handle_event(event)
            liste_text_box.remove(liste_text_box[-1])
            print(word)
            print(nouvel_transition)
            if nouvel_transition :
                liste_text.append(word)
                nouvel_transition=False
                
        
        word_prec=word   
        mouse_current=pygame.mouse.get_pos()
        x,y,w,h,text=generate_click(10,10,100,50,event)
        if text!='':
            textf=text
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            drag=move_state(x,y,w,h,event)
        if event.type==pygame.MOUSEBUTTONUP:
            if drag:
                drag=False
                pygame.draw.ellipse(gameDisplay,font,[x,y,w,h])
                posx,posy=pygame.mouse.get_pos()
                pygame.draw.ellipse(gameDisplay,white,[posx,posy,w,h])
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
            t=transition('','','')
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse=pygame.mouse.get_pos()
                k=0
                for key in dic["nom"]:
                    if dic["x"][k]+dic["w"][k]>mouse[0]>dic["x"][k] and dic["y"][k]+dic["h"][k]>mouse[1]>dic["y"][k]:
                        t.edep=key
                        start=(dic["x"][k]+22,dic["y"][k]+4)
                        break
                    k+=1
                        
            
            if event.type==pygame.MOUSEBUTTONUP:
                         
                mouse=pygame.mouse.get_pos()
                k=0
                for key in dic["nom"]:
                   
                    if dic["x"][k]+dic["w"][k]>mouse[0]>dic["x"][k] and dic["y"][k]+dic["h"][k]>mouse[1]>dic["y"][k]:
                        t.earv=key
                        end=(dic["x"][k]+24,dic["y"][k]+10)
                        Automate["tbltransition"].append(t)
                        terminer=False
                        
                        break    
                    k+=1
            if start!=(0,0) and end!=(0,0):
                nouvel_transition=True
                start1=(0,0)
                end1=(0,0)
                start1=(start[0],start[1])
                end1=(end[0]-10,int(end[1]+30))
                #pygame.draw.line(gameDisplay,white, start, end,2)
                
                fleche=arrow(gameDisplay, white, black,start1,end1,5, 2)
                text_box=InputBox(int((start1[0]+end1[0])/2),int((start1[1]+end1[1])/2), 15, 15, text='')
                text_box.draw(gameDisplay)
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
  
    
    
        
    















pygame.quit()
quit()
