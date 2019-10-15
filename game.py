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
        self.guardian = pygame.image.load("img/Gardien.png").convert_alpha()

        aiguille = pygame.image.load("img/aiguille.png").convert_alpha()
        ether = pygame.image.load("img/ether.png").convert()
        seringue = pygame.image.load("img/seringue.png").convert_alpha()

        self.obj_list = [aiguille, ether, seringue]

        self.current_pos = self.maze.get_current_pos()
        self.next_pos = self.current_pos

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
        char_pos = self.maze.get_current_pos()
        # pygame.draw.rect(self.window, (0, 128, 255), pygame.Rect(pos[0] * width, pos[1] * width, width, width))
        rect = self.mc_gyv.get_rect()
        rect.topleft = (char_pos[1] * self.width + 4, char_pos[0] * self.width + 3)
        self.window.blit(self.mc_gyv, rect)

    def draw_guardian(self):
        guard_pos = self.maze.get_guard_pos()
        rect = self.guardian.get_rect()
        rect.topleft = (guard_pos[1] * self.width + 3, guard_pos[0] * self.width + 3)
        self.window.blit(self.guardian, rect)

    def draw_objects(self):
        i = 0
        for pos in self.maze.get_objects_pos():
            print('obj : ', pos)

            rect = self.obj_list[i].get_rect()
            rect.topleft = (pos[1] * self.width + 4, pos[0] * self.width + 3)
            self.window.blit(self.obj_list[i], rect)
            i += 1

    def set_position(self, event):
        self.current_pos = self.maze.get_current_pos()
        if event.key == pygame.K_LEFT:
            self.next_pos = self.current_pos[0], (self.current_pos[1] - 1)
        elif event.key == pygame.K_RIGHT:
            self.next_pos = self.current_pos[0], (self.current_pos[1] + 1)
        elif event.key == pygame.K_UP:
            self.next_pos = (self.current_pos[0] - 1), self.current_pos[1]
        elif event.key == pygame.K_DOWN:
            self.next_pos = (self.current_pos[0] + 1), self.current_pos[1]
        else:
            self.next_pos = self.current_pos
            print("Please use keyboard arrows to move")

    def move(self):
        if self.maze.is_wall(self.next_pos):
            print("It's a wall")
            time.sleep(.1)
        elif self.maze.is_too_far(self.next_pos):
            print("Wrong way.")
        elif self.maze.is_guardian(self.next_pos):
            running = False
            return running
        else:
            if self.maze.is_object(self.next_pos):
                print("You picked up an object")
            self.redraw()

    def redraw(self):
        pygame.draw.rect(self.window, (240, 240, 240), pygame.Rect(self.current_pos[1] * self.width, self.current_pos[0] * self.width, self.width, self.width))
        pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(self.current_pos[1] * self.width, self.current_pos[0] * self.width, self.width, self.width), 2)

        rect = self.mc_gyv.get_rect()
        rect.topleft = (self.next_pos[1] * self.width + 4, self.next_pos[0] * self.width + 4)
        self.window.blit(self.mc_gyv, rect)

        time.sleep(.1)
        self.maze.update_mazelist(self.next_pos)

    def play(self):
        running = True

        """Sometimes move function returns None, and gets out of the "while running" loop"""
        while running is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.set_position(event)
                    running = self.move()

            pygame.display.flip()
