import pygame
import math

from bullet import bullet

pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
done = False

ship_img = pygame.image.load('img/ship.jpg')
ship_w = ship_img.get_rect().size[0]
ship_middle = ship_img.get_rect().size[0]/2
ship_h = ship_img.get_rect().size[1]

playerx, playery = 0,0
playerx_a, playery_a = 0, 0
playerx_v, playery_v = 0, 0

bullets = []

max_v = 15

while not done:  
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
    	playerx_a = -3
    elif keys[pygame.K_d]:
    	playerx_a = 3
    else:
    	playerx_a = 0

    if keys[pygame.K_w]:
    	playery_a = -3
    elif keys[pygame.K_s]:
    	playery_a = 3
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

    if playerx < 0:
    	playerx = width
    elif playerx > width:
    	playerx = 0

    if playery < 0:
   	    playery = height
    elif playery > height:
        playery = 0

    angle = (180 / math.pi) * -math.atan2(playerx_v, -playery_v)

    events = pygame.event.get()
    for event in events:
    	if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
            	if len(bullets) < 3:
                	bullets.append(bullet(playerx_v, playery_v, playerx+ship_middle, playery, width, height))
    
    screen.fill((0,0,0))
    for b in bullets:
    	bx,by = b.tick(bullets)
    	if bx != None:
    		pygame.draw.circle(screen, (244, 244, 66), (int(bx),int(by)), 5)
    ship_img_r = pygame.transform.rotate(ship_img, angle)
    screen.blit(ship_img_r, (playerx, playery))
    pygame.display.flip()   