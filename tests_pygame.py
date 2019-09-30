import pygame
import random

from labyrinthe import here_is_the_maze, display_maze

THE_MAZE = here_is_the_maze()

pygame.init()

pygame.display.set_caption("Projet 3 - Labyrinthe")
window = pygame.display.set_mode((600, 600))

grey = (35, 35, 35)
green = (0, 153, 76)
blue = (0, 128, 255)

while True:
    OBJ1 = random.randint(1, 13), random.randint(1, 13)
    OBJ2 = random.randint(1, 13), random.randint(1, 13)
    OBJ3 = random.randint(1, 13), random.randint(1, 13)
    if (THE_MAZE[OBJ1[0]][OBJ1[1]] == ' ') and (THE_MAZE[OBJ2[0]][OBJ2[1]] == ' ') and (THE_MAZE[OBJ3[0]][OBJ3[1]] == ' '):
        THE_MAZE[OBJ1[0]][OBJ1[1]] = 'OBJ1'
        THE_MAZE[OBJ2[0]][OBJ2[1]] = 'OBJ2'
        THE_MAZE[OBJ3[0]][OBJ3[1]] = 'OBJ3'
        break

window.fill((240, 240, 240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x, y = 0, 0
    w = 40

    for row in THE_MAZE:
        for cell in row:
            if cell == 'X':
                pygame.draw.rect(window, grey, pygame.Rect(x, y, w, w))
            elif cell == 'MC' :
                pygame.draw.rect(window, blue, pygame.Rect(x, y, w, w))
            elif cell == 'OBJ1' :
                pygame.draw.rect(window, green, pygame.Rect(x, y, w, w))
            elif cell == 'OBJ2' :
                pygame.draw.rect(window, green, pygame.Rect(x, y, w, w))
            elif cell == 'OBJ3' :
                pygame.draw.rect(window, green, pygame.Rect(x, y, w, w))
            else:
                pygame.draw.rect(window, grey, pygame.Rect(x, y, w, w), 2)
            x = x + w
        x = 0
        y = y + w

    pygame.display.flip()
