import random
import keyboard
import time
import pygame

from labyrinthe import here_is_the_maze, display_maze

# pygame.init()
# screen = pygame.display.set_mode((640, 480))
#
# print(pygame.get_sdl_version())

"""Préparation du labyrinthe et affichage"""
THE_MAZE = here_is_the_maze()

"""On choisit au hasard où placer les trois éléments et on s'assure qu'ils sont
sur une case disponible"""
while True:
    OBJ1 = random.randint(1, 13), random.randint(1, 13)
    OBJ2 = random.randint(1, 13), random.randint(1, 13)
    OBJ3 = random.randint(1, 13), random.randint(1, 13)
    if (THE_MAZE[OBJ1[0]][OBJ1[1]] == ' ') and (THE_MAZE[OBJ2[0]][OBJ2[1]] == ' ') and (THE_MAZE[OBJ3[0]][OBJ3[1]] == ' '):
        THE_MAZE[OBJ1[0]][OBJ1[1]] = 'OBJ1'
        THE_MAZE[OBJ2[0]][OBJ2[1]] = 'OBJ2'
        THE_MAZE[OBJ3[0]][OBJ3[1]] = 'OBJ3'
        break

print("OBJ 1 : ", OBJ1)
print("OBJ 2 : ", OBJ2)
print("OBJ 3 : ", OBJ3)

display_maze(THE_MAZE)

picked = []

"""Fonction de déplacement"""
def move(direction):
    """On récupère la position de MacGyver"""
    current_pos = [(index, THE_MAZE[index].index('MC')) for index in range(len(THE_MAZE)) if 'MC' in THE_MAZE[index]]
    current_pos = current_pos[0][0], current_pos[0][1]
    """On change la valeur du tuple de position en fonction de la direction souhaitée"""
    if direction == 'left' :
        next_pos = current_pos[0], (current_pos[1] - 1)
    elif direction == 'right' :
        next_pos = current_pos[0], (current_pos[1] + 1)
    elif direction == 'up' :
        next_pos = (current_pos[0] - 1), current_pos[1]
    elif direction == 'down' :
        next_pos = (current_pos[0] + 1), current_pos[1]

    """Check si y'a un mur ou pas, si y'en a pas, on regarde s'il y a un
     objet. Si on a un objet on l'ajoute dans la liste.
     Puis quand il se déplace sur la case de sortie on regarde si il a bien tous
     les objets"""
    if THE_MAZE[next_pos[0]][next_pos[1]] == 'X':
        print("Y'A UN MUR")
        display_maze(THE_MAZE)
    else:
        THE_MAZE[current_pos[0]][current_pos[1]] = ' '
        THE_MAZE[next_pos[0]][next_pos[1]] = 'MC'
        if next_pos == OBJ1 :
            picked.append('OBJ1')
            print("Vous avez récupéré l'objet 1\n", "picked : ", picked)
        elif next_pos == OBJ2 :
            picked.append('OBJ2')
            print("Vous avez récupéré l'objet 2\n", "picked : ", picked)
        elif next_pos == OBJ3 :
            picked.append('OBJ3')
            print("Vous avez récupéré l'objet 3\n", "picked : ", picked)
        elif next_pos == (14, 4):
            if 'OBJ1' and 'OBJ2' and 'OBJ3' in picked:
                print("picked : ", picked)
                print("YOU WIN, WELL PLAYED")
            else:
                print("YOU LOSE")
                print("picked : ", picked)
        display_maze(THE_MAZE)
        print("current_pos : ", current_pos)
        print("next_pos : ", next_pos)

while True:
    try:
        if keyboard.is_pressed('z'):
            move('up')
            time.sleep(0.1)
        elif keyboard.is_pressed('q'):
            move('left')
            time.sleep(0.1)
        elif keyboard.is_pressed('d'):
            move('right')
            time.sleep(0.1)
        elif keyboard.is_pressed('s'):
            move('down')
            time.sleep(0.1)
        else: pass
    except:
        break
