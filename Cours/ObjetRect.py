#coding:utf-8
"""
mynvrect = myrect.copy()
myrect.move() | myrect.move_ip()
myrect.inflate()
myrect.colliderect()
"""
import pygame
import time
pygame.init()
windowResolution=(640,480)
pygame.display.set_caption("l'objet RECT")
windowSurface = pygame.display.set_mode(windowResolution)
whitecolor = (255,255,255)
redcolor=(255,0,0)
blackcolor= (0,0,0)
myrect = pygame.Rect(10,100,80,80)
pygame.draw.rect(windowSurface,whitecolor,myrect)
bluecolor = (0,75,255)
myblock = pygame.Rect(600,50,20,480)
pygame.draw.rect(windowSurface,bluecolor,myblock)
pygame.display.flip()
"""
i=0
while i<18:
    time.sleep(.030)
    windowSurface.fill(redcolor)
    myrect.x +=10
    myrect.y += 10
    pygame.draw.rect(windowSurface,whitecolor,myrect)
    i +=1
    pygame.display.flip()"""

launched = True
while launched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    while not myrect.colliderect(myblock):
        time.sleep(.010)
        windowSurface.fill(blackcolor)
        myrect.x +=1
        pygame.draw.rect(windowSurface,whitecolor,myrect)
        pygame.draw.rect(windowSurface,bluecolor,myblock)
        pygame.display.flip()