import pygame
import math
import eztext
import socket

from bullet import bullet
from ship import ship
from datetime import *

pygame.init()
pygame.font.init()

width, height = 1280, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial', 30)

txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='Enter your name: ')

ship_img = pygame.image.load('ship.jpg')
ship_w = ship_img.get_rect().size[0]
ship_middle = ship_img.get_rect().size[0]/2
ship_h = ship_img.get_rect().size[1]

playername = ''
playernum = -1

ships = [ship(0,0), ship(100,100)]

bullets = []

max_v = 8

exit = False
name_entry = True
while name_entry:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            name_entry = False
            exit = True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        playername = txtbx.value
        name_entry = False

    txtbx.update(events)
    txtbx.draw(screen)
    pygame.display.flip()
    clock.tick(30)

if not exit:
    screen.fill((0,0,0))
    print 1
    textsurface = myfont.render('Waiting for an opponent...', False, (255, 255, 255))
    screen.blit(textsurface,(width/2, height/2))
    pygame.display.flip()
    s = socket.socket()
    host = "24.91.116.125"
    port = 8000
    s.connect((host, port))
    role = s.recv(1) #0 = host 1 = not host
    print 2
    playernum = int(role)
    if role == "0":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            s.bind(('', 8001))
        except socket.error as msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
         
        s.listen(10)
        print "Waiting for partner"
        conn, addr = s.accept()
    else:
        host = s.recv(20)
        print host
        port = 8001
        s = socket.socket()
        s.connect((host, port))

if not exit:
    playing = True
    while playing:  
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ships[playernum].x_a = -1
        elif keys[pygame.K_d]:
            ships[playernum].x_a = 1
        else:
            ships[playernum].x_a = 0

        if keys[pygame.K_w]:
            ships[playernum].y_a = -1
        elif keys[pygame.K_s]:
            ships[playernum].y_a = 1
        else:
            ships[playernum].y_a = 0

        if ships[playernum].x_a > 0 and ships[playernum].x_v < max_v:
            ships[playernum].x_v += ships[playernum].x_a
        elif ships[playernum].x_a < 0 and ships[playernum].x_v > -1 * max_v:
            ships[playernum].x_v += ships[playernum].x_a
        elif ships[playernum].x_v != 0:
            if ships[playernum].x_v > 0:
                ships[playernum].x_v -= 1
            else:
                ships[playernum].x_v += 1

        if ships[playernum].y_a > 0 and ships[playernum].y_v < max_v:
            ships[playernum].y_v += ships[playernum].y_a
        elif ships[playernum].y_a < 0 and ships[playernum].y_v > -1 * max_v:
            ships[playernum].y_v += ships[playernum].y_a
        elif ships[playernum].y_v != 0:
            if ships[playernum].y_v > 0:
                ships[playernum].y_v -= 1
            else:
                ships[playernum].y_v += 1
        
        ships[playernum].x_p += ships[playernum].x_v
        ships[playernum].y_p += ships[playernum].y_v

        if ships[playernum].x_p < 0:
            ships[playernum].x_p = width
        elif ships[playernum].x_p > width:
            ships[playernum].x_p = 0

        if ships[playernum].y_p < 0:
               ships[playernum].y_p = height
        elif ships[playernum].y_p > height:
            ships[playernum].y_p = 0

        ships[playernum].angle = (180 / math.pi) * -math.atan2(ships[playernum].x_v, -ships[playernum].y_v)

        if playernum == 0:
            conn.send(ships[0].toString())
            data = conn.recv(1024)
            data = data.split()
            ships[1].x_p = float(data[0])
            ships[1].y_p = float(data[1])
            ships[1].angle = float(data[2])
        else:
            s.send(ships[1].toString())
            data = s.recv(1024)
            data = data.split()
            ships[0].x_p = float(data[0])
            ships[0].y_p = float(data[1])
            ships[0].angle = float(data[2])

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(bullets) < 3:
                        bullets.append(bullet(ships[playernum].x_v, ships[playernum].y_v, ships[playernum].x_p+ship_middle, ships[playernum].y_p, width, height))
        
        screen.fill((0,0,0))
        for b in bullets:
            bx,by = b.tick(bullets)
            if bx != None:
                pygame.draw.circle(screen, (244, 244, 66), (int(bx),int(by)), 5)
        ship_img_r = pygame.transform.rotate(ship_img, ships[playernum].angle)
        screen.blit(ship_img_r, (ships[playernum].x_p, ships[playernum].y_p))
        for sh in ships:
            ship_img_r = pygame.transform.rotate(ship_img, sh.angle)
            screen.blit(ship_img_r, (sh.x_p, sh.y_p))
        pygame.display.flip()   
        clock.tick(30)
s.close()