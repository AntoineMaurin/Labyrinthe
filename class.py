import random
import pygame
import keyboard
import time

# class Game:
#
#     def __init__(self, title, width, height):
#
#         pygame.init()
#         pygame.display.set_caption(title)
#         self.window = pygame.display.set_mode((width, height))
#
#         self.grey = (35, 35, 35)
#         self.green = (0, 153, 76)
#         self.blue = (0, 128, 255)
#         self.window.fill((240, 240, 240))

class Maze:

    def __init__(self):
        self.maze_list = []
        self.current_pos = []
        opened_file = open("Maze.txt", 'r')
        self.mazelist = [list(line.strip()) for line in opened_file.readlines()]
        self.current_pos = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        self.current_pos = self.current_pos[0][0], self.current_pos[0][1]
        opened_file.close()

    def get_maze(self):
        return self.mazelist

    def display_maze(self):
        for row in self.mazelist:
            print(row)
        print("\n", "-------------------------------------------------", "\n")

    def add_objects(self):
        while True:
            OBJ1 = random.randint(1, 13), random.randint(1, 13)
            OBJ2 = random.randint(1, 13), random.randint(1, 13)
            OBJ3 = random.randint(1, 13), random.randint(1, 13)
            if (self.mazelist[OBJ1[0]][OBJ1[1]] == ' ') and (self.mazelist[OBJ2[0]][OBJ2[1]] == ' ') and (self.mazelist[OBJ3[0]][OBJ3[1]] == ' '):
                self.mazelist[OBJ1[0]][OBJ1[1]] = 'OBJ1'
                self.mazelist[OBJ2[0]][OBJ2[1]] = 'OBJ2'
                self.mazelist[OBJ3[0]][OBJ3[1]] = 'OBJ3'
                break
        self.picked = []
        self.objects_list = ['OBJ1', 'OBJ2', 'OBJ3']

        print("OBJ 1 : ", OBJ1)
        print("OBJ 2 : ", OBJ2)
        print("OBJ 3 : ", OBJ3)

#---------------------------FONCTIONS-SEULES----------------------------------#

def check_key():
    if event.key == pygame.K_LEFT:
        return 'ARROW LEFT'
    elif event.key == pygame.K_RIGHT:
        return 'ARROW RIGHT'
    elif event.key == pygame.K_UP:
        return 'ARROW UP'
    elif event.key == pygame.K_DOWN:
        return 'ARROW DOWN'
    elif event.key == pygame.K_ESCAPE:
        return 'ESCAPE'

def move_with(pressed_key):
    running = True
    if pressed_key == 'ARROW LEFT':
        next_pos = my_maze.current_pos[0], (my_maze.current_pos[1] - 1)
    elif pressed_key == 'ARROW RIGHT':
        next_pos = my_maze.current_pos[0], (my_maze.current_pos[1] + 1)
    elif pressed_key == 'ARROW UP':
        next_pos = (my_maze.current_pos[0] - 1), my_maze.current_pos[1]
    elif pressed_key == 'ARROW DOWN':
        next_pos = (my_maze.current_pos[0] + 1), my_maze.current_pos[1]
    elif pressed_key == 'ESCAPE':
        running = False
        return running
    else:
        next_pos = my_maze.current_pos
        print("Please use keyboard arrows to move or Esc to quit")

    if my_maze.mazelist[next_pos[0]][next_pos[1]] == 'X':
        print("Y'A UN MUR")
        time.sleep(.15)
    elif my_maze.mazelist[next_pos[0]][next_pos[1]] == 'O':
        if all(i in my_maze.picked for i in my_maze.objects_list):
            print("picked : ", my_maze.picked)
            print("YOU WIN, WELL PLAYED")
            running = False
            return running
        else:
            print("YOU LOSE")
            print("picked : ", my_maze.picked)
            running = False
            return running
    else:
        if my_maze.mazelist[next_pos[0]][next_pos[1]] == 'OBJ1':
            my_maze.picked.append('OBJ1')
            print("Vous avez récupéré l'objet 1\n", "picked : ", my_maze.picked)
        elif my_maze.mazelist[next_pos[0]][next_pos[1]] == 'OBJ2':
            my_maze.picked.append('OBJ2')
            print("Vous avez récupéré l'objet 2\n", "picked : ", my_maze.picked)
        elif my_maze.mazelist[next_pos[0]][next_pos[1]] == 'OBJ3':
            my_maze.picked.append('OBJ3')
            print("Vous avez récupéré l'objet 3\n", "picked : ", my_maze.picked)
        pygame.draw.rect(window, white, pygame.Rect(my_maze.current_pos[1] * w, my_maze.current_pos[0] * w, w, w))
        pygame.draw.rect(window, grey, pygame.Rect(my_maze.current_pos[1] * w, my_maze.current_pos[0] * w, w, w), 2)
        pygame.draw.rect(window, blue, pygame.Rect(next_pos[1] * w, next_pos[0] * w, w, w))
        time.sleep(.15)
        my_maze.current_pos = next_pos
        my_maze.maze_list[my_maze.current_pos[0]][my_maze.current_pos[1]] = ' '
        my_maze.maze_list[next_pos[0]][next_pos[1]] = 'M'

#-------------------------------PROGRAMME-PRINCIPAL---------------------------#

# g = Game("Maze - Project 3", 600, 600)

pygame.init()
pygame.display.set_caption("Maze - Project 3")
window = pygame.display.set_mode((600, 600))

grey = (35, 35, 35)
green = (0, 153, 76)
blue = (0, 128, 255)
white = (240, 240, 240)
window.fill(white)

my_maze = Maze()

my_maze.display_maze()
my_maze.add_objects()
print("\n", "-------------------------------------------------", "\n")

my_maze.display_maze()

my_maze.maze_list = my_maze.get_maze()

x, y = 0, 0
w = 40

running = True
while running != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN :
            pressed_key = check_key()
            running = move_with(pressed_key)

    for row in my_maze.mazelist:
        for cell in row:
            if cell == 'X':
                pygame.draw.rect(window, grey, pygame.Rect(x, y, w, w))
            elif cell == 'M' :
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
