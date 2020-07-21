#coding:utf-8
import pygame 
windowResolution = (640,480)
pygame.init()
pygame.display.set_caption("Les evenements")
windowSurface = pygame.display.set_mode(windowResolution,pygame.RESIZABLE)
arialfont = pygame.font.SysFont("arial",30)
whiteColor = (255,255,255)
blackColor = (0,0,0)
dimentisionText = arialfont.render("{}".format(windowResolution),True,whiteColor)
windowSurface.blit(dimentisionText,[20,10])
pygame.display.flip()
launched = True
while launched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.VIDEORESIZE:
            windowSurface.fill(blackColor)
            dimentisionText = arialfont.render("{}x{}".format(event.w , event.h),True,whiteColor)
            windowSurface.blit(dimentisionText,[20,10])
            pygame.display.flip()
            launched = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("haut")
            elif event.key == pygame.K_DOWN:
                print("bas")
        elif event.type == pygame.MOUSEMOTION:
                print("{}".format(event.pos))
        


