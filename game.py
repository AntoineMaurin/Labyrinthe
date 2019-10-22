from maze import Maze

import pygame


class Game:

    def __init__(self):

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

        needle = pygame.image.load("img/aiguille.png").convert_alpha()
        ether = pygame.image.load("img/ether.png").convert()
        syringe = pygame.image.load("img/seringue.png").convert_alpha()

        self.obj_list = [needle, ether, syringe]

        self.current_pos = self.maze.get_current_pos()
        self.next_pos = self.current_pos

        self.draw_empty_maze()
        self.draw_character()
        self.draw_guardian()
        self.draw_objects()

    def draw_empty_maze(self):
        x, y = 0, 0

        for row in self.maze.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(
                                    self.window,
                                    (35, 35, 35),
                                    pygame.Rect(x, y, self.width, self.width)
                                    )
                else:
                    pygame.draw.rect(
                                    self.window,
                                    (35, 35, 35),
                                    pygame.Rect(x, y, self.width, self.width),
                                    2
                                    )
                x = x + self.width
            x = 0
            y = y + self.width

    def draw_character(self):
        char_pos = self.maze.get_current_pos()
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

            rect = self.obj_list[i].get_rect()
            rect.topleft = (pos[1] * self.width + 4, pos[0] * self.width + 3)
            self.window.blit(self.obj_list[i], rect)
            i += 1

    def compute_next_pos(self, event):
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

    def try_to_move(self):
        if self.maze.is_wall(self.next_pos):
            print("It's a wall")
        elif self.maze.is_too_far(self.next_pos):
            print("Wrong way")
        elif self.maze.is_guardian(self.next_pos):
            running = False
            return running
        else:
            if self.maze.is_object(self.next_pos):
                print("You picked up an object")
            self.move()

    def move(self):
        self.redraw()
        rect = self.mc_gyv.get_rect()
        rect.topleft = (self.next_pos[1] * self.width + 4, self.next_pos[0] * self.width + 4)
        self.window.blit(self.mc_gyv, rect)

        self.maze.update_mazelist(self.next_pos)

    def redraw(self):
        pygame.draw.rect(self.window, (240, 240, 240), pygame.Rect(self.current_pos[1] * self.width, self.current_pos[0] * self.width, self.width, self.width))
        pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(self.current_pos[1] * self.width, self.current_pos[0] * self.width, self.width, self.width), 2)

        pygame.draw.rect(self.window, (240, 240, 240), pygame.Rect(self.next_pos[1] * self.width, self.next_pos[0] * self.width, self.width, self.width))
        pygame.draw.rect(self.window, (35, 35, 35), pygame.Rect(self.next_pos[1] * self.width, self.next_pos[0] * self.width, self.width, self.width), 2)

    def play(self):
        running = True

        while running is not False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.compute_next_pos(event)
                    running = self.try_to_move()

            pygame.display.flip()
