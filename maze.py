import random
import pygame

class Maze:

    def get_maze(self):
        opened_file = open("Maze.txt", 'r')
        mazelist = [list(line.strip()) for line in opened_file.readlines()]
        opened_file.close()
        self.mazelist = Maze.add_objects(self, mazelist)
        return self.mazelist

    def display_maze(self):
        mazelist = self.get_maze()
        for row in mazelist:
            print(row)
        print("\n", "-------------------------------------------------", "\n")

    def add_objects(self, list):
        i = 0
        while i < 3 :
            OBJ = random.randint(1, 13), random.randint(1, 13)
            if (list[OBJ[0]][OBJ[1]] != 'X'):
                list[OBJ[0]][OBJ[1]] = 'OBJ'
                i += 1
        return list
