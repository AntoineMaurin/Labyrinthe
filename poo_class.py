import random
import time
import pygame

pygame.init()
pygame.display.set_caption("Maze - Project 3")
window = pygame.display.set_mode((600, 600))

grey = (35, 35, 35)
green = (0, 153, 76)
blue = (0, 128, 255)
white = (240, 240, 240)
window.fill(white)

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

    def generate_maze(self):
        self.x, self.y = 0, 0
        self.w = 40

        for row in self.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(window, grey, pygame.Rect(self.x, self.y, self.w, self.w))
                elif cell == 'M' :
                    pygame.draw.rect(window, blue, pygame.Rect(self.x, self.y, self.w, self.w))
                elif cell == 'OBJ1' :
                    pygame.draw.rect(window, green, pygame.Rect(self.x, self.y, self.w, self.w))
                elif cell == 'OBJ2' :
                    pygame.draw.rect(window, green, pygame.Rect(self.x, self.y, self.w, self.w))
                elif cell == 'OBJ3' :
                    pygame.draw.rect(window, green, pygame.Rect(self.x, self.y, self.w, self.w))
                else:
                    pygame.draw.rect(window, grey, pygame.Rect(self.x, self.y, self.w, self.w), 2)
                self.x = self.x + self.w
            self.x = 0
            self.y = self.y + self.w

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

    def check_key(self, event):
        dict = {'running' : True, 'pressed_key' : ''}
        if event.type == pygame.QUIT:
            dict['running'] = False
            return dict
        elif event.key == pygame.K_LEFT:
            dict['pressed_key'] = 'ARROW LEFT'
            return dict
        elif event.key == pygame.K_RIGHT:
            dict['pressed_key'] = 'ARROW RIGHT'
            return dict
        elif event.key == pygame.K_UP:
            dict['pressed_key'] = 'ARROW UP'
            return dict
        elif event.key == pygame.K_DOWN:
            dict['pressed_key'] = 'ARROW DOWN'
            return dict
        elif event.key == pygame.K_ESCAPE:
            dict['pressed_key'] = 'ESCAPE'
            return dict
        else:
            return dict

    def move_or_quit(self, pressed_key):
        running = True
        if pressed_key == 'ARROW LEFT':
            next_pos = self.current_pos[0], (self.current_pos[1] - 1)
        elif pressed_key == 'ARROW RIGHT':
            next_pos = self.current_pos[0], (self.current_pos[1] + 1)
        elif pressed_key == 'ARROW UP':
            next_pos = (self.current_pos[0] - 1), self.current_pos[1]
        elif pressed_key == 'ARROW DOWN':
            next_pos = (self.current_pos[0] + 1), self.current_pos[1]
        elif pressed_key == 'ESCAPE':
            running = False
            return running
        else:
            next_pos = self.current_pos
            print("Please use keyboard arrows to move or Esc to quit")

        if self.mazelist[next_pos[0]][next_pos[1]] == 'X':
            print("C'est un mur")
            time.sleep(.15)
        elif self.mazelist[next_pos[0]][next_pos[1]] == 'O':
            if all(i in self.picked for i in self.objects_list):
                print("picked : ", self.picked)
                print("YOU WIN, WELL PLAYED")
                running = False
                return running
            else:
                print("YOU LOSE")
                print("picked : ", self.picked)
                running = False
                return running
        else:
            if self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ1':
                self.picked.append('OBJ1')
                print("Vous avez récupéré l'objet 1\n", "picked : ", self.picked)
            elif self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ2':
                self.picked.append('OBJ2')
                print("Vous avez récupéré l'objet 2\n", "picked : ", self.picked)
            elif self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ3':
                self.picked.append('OBJ3')
                print("Vous avez récupéré l'objet 3\n", "picked : ", self.picked)
            pygame.draw.rect(window, white, pygame.Rect(self.current_pos[1] * self.w, self.current_pos[0] * self.w, self.w, self.w))
            pygame.draw.rect(window, grey, pygame.Rect(self.current_pos[1] * self.w, self.current_pos[0] * self.w, self.w, self.w), 2)
            pygame.draw.rect(window, blue, pygame.Rect(next_pos[1] * self.w, next_pos[0] * self.w, self.w, self.w))
            time.sleep(.15)
            self.current_pos = next_pos
            self.maze_list[self.current_pos[0]][self.current_pos[1]] = ' '
            self.maze_list[next_pos[0]][next_pos[1]] = 'M'
