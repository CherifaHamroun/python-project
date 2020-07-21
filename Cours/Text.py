#coding:utf-8
import pygame
pygame.init()
windowResolution = (640,480)
pygame.display.set_caption("Affichage de texte")
windowSurface = pygame.display.set_mode(windowResolution)

#print(pygame.font.get_fonts())
arialFont = pygame.font.SysFont("arial",80,True,True)
font = pygame.font.Font("Street Photography.otf",32)
blue = (0,75,255)
hello = arialFont.render("hello",True,blue)
hello2 = font.render("hello",True,blue)
windowSurface.blit(hello,[400,200])
windowSurface.blit(hello2,[0,0])
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched=False
    