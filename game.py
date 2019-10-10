from maze import Maze

import pygame
import time

class Game:

    def __init__(self):

        self.maze = Maze
        self.mazelist = Maze.get_maze(Maze)

        pygame.init()
        pygame.display.set_caption("Maze - Project 3")
        self.window = pygame.display.set_mode((600, 600))
        self.window.fill((240, 240, 240))

        # grey = (35, 35, 35)
        # green = (0, 153, 76)
        # blue = (0, 128, 255)
        # white = (240, 240, 240)
        # window.fill(white)

        self.picked = 0

        position = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        self.current_pos = position[0][0], position[0][1]


    def generate_maze(self):
        x, y = 0, 0
        width = 40

        for row in self.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(x, y, width, width))
                elif cell == 'M' :
                    pygame.draw.rect(self.window, (0, 128, 255), pygame.Rect(x, y, width, width))
                elif cell == 'OBJ' :
                    pygame.draw.rect(self.window, (0, 153, 76), pygame.Rect(x, y, width, width))
                else:
                    pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(x, y, width, width), 2)
                x = x + width
            x = 0
            y = y + width

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
                self.picked = self.picked + 1
                print("You picked up an object \n", "picked : ", self.picked)
            pygame.draw.rect(self.window, (240, 240, 240), pygame.Rect(self.current_pos[1] *width, self.current_pos[0] *width,width,width))
            pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(self.current_pos[1] *width, self.current_pos[0] *width,width,width), 2)
            pygame.draw.rect(self.window, (0, 128, 255), pygame.Rect(next_pos[1] *width, next_pos[0] *width,width,width))
            time.sleep(.1)
            self.mazelist[self.current_pos[0]][self.current_pos[1]] = '#'
            self.current_pos = next_pos
            self.mazelist[next_pos[0]][next_pos[1]] = 'M'
