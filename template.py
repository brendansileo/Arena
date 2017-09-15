import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
mousex, mousey = 0, 0
square = pygame.image.load('conway_square.png')
live_square = pygame.image.load('conway_square_live.png')
blank = pygame.image.load('blank.png')
squarex, squarey = 900, 900
xdist = 0
ydist = 0
mousedown = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mousex, mousey = pygame.mouse.get_pos()
    if mousedown == True:
        screen.blit(blank, (mousex - 50, mousey - 50))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mousedown = True
            pygame.display.flip()   
    
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            mousedown = False
            

    for x in range(0,1000): 
        squarex = random.randint(0,800)
        squarey = random.randint(0,800)
        
        if squarex > mousex + 50 or squarex < mousex - 50 or squarey > mousey + 50 or squarey < mousey - 50 or random.randint(0,4) == 1 and squarex > mousex + 30 or squarex < mousex - 30 or squarey > mousey + 30 or squarey < mousey - 30:
            if random.randint(0,1) is 1:
                screen.blit(square, (squarex, squarey))
            else:
                screen.blit(live_square, (squarex, squarey))
    
    pygame.display.flip()   