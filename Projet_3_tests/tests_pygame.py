import pygame
import random
import time

from labyrinthe import here_is_the_maze, display_maze

THE_MAZE = here_is_the_maze()

pygame.init()

pygame.display.set_caption("Projet 3 - Labyrinthe")
window = pygame.display.set_mode((600, 600))

grey = (35, 35, 35)
green = (0, 153, 76)
blue = (0, 128, 255)

window.fill((240, 240, 240))

def check_key():
    if event.key == pygame.K_LEFT:
        return 'ARROW LEFT'
    elif event.key == pygame.K_RIGHT:
        return 'ARROW RIGHT'
    elif event.key == pygame.K_UP:
        return 'ARROW UP'
    elif event.key == pygame.K_DOWN:
        return 'ARROW DOWN'

def move_with(pressed_key):
    if pressed_key == 'ARROW LEFT':
        pygame.draw.rect(window, grey, pygame.Rect(0, 100, 40, 40), 2)
    elif pressed_key == 'ARROW RIGHT':
        pygame.draw.rect(window, grey, pygame.Rect(200, 100, 40, 40), 2)
    elif pressed_key == 'ARROW UP':
        pygame.draw.rect(window, grey, pygame.Rect(100, 0, 40, 40), 2)
    elif pressed_key == 'ARROW DOWN':
        pygame.draw.rect(window, grey, pygame.Rect(100, 200, 40, 40), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            pressed_key = check_key(event)
            move_with(pressed_key)


    pygame.display.flip()
