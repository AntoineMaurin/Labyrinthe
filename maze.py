import random


class Maze:

    def __init__(self):
        self.mazelist = []

    def get_maze(self):
        opened_file = open("Maze.txt", 'r')
        mazelist = [list(line.strip()) for line in opened_file.readlines()]
        opened_file.close()
        self.mazelist = Maze.add_objects(self, mazelist)
        return self.mazelist

    def add_objects(self, list):
        i = 0
        while i < 3:
            obj = random.randint(0, 14), random.randint(0, 14)
            if list[obj[0]][obj[1]] != 'X' and 'M' and 'O':
                list[obj[0]][obj[1]] = 'OBJ'
                i += 1
        return list

    # def display_maze(self):
    #     mazelist = self.get_maze()
    #     for row in mazelist:
    #         print(row)
    #     print("\n", "------------------------------------------------", "\n")
