import pygame
from random import randint
from time import sleep
pygame.init()

#make window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Caption")

#variable declaration
apple1_x = 0
apple1_y = 0
apple1_vel_y = 0.3

apple2_x = randint(0,600)
apple2_y = 0
apple2_vel_y = 0.4

#sprites
apple1 = pygame.surface.Surface((40, 40))
apple1.fill((255, 0, 0))
apple2 = pygame.surface.Surface((40, 40))
apple2.fill((255, 0, 0))

#game loop
while True:
    elapsed_time = pygame.time.get_ticks()
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    
    #output
    apple1_y += apple1_vel_y
    if (apple1_y) >= window.height:
        apple1_y = 0
        apple1_x = randint(0,600)
    window.fill((255, 255, 255))

    if elapsed_time > randint(1000,5000):
        apple2_y += apple2_vel_y
    if (apple2_y) >= window.height:
        sleep(1)
        apple2_y = 0
        apple2_x = randint(0,600)
    window.fill((255, 255, 255))
    

    #place sprites
    window.blit(apple1, (apple1_x, apple1_y))
    window.blit(apple2, (apple2_x, apple2_y))
    pygame.display.flip()