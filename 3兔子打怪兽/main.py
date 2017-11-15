# -*- coding:utf-8 -*-
import sys
import math
import pygame
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PAI = 3.1415926


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

player = pygame.image.load('resources/images/dude.png')  # 64 x 46
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')\

arrows = []
acc = [0, 0]  # 射箭次数/射中次数--计算精度

player_pos = [200, 200]  # 这是左上角的坐标
player_width, player_height = player.get_size()

running = True
while running:
    w, h = grass.get_size()
    for i in range(SCREEN_WIDTH / w):
        for j in range(SCREEN_HEIGHT / h):
            screen.blit(grass, (i * h, j * w))

    screen.blit(castle, (50, 100))
    screen.blit(castle, (50, 200))
    screen.blit(castle, (50, 300))
    screen.blit(castle, (50, 400))

    mouse_pos = pygame.mouse.get_pos()
    y = mouse_pos[1] - player_pos[1] - player_height / 2
    x = mouse_pos[1] - player_pos[0] - player_width / 2
    angle = 360 - math.atan2(y, x) * 180 / PAI
    player1 = pygame.transform.rotate(player, angle)

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_pos[1] -= 5
    elif keys[K_DOWN]:
        player_pos[1] += 5
    elif keys[K_LEFT]:
        player_pos[0] -= 5
    elif keys[K_RIGHT]:
        player_pos[0] += 5

    screen.blit(player1, player_pos)
    pygame.display.flip()

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key ==
                K_ESCAPE) or event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
