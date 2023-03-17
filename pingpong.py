from random import *
from math import *
import pygame
from pygame.locals import *
import os
from ball import ball
from player import player

pygame.init()

#initialize display elements
screen = pygame.display.set_mode((800,650),0,32)
pygame.display.set_caption('ping pong')
font = pygame.font.SysFont('arial',16)
gofont = pygame.font.SysFont('arial',30)
sc1 = 0
sc2 = 0

#custom class instance

ball = ball((400,300),(0.5,0.5),1)
p1 = player((100,100))
p2 = player((680,100))
size = (2,100)


def vc(b):
    x,y = b.pos
    xd,yd = b.dire
    if(y<=0):
        yd = yd*-1
    if(y>=550):
        yd = yd*-1
    return (xd,yd)

def score(b):
    x,y = b.pos
    xd,yd = b.dire
    if(x<=0):
        return 2
    if(x>=750):
        return 1
    return 0

def hc(b):
    x,y = b.pos
    xd,yd = b.dire
    if(x<=0):
        xd = xd*-1
        
    if(x>=750):
        xd = xd*-1
        
    return (xd,yd)

def hh(b):
    xd,yd = b.dire
    xd = xd*-1
    return (xd,yd)

def vh(b):
    xd,yd = b.dire
    yd = yd*-1
    return (xd,yd)


def p1c(p,b):
    px,py = p.pos
    bx,by = b.pos
    bdx,bdy = b.dire
    ox,oy = size
    if(bx == px+ox and bdx<0):
        if(by > (py-17) and by < py+oy):
            xd,yd = hh(b)
            return (xd,yd)
    return bdx,bdy
        
def p2c(p,b):
    px,py = p.pos
    bx,by = b.pos
    bdx,bdy = b.dire
    ox,oy = size
    if(bx == (px-50) and bdx>0):
        if(by > (py-17) and by < py+oy):
            xd,yd = hh(b)
            return (xd,yd)
    return bdx,bdy

def limitpos(p):
    x,y = p.pos
    if(y<0):
        y = 0
    elif(y>500):
        y = 500
    return (x,y)


while True:
    event = pygame.event.poll()
    if event.type == QUIT:
        os._exit(0)

    
    #Set the frame Rate
    clock = pygame.time.Clock()
    time_passed = clock.tick(600)

    #Check for key pressed

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_q]:
        p1.up()
    if pressed_keys[K_a]:
        p1.down()
    if pressed_keys[K_o]:
        p2.up()
    if pressed_keys[K_l]:
        p2.down()

    p1.pos = limitpos(p1)
    p2.pos = limitpos(p2)

    #Scoring
    if(score(ball) == 1):
        sc1 = sc1 +1
    if(score(ball) == 2):
        sc2 = sc2 +1

    
    #Ball collision with horizontal wall
    ball.dire = hc(ball)
    #Ball collisioin with vertical wall
    ball.dire = vc(ball)

    #Update ball position
    ball.updatePos()
    
    ball.dire = p1c(p1,ball)
    ball.dire = p2c(p2,ball)

    #Fill the screen with white
    screen.fill((255,255,255))

    #Draw Court
    pygame.draw.line(screen,(255,0,0),(0,0),(0,600),5)
    pygame.draw.line(screen,(255,0,0),(800,0),(800,600),5)
    pygame.draw.line(screen,(255,0,0),(0,0),(800,0),5)
    pygame.draw.line(screen,(255,0,0),(0,600),(800,600),5)
    pygame.draw.line(screen,(255,0,0),(400,0),(400,600),5)
    pygame.draw.line(screen,(255,0,0),(0,300),(800,300),2)
    
    #Print players
    pygame.draw.rect(screen,(0,0,0),Rect(p1.pos,size))
    pygame.draw.rect(screen,(0,0,0),Rect(p2.pos,size))

    

    #Print ball
    x,y = ball.pos
    x = x+25
    y = y+25
    pygame.draw.circle(screen,(0,0,255),(x,y),25)

    #Draw Score
    #Print score
    sc1size = font.render('score: '+str(sc1),True,(0,0,0)).get_size()
    sc2size = font.render('score: '+str(sc2),True,(0,0,0)).get_size()
    screen.blit(font.render('Player 1 Score: '+str(sc1),True,(0,0,0)),(0,610))
    screen.blit(font.render('Player 2 Score: '+str(sc2),True,(0,0,0)),(400,610))

    

    #Display Update
    pygame.display.update()
