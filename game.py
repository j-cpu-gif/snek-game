import pygame
from random import randint
from time import sleep
pygame.init()

#make window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Caption")

#variable declaration
apple1_x = randint(0,750)
apple1_y = -50
apple1_vel_y = 0.1

apple2_x = randint(0,750)
apple2_y = -50
apple2_vel_y = 0.1

apple3_x = randint(0,750)
apple3_y = -50
apple3_vel_y = 0.1

apple4_x = randint(0,750)
apple4_y = -50
apple4_vel_y = 0.1

apple5_x = randint(0,750)
apple5_y = -50
apple5_vel_y = 0.1

apple6_x = randint(0,750)
apple6_y = -50
apple6_vel_y = 0.1

#sprites
apple1 = pygame.surface.Surface((40, 40))
apple1.fill((255, 0, 0))

apple2 = pygame.surface.Surface((40, 40))
apple2.fill((255, 0, 0))

apple3 = pygame.surface.Surface((40, 40))
apple3.fill((255, 0, 0))

apple4 = pygame.surface.Surface((40, 40))
apple4.fill((255, 0, 0))

apple5 = pygame.surface.Surface((40, 40))
apple5.fill((255, 0, 0))

apple6 = pygame.surface.Surface((40, 40))
apple6.fill((255, 0, 0))

#game loop
while True:
    elapsed_time = pygame.time.get_ticks()
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

    
    #output
    if elapsed_time >randint(1000,2000) :
        apple1_y += apple1_vel_y
    if (apple1_y) >= window.height:
        apple1_y = 0
        apple1_x = randint(0,600)
    window.fill((255, 255, 255))

    if elapsed_time > randint(4000,6000):
        apple2_y += apple2_vel_y
    if (apple2_y) >= window.height:
        apple2_y = 0
        apple2_x = randint(0,600)
    window.fill((255, 255, 255))

    if elapsed_time > randint(7000,8000):
        apple3_y += apple3_vel_y
    if (apple3_y) >= window.height:
        apple3_y = 0
        apple3_x = randint(0,600)
    window.fill((255, 255, 255))
    
    if elapsed_time > randint(8000,9000):
        apple4_y += apple4_vel_y
    if (apple4_y) >= window.height:
        apple4_y = 0
        apple4_x = randint(0,600)
    window.fill((255, 255, 255))

    if elapsed_time > randint(10000,12000):
        apple5_y += apple5_vel_y
    if (apple5_y) >= window.height:
        apple5_y = 0
        apple5_x = randint(0,600)
    window.fill((255, 255, 255))
    
    if elapsed_time > randint(15000,20000):
        apple6_y += apple6_vel_y
    if (apple6_y) >= window.height:
        apple6_y = 0
        apple6_x = randint(0,600)
    window.fill((255, 255, 255))
    

    #place sprites
    window.blit(apple1, (apple1_x, apple1_y))
    window.blit(apple2, (apple2_x, apple2_y))
    window.blit(apple3, (apple3_x, apple3_y))
    window.blit(apple4, (apple4_x, apple4_y))
    window.blit(apple5, (apple5_x, apple5_y))
    window.blit(apple6, (apple6_x, apple6_y))
    pygame.display.flip()