from maze import Maze
import pygame

"""This class manages the game in general, using the pygame library."""

CELL_SIZE = 45


class Game:

    """Creates a Maze object from the Maze class, initializes pygame
    and the images of the game, set up character and guardian positions
    and draws the maze."""
    def __init__(self):

        self.maze = Maze()

        pygame.init()
        pygame.display.set_caption("Maze - Project 3")
        self.window = pygame.display.set_mode((
                                              self.maze.width * CELL_SIZE,
                                              self.maze.height * CELL_SIZE
                                              ))
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

    """Draws the maze from the mazelist attribute of the Maze class with only
    walls and free spaces."""
    def draw_empty_maze(self):
        x, y = 0, 0

        for row in self.maze.mazelist:
            for cell in row:
                if cell == 'X':
                    pygame.draw.rect(
                                    self.window,
                                    (35, 35, 35),
                                    pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                                    )
                else:
                    pygame.draw.rect(
                                    self.window,
                                    (35, 35, 35),
                                    pygame.Rect(x, y, CELL_SIZE, CELL_SIZE), 2
                                    )
                x = x + CELL_SIZE
            x = 0
            y = y + CELL_SIZE

    """Draws the main character on the game window."""
    def draw_character(self):
        pos = self.maze.get_current_pos()
        rect = self.mc_gyv.get_rect()
        rect.topleft = (pos[1] * CELL_SIZE + 4, pos[0] * CELL_SIZE + 3)
        self.window.blit(self.mc_gyv, rect)

    """Draws the guardian which is also the exit of the maze."""
    def draw_guardian(self):
        pos = self.maze.get_guard_pos()
        rect = self.guardian.get_rect()
        rect.topleft = (pos[1] * CELL_SIZE + 3, pos[0] * CELL_SIZE + 3)
        self.window.blit(self.guardian, rect)

    """Draws the three objects at random positions on free spaces of the
    maze."""
    def draw_objects(self):
        i = 0
        for pos in self.maze.get_objects_pos():

            rect = self.obj_list[i].get_rect()
            rect.topleft = (pos[1] * CELL_SIZE + 4, pos[0] * CELL_SIZE + 3)
            self.window.blit(self.obj_list[i], rect)
            i += 1

    """As soon as a KEYDOWN event has been detected, this function is called
    and computes the next pos attribute to prepare a move in the desired
    direction."""
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

    """This function checks if we can move to the next position, if yes, it
    calls the move() function."""
    def try_to_move(self, running):
        if self.maze.is_too_far(self.next_pos):
            return True
        elif self.maze.is_wall(self.next_pos):
            return True
        elif self.maze.is_guardian(self.next_pos):
            return False
        else:
            if self.maze.is_object(self.next_pos):
                print("You picked up an object")
            self.move()
            return True

    """This functions starts by calling the redraw function, then draws
    the character on the next position, and sends the next pos to the
    update_macgyver() function, to the Maze class."""
    def move(self):
        self.redraw()
        rect = self.mc_gyv.get_rect()
        rect.topleft = (
                        self.next_pos[1] * CELL_SIZE + 4,
                        self.next_pos[0] * CELL_SIZE + 4
                        )
        self.window.blit(self.mc_gyv, rect)

        self.maze.update_macgyver(self.next_pos)

    """This function draws a normal square at the current position and next
    position, to erase the character image or a potential object on the next
    position."""
    def redraw(self):
        pygame.draw.rect(
                        self.window,
                        (240, 240, 240),
                        pygame.Rect(
                                    self.current_pos[1] * CELL_SIZE,
                                    self.current_pos[0] * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE)
                                    )
        pygame.draw.rect(
                        self.window,
                        (35, 35, 35),
                        pygame.Rect(
                                    self.current_pos[1] * CELL_SIZE,
                                    self.current_pos[0] * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE), 2
                                    )
        pygame.draw.rect(
                        self.window,
                        (240, 240, 240),
                        pygame.Rect(
                                    self.next_pos[1] * CELL_SIZE,
                                    self.next_pos[0] * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE)
                                    )
        pygame.draw.rect(
                        self.window,
                        (35, 35, 35),
                        pygame.Rect(
                                    self.next_pos[1] * CELL_SIZE,
                                    self.next_pos[0] * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE), 2
                                    )

    """This function displays the game constantly after checking if the Maze.txt
    is usable by the program. If yes, it filters every event around, and when
    an event is a KEYDOWN type, it calls compute_next_pos() function, and then
    tries to move. It quits the game if the try_to_move() function returns
    False."""
    def play(self):
        running = self.maze.is_maze_usable()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.compute_next_pos(event)
                    running = self.try_to_move(running)

            pygame.display.flip()
