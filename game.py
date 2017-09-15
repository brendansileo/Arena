import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 800))
done = False

playerx, playery = 0,0
playerx_a, playery_a = 0, 0
playerx_v, playery_v = 0, 0

max_a = 5
max_v = 10

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
    	playerx_a = -3
    #	if playerx_a > -1 * max_a:
    #		playerx_a -= 1
    elif keys[pygame.K_d]:
    	playerx_a = 3
    #	if playerx_a < max_a:
    #		playerx_a += 1
    else:
    	playerx_a = 0

    if keys[pygame.K_w]:
    	playery_a = -3
    #	if playery_a > -1 * max_a:
    #		playery_a -= 1
    elif keys[pygame.K_s]:
    	playery_a = 3
    #	if playery_a < max_a:
    #		playery_a += 1
    else:
    	playery_a = 0

    if playerx_a > 0 and playerx_v < max_v:
    	playerx_v += playerx_a
    elif playerx_a < 0 and playerx_v > -1 * max_v:
    	playerx_v += playerx_a
    elif playerx_v != 0:
    	if playerx_v > 0:
    		playerx_v -= 1
    	else:
    		playerx_v += 1

    if playery_a > 0 and playery_v < max_v:
    	playery_v += playery_a
    elif playery_a < 0 and playery_v > -1 * max_v:
    	playery_v += playery_a
    elif playery_v != 0:
    	if playery_v > 0:
    		playery_v -= 1
    	else:
    		playery_v += 1
    
    playerx += playerx_v
    playery += playery_v

    
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (235, 244, 66), (playerx, playery), 20)
    pygame.display.flip()   