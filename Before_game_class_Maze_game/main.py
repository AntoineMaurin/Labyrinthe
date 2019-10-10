import pygame

from maze import Maze

my_maze = Maze()

my_maze.add_objects()
my_maze.maze_list = my_maze.get_maze()
my_maze.generate_maze()

my_maze.display_maze()

running = True

"""Sometimes move function returns None, and gets out of the while running loop"""
while running != False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            next_pos = my_maze.set_position(event)
            running = my_maze.move(next_pos)

    pygame.display.flip()
