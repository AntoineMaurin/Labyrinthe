import random


class Maze:

    def __init__(self):

        opened_file = open("Maze.txt", 'r')
        self.mazelist = [list(line.strip()) for line in opened_file.readlines()]
        opened_file.close()

        """This list comprehension returns the coordinates of the 'M' element
        in self.mazelist inside a tuple as the first element of a list.
        Then self.current_pos takes the coordinates as a simple tuple
        for an easier use of these coordinates."""

        position = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        self.current_pos = position[0][0], position[0][1]

        guard_pos = [(index, self.mazelist[index].index('O')) for index in range(len(self.mazelist)) if 'O' in self.mazelist[index]]
        self.guard_pos = guard_pos[0][0], guard_pos[0][1]

        self.picked = 0

    def get_objects_pos(self):
        i = 0
        obj_pos = []
        while i < 3:
            obj = random.randint(0, 14), random.randint(0, 14)
            if self.mazelist[obj[0]][obj[1]] is not 'X' and 'M' and 'O' and 'OBJ':
                self.mazelist[obj[0]][obj[1]] = 'OBJ'
                obj_pos.append(obj)
                i += 1
        return obj_pos

    def get_current_pos(self):
        return self.current_pos

    def get_guard_pos(self):
        return self.guard_pos

    def is_wall(self, next_pos):
        if self.mazelist[next_pos[0]][next_pos[1]] == 'X':
            return True
        else:
            return False

    def is_too_far(self, next_pos):
        if next_pos[0] > 14 or next_pos[1] > 14 or next_pos[0] < 0 or next_pos[1] < 0:
            return True
        else:
            return False

    def is_object(self, next_pos):
        if self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ':
            self.picked += 1
            print("picked : ", self.picked)
            return True
        else:
            return False

    def is_guardian(self, next_pos):
        if self.mazelist[next_pos[0]][next_pos[1]] == 'O':
            if self.picked == 3:
                print("picked : ", self.picked)
                print("You win, well played")
            else:
                print("You lose")
                print("picked : ", self.picked)
            return True
        else:
            return False

    def update_mazelist(self, next_pos):
        self.mazelist[self.current_pos[0]][self.current_pos[1]] = '#'
        self.current_pos = next_pos
        self.mazelist[next_pos[0]][next_pos[1]] = 'M'
