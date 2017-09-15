import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 800))
done = False
mousex, mousey = 0, 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mousex, mousey = pygame.mouse.get_pos()
    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, rgb(235, 244, 66), (mousex, mousey), 20)
    pygame.display.flip()   