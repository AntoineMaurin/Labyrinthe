from maze import Maze

import pygame
import time


class Game:

    def __init__(self):

        """Here we are getting the mazelist from the get_maze() method of the
        Maze class."""
        self.maze = Maze()
        self.width = 45

        pygame.init()
        pygame.display.set_caption("Maze - Project 3")
        self.window = pygame.display.set_mode((675, 675))
        self.window.fill((240, 240, 240))

        # grey = (35, 35, 35)
        # green = (0, 153, 76)
        # blue = (0, 128, 255)
        # white = (240, 240, 240)

        self.mc_gyv = pygame.image.load("img/MacGyver.png").convert()
        self.guardian = pygame.image.load("img/Gardien.png").convert()

        aiguille = pygame.image.load("img/aiguille.png").convert()
        ether = pygame.image.load("img/ether.png").convert()
        seringue = pygame.image.load("img/seringue.png").convert()

        self.obj_list = [aiguille, ether, seringue]

    def draw_empty_maze(self):
        x, y = 0, 0

        for row in self.maze.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(x, y, self.width, self.width))
                else:
                    pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(x, y, self.width, self.width), 2)
                x = x + self.width
            x = 0
            y = y + self.width

    def draw_character(self):
        pos = self.maze.get_current_pos()
        # pygame.draw.rect(self.window, (0, 128, 255), pygame.Rect(pos[0] * width, pos[1] * width, width, width))
        rect = self.mc_gyv.get_rect()
        rect.topleft = (pos[1] * self.width, pos[0] * self.width)
        self.window.blit(self.mc_gyv, rect)

    def draw_guardian(self):
        pos = self.maze.get_guard_pos()
        rect = self.guardian.get_rect()
        rect.topleft = (pos[1] * self.width + 6, pos[0] * self.width + 6)
        self.window.blit(self.guardian, rect)

    def draw_objects(self):
        i = 0
        for pos in self.maze.get_objects_pos():
            print('obj : ', pos)
            rect = self.obj_list[i].get_rect()
            rect.topleft = (pos[1] * self.width + 3, pos[0] * self.width + 3)
            self.window.blit(self.obj_list[i], rect)
            i += 1


    # def generate_maze(self):
    #     x, y = 0, 0
    #     width = 45
    #
    # aiguille = pygame.image.load("img/aiguille.png").convert()
    # ether = pygame.image.load("img/ether.png").convert()
    # seringue = pygame.image.load("img/seringue.png").convert()
    #
    # self.obj_list = [aiguille, ether, seringue]
    #
    #     """Creation of the graphic maze with Rect objects from the mazelist."""
    #     for row in self.mazelist:
    #         for cell in row:
    #             if cell == 'X':
    #                 pygame.draw.rect(
    #                     self.window,
    #                     (35, 35, 35),
    #                     pygame.Rect(x, y, width, width)
    #                     )
    #             elif cell == 'M':
    #                 rect = self.mc_gyv.get_rect()
    #                 rect.topleft = (x + 7, y)
    #                 self.window.blit(self.mc_gyv, rect)
    #             elif cell == 'OBJ':
    #                 pygame.draw.rect(
    #                     self.window,
    #                     (0, 153, 76),
    #                     pygame.Rect(x, y, width, width)
    #                     )
    #             elif cell == 'O':
    #                 rect = guardian.get_rect()
    #                 rect.topleft = (x + 8, y + 5)
    #                 self.window.blit(guardian, rect)
    #             else:
    #                 pygame.draw.rect(
    #                     self.window,
    #                     (35, 35, 35),
    #                     pygame.Rect(x, y, width, width), 2
    #                     )
    #             x = x + width
    #         x = 0
    #         y = y + width

    def set_position(self, event):
        current_pos = self.maze.get_current_pos()
        if event.key == pygame.K_LEFT:
            next_pos = current_pos[0], (current_pos[1] - 1)
        elif event.key == pygame.K_RIGHT:
            next_pos = current_pos[0], (current_pos[1] + 1)
        elif event.key == pygame.K_UP:
            next_pos = (current_pos[0] - 1), current_pos[1]
        elif event.key == pygame.K_DOWN:
            next_pos = (current_pos[0] + 1), current_pos[1]
        else:
            next_pos = current_pos
            print("Please use keyboard arrows to move")
        return next_pos

    def move(self, next_pos):
        current_pos = self.maze.get_current_pos()
        if self.maze.is_wall(next_pos) == True:
            print("It's a wall")
            time.sleep(.1)
        elif self.maze.is_too_far(next_pos) == True:
            print("Wrong way.")
        elif self.maze.is_guardian(next_pos) == True:
            running = False
            return running
        else:
            x, y = 0, 0
            width = 45
            if self.maze.is_object(next_pos):
                print("You picked up an object")
            pygame.draw.rect(self.window, (240, 240, 240), pygame.Rect(current_pos[1] * self.width, current_pos[0] * self.width, self.width, self.width))
            pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(current_pos[1] * self.width, current_pos[0] * self.width, self.width, self.width), 2)
            rect = self.mc_gyv.get_rect()
            rect.topleft = (next_pos[1] * width + 8, next_pos[0] * width + 2)
            self.window.blit(self.mc_gyv, rect)
            time.sleep(.1)
            self.maze.update_mazelist(next_pos)

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
