import pygame

from poo_class import Maze

my_maze = Maze()

my_maze.add_objects()
my_maze.maze_list = my_maze.get_maze()
my_maze.generate_maze()

running = True

"""Sometimes move_or_quit function returns None, and gets out of the while running loop"""
while running != False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            dico = my_maze.check_key(event)
            running = dico['running']
            pressed_key = dico['pressed_key']
            running = my_maze.move_or_quit(pressed_key)

    pygame.display.flip()
