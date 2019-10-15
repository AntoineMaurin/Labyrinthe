import pygame

from game import Game

my_game = Game()

# my_game.generate_maze()
my_game.draw_empty_maze()
my_game.draw_character()
my_game.draw_guardian()
my_game.draw_objects()

my_game.play()
