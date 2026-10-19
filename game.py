import pygame
pygame.init()

#make window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("Caption")

#variable declaration
player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0.3

#sprites
player = pygame.surface.Surface((100, 100))
player.fill((0, 0, 0))

#game loop
while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    
    #output
    player_y += player_vel_y
    if (player_y+player.height) >= window.height:
        player_vel_y = 0
    window.fill((255, 255, 255))

    #place player
    window.blit(player, (player_x, player_y))
    pygame.display.flip()