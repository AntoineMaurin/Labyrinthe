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
        self.picked = 0
        opened_file = open("Maze.txt", 'r')
        self.mazelist = [list(line.strip()) for line in opened_file.readlines()]
        position = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        self.current_pos = position[0][0], position[0][1]
        opened_file.close()

    def get_maze(self):
        return self.mazelist

    def display_maze(self):
        for row in self.mazelist:
            print(row)
        print("\n", "-------------------------------------------------", "\n")

    def generate_maze(self):
        x, y = 0, 0
        width = 40

        for row in self.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(window, grey, pygame.Rect(x, y, width, width))
                elif cell == 'M' :
                    pygame.draw.rect(window, blue, pygame.Rect(x, y, width, width))
                elif cell == 'OBJ' :
                    pygame.draw.rect(window, green, pygame.Rect(x, y, width, width))
                else:
                    pygame.draw.rect(window, grey, pygame.Rect(x, y, width, width), 2)
                x = x + width
            x = 0
            y = y + width

    def add_objects(self):
        i = 0
        while i < 3 :
            OBJ = random.randint(1, 13), random.randint(1, 13)
            if (self.mazelist[OBJ[0]][OBJ[1]] != 'X'):
                self.mazelist[OBJ[0]][OBJ[1]] = 'OBJ'
                i += 1

    def set_position(self, event):
        if event.key == pygame.K_LEFT:
            next_pos = self.current_pos[0], (self.current_pos[1] - 1)
        elif event.key == pygame.K_RIGHT:
            next_pos = self.current_pos[0], (self.current_pos[1] + 1)
        elif event.key == pygame.K_UP:
            next_pos = (self.current_pos[0] - 1), self.current_pos[1]
        elif event.key == pygame.K_DOWN:
            next_pos = (self.current_pos[0] + 1), self.current_pos[1]
        else:
            next_pos = self.current_pos
            print("Please use keyboard arrows to move")
        return next_pos

    def move(self, next_pos):
        # print('next item : ', self.mazelist[next_pos[0]][next_pos[1]])
        if self.mazelist[next_pos[0]][next_pos[1]] == 'X':
            print("It's a wall")
            time.sleep(.1)
        elif next_pos[0] > 14 or next_pos[1] > 14 or next_pos[0] < 0 or next_pos[1] < 0:
            print("Wrong way.")
        elif self.mazelist[next_pos[0]][next_pos[1]] == 'O':
            if self.picked == 3:
                print("picked : ", self.picked)
                print("You win, well played")
                running = False
                return running
            else:
                print("You lose")
                print("picked : ", self.picked)
                running = False
                return running
        else:
            x, y = 0, 0
            width = 40
            if self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ':
                self.picked += 1
                print("You picked up an object \n", "picked : ", self.picked)
            pygame.draw.rect(window, white, pygame.Rect(self.current_pos[1] *width, self.current_pos[0] *width,width,width))
            pygame.draw.rect(window, grey, pygame.Rect(self.current_pos[1] *width, self.current_pos[0] *width,width,width), 2)
            pygame.draw.rect(window, blue, pygame.Rect(next_pos[1] *width, next_pos[0] *width,width,width))
            time.sleep(.1)
            self.maze_list[self.current_pos[0]][self.current_pos[1]] = '#'
            self.current_pos = next_pos
            self.maze_list[next_pos[0]][next_pos[1]] = 'M'
        # print("current pos : ", self.current_pos)
        # print("next_pos : ", next_pos)
