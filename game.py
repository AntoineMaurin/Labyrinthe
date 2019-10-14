from maze import Maze

import pygame
import time


class Game:

    def __init__(self):

        """Here we are getting the mazelist from the get_maze() method of the
        Maze class."""
        self.mazelist = Maze.get_maze(Maze)

        pygame.init()
        pygame.display.set_caption("Maze - Project 3")
        self.window = pygame.display.set_mode((675, 675))
        self.window.fill((240, 240, 240))

        # grey = (35, 35, 35)
        # green = (0, 153, 76)
        # blue = (0, 128, 255)
        # white = (240, 240, 240)

        """Variable used to count the picked up objects"""
        self.picked = 0

        """This list comprehension returns the coordinates of the 'M' element
        in self.mazelist inside a tuple as the first element of a list.
        Then, our self.current_pos takes the coordinates as a simple tuple
        to allow an easier use of these coordinates."""
        position = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        self.current_pos = position[0][0], position[0][1]

        guard_pos = [(index, self.mazelist[index].index('O')) for index in range(len(self.mazelist)) if 'O' in self.mazelist[index]]
        self.guard_pos = guard_pos[0][0], guard_pos[0][1]

    def generate_maze(self):
        x, y = 0, 0
        width = 45

        guardian = pygame.image.load("img/Gardien.png").convert()
        self.mc_gyv = pygame.image.load("img/MacGyver.png").convert()

        aiguille = pygame.image.load("img/aiguille.png").convert()
        ether = pygame.image.load("img/ether.png").convert()
        seringue = pygame.image.load("img/seringue.png").convert()

        self.obj_list = [aiguille, ether, seringue]

        """Creation of the graphic maze with Rect objects from the mazelist."""
        for row in self.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(
                        self.window,
                        (35, 35, 35),
                        pygame.Rect(x, y, width, width)
                        )
                elif cell == 'M':
                    rect = self.mc_gyv.get_rect()
                    rect.topleft = (x + 7, y)
                    self.window.blit(self.mc_gyv, rect)
                elif cell == 'OBJ':
                    pygame.draw.rect(
                        self.window,
                        (0, 153, 76),
                        pygame.Rect(x, y, width, width)
                        )
                elif cell == 'O':
                    rect = guardian.get_rect()
                    rect.topleft = (x + 8, y + 5)
                    self.window.blit(guardian, rect)
                else:
                    pygame.draw.rect(
                        self.window,
                        (35, 35, 35),
                        pygame.Rect(x, y, width, width), 2
                        )
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
            else:
                print("You lose")
                print("picked : ", self.picked)
            running = False
            return running
        else:
            x, y = 0, 0
            width = 45
            if self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ':
                self.picked = self.picked + 1
                print("You picked up an object \n", "picked : ", self.picked)
            pygame.draw.rect(self.window, (240, 240, 240), pygame.Rect(self.current_pos[1] * width, self.current_pos[0] * width, width, width))
            pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(self.current_pos[1] * width, self.current_pos[0] * width, width, width), 2)
            rect = self.mc_gyv.get_rect()
            rect.topleft = (next_pos[1] * width + 8, next_pos[0] * width + 2)
            self.window.blit(self.mc_gyv, rect)
            # pygame.draw.rect(self.window, (0, 128, 255), pygame.Rect(next_pos[1] * width, next_pos[0] * width, width, width))
            time.sleep(.1)
            self.mazelist[self.current_pos[0]][self.current_pos[1]] = '#'
            self.current_pos = next_pos
            self.mazelist[next_pos[0]][next_pos[1]] = 'M'

    def play(self):
        running = True

        """Sometimes move function returns None, and gets out of the "while running" loop"""
        while running is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    next_pos = self.set_position(event)
                    running = self.move(next_pos)

            pygame.display.flip()



# rect = mc_gyv.get_rect()
# rect.topleft  = (x, y)
#
# window.blit(mc_gyv, rect)
