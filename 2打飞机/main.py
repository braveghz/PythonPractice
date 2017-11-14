# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
TITLE = "play plane"

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

background = pygame.image.load('resource/background.png')
plane_img = pygame.image.load('resource/shoot.png')
game_over = pygame.image.load('resource/gameover.png')

plane_rect = pygame.Rect(0, 99, 102, 126)
player = plane_img.subsurface(plane_rect)
player_pos = [150, 400]

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(player, player_pos)
    pygame.display.flip()
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_pos[1] -= 3
    if keys[K_DOWN]:
        player_pos[1] += 3
    if keys[K_LEFT]:
        player_pos[0] -= 3
    if keys[K_RIGHT]:
        player_pos[0] += 3



