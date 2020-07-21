#coding:utf-8
"""
Pour png avec transparence :
remplacer convert par convert_alpha()
"""
import pygame 
pygame.init()
windowResolution = (640,480)
pygame.display.set_caption("Cherifa")
windowSurface = pygame.display.set_mode(windowResolution)
imageSurface = pygame.image.load("IMG_9891.JPG")
imageSurface.convert()
imageSurface.set_colorkey((0,0,255)) #rendre transparent une couleur dans une image
launched = True
while(launched):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    windowSurface.blit(imageSurface,[10,10])
    pygame.display.flip()