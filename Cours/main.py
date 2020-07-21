#coding:utf-8
import pygame
pygame.init()#initialiser les programmes principaux pour lancer pygame
"""
pygame.FULLSCREEN
pygame.DOUBLEBUF
| POUR AJOUTER PLUSIEURS
pygame.NOFRAME
"""
pygame.display.set_caption("Premiere fenetre")
whitecolor = (255,255,255)
blackcolor = (0,0,0)
screen = pygame.display.set_mode((640,480),pygame.RESIZABLE)#crée la fenetre en prenant la résolution comme parametres tuple
screen.fill(whitecolor)
pygame.draw.line(screen,blackcolor,[100,20],[200,20],5)
pygame.draw.rect(screen,blackcolor,pygame.Rect(50,50,150,65),2)
pygame.draw.circle(screen,blackcolor,[300,300],50,2)
coord = [(10,10),(100,10),(30,50)]
pygame.draw.polygon(screen,blackcolor,coord,2)
pygame.display.flip()
"""
print(type(screen))
print(pygame.display.Info())
print(pygame.get_sdl_version())
"""
launched = True
while launched :
    for event in pygame.event.get() :
        if event.type ==pygame.QUIT:
            launched = False
