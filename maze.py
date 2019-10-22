import random


class Maze:

    def __init__(self):

        maze_file = open("Maze.txt", 'r')
        self.mazelist = [list(line.strip()) for line in maze_file.readlines()]
        maze_file.close()

        # position = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        for index in range(len(self.mazelist)):
            if 'M' in self.mazelist[index]:
                position = (index, self.mazelist[index].index('M'))
        # self.current_pos = position[0][0], position[0][1]
        self.current_pos = position

        # guard_pos = [(index, self.mazelist[index].index('O')) for index in range(len(self.mazelist)) if 'O' in self.mazelist[index]]
        for index in range(len(self.mazelist)):
            if 'O' in self.mazelist[index]:
                guard_pos = (index, self.mazelist[index].index('O'))

        # self.guard_pos = guard_pos[0][0], guard_pos[0][1]
        self.guard_pos = guard_pos

        self.picked = 0

        self.obj_pos = []
        self.set_objects()
        for i in self.mazelist:
            print(i)

    def set_objects(self):
        i = 0
        while i < 3:
            obj = random.randint(0, 14), random.randint(0, 14)
            if self.mazelist[obj[0]][obj[1]] is not 'X':
                if self.mazelist[obj[0]][obj[1]] is not 'OBJ':
                    if obj != self.current_pos:
                        if obj != self.guard_pos:
                            self.mazelist[obj[0]][obj[1]] = 'OBJ'
                            self.obj_pos.append(obj)
                            i += 1

    def get_objects_pos(self):
        return self.obj_pos

    def get_current_pos(self):
        return self.current_pos

    def get_guard_pos(self):
        return self.guard_pos

    def is_wall(self, next_pos):
        try:
            return self.mazelist[next_pos[0]][next_pos[1]] == 'X'
        except IndexError:
            print('Wrong way')
            return True

    def is_too_far(self, next_pos):
        if next_pos[0] > 14 or next_pos[1] > 14:
            return True
        elif next_pos[0] < 0 or next_pos[1] < 0:
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
