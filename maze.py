import random

"""This class manages the maze itself and is mainly used to exchange data with
the Game class."""


class Maze:

    """Reads the Maze.txt file to make a list of lists from every line in it,
    then checks if the file is usable for the program.
    It initializes some attributes used later and then calls the function
    set_objects()"""
    def __init__(self):

        maze_file = open("Maze.txt", 'r')
        self.mazelist = [list(line.strip()) for line in maze_file.readlines()]
        maze_file.close()

        self.height = len(self.mazelist)
        self.width = len(self.mazelist[0])


        # position = [(index, self.mazelist[index].index('M')) for index in range(len(self.mazelist)) if 'M' in self.mazelist[index]]
        # self.current_pos = position[0][0], position[0][1]

        self.current_pos = self.where_is('M')

        # guard_pos = [(index, self.mazelist[index].index('O')) for index in range(len(self.mazelist)) if 'O' in self.mazelist[index]]
        # self.guard_pos = guard_pos[0][0], guard_pos[0][1]
        self.guard_pos = self.where_is('G')

        self.picked = 0
        self.obj_pos = []
        self.set_objects()

    """This function returns True if the maze is usable, by calling four cheking
    methods."""
    def is_maze_usable(self):
        if (self.check_maze_length()):
            return True
        if (self.is_pure()):
            return True
        if (self.is_once('M')):
            return True
        if (self.is_once('G')):
            return True
        else:
            return False

    """This function checks if all the lines in the maze are the same lenght.
    It's a problem if they're not because the size of the window is calculated
    with the lenght of the first line, and I also want my maze to be a
    square."""
    def check_maze_length(self):
        state = True
        for index, elt in enumerate(self.mazelist):
            if (len(elt)) != len(self.mazelist[index - 1]):
                state = False
        return state

    """This function checks if there is not other string in the maze than
    'M', 'G', '#', 'X' or 'OBJ'."""
    def is_pure(self):
        state = True
        for row in self.mazelist:
            for cell in row:
                if cell not in ('M', 'G', '#', 'X', 'OBJ'):
                    state = False
        return state

    """This function checks if a certain letter in the maze is in it only
    once."""
    def is_once(self, letter):
        counter = 0
        for index in range(len(self.mazelist)):
            if letter in self.mazelist[index]:
                counter += 1
        return counter == 1

    """This function returns a tuple of coordinates that tells where the letter
    in parameter is."""
    def where_is(self, letter):
        for index in range(len(self.mazelist)):
            if letter in self.mazelist[index]:
                return (index, self.mazelist[index].index(letter))

    """This function puts the string 'OBJ' in the mazelist at three random
    free places."""
    def set_objects(self):
        i = 0
        while i < 3:
            obj = random.randint(0, 14), random.randint(0, 14)
            if self.mazelist[obj[0]][obj[1]] != 'X':
                if self.mazelist[obj[0]][obj[1]] != 'OBJ':
                    if obj != self.current_pos:
                        if obj != self.guard_pos:
                            self.mazelist[obj[0]][obj[1]] = 'OBJ'
                            self.obj_pos.append(obj)
                            i += 1

    """This function returns the attribute obj_pos."""
    def get_objects_pos(self):
        return self.obj_pos

    """This function returns the attribute current_pos."""
    def get_current_pos(self):
        return self.current_pos

    """This function returns the attribute guard_pos."""
    def get_guard_pos(self):
        return self.guard_pos

    """This function checks if the next_pos given in parameter is on the limits
    of the maze or not."""
    def is_too_far(self, next_pos):
        if next_pos[0] > self.width - 1 or next_pos[1] > self.height - 1:
            return True
        elif next_pos[0] < 0 or next_pos[1] < 0:
            return True
        else:
            return False

    """This function checks if the next_pos given in parameter is a wall
    or not."""
    def is_wall(self, next_pos):
        return self.mazelist[next_pos[0]][next_pos[1]] == 'X'

    """This function checks if the next_pos given in parameter is the guardian
    positon or not."""
    def is_guardian(self, next_pos):
        if self.mazelist[next_pos[0]][next_pos[1]] == 'G':
            if self.picked == 3:
                print("picked : ", self.picked)
                print("You win, well played")
            else:
                print("You lose")
                print("picked : ", self.picked)
            return True
        else:
            return False

    """This function checks if the next_pos given in parameter is an object
    positon or not."""
    def is_object(self, next_pos):
        if self.mazelist[next_pos[0]][next_pos[1]] == 'OBJ':
            self.picked += 1
            print("picked : ", self.picked)
            return True
        else:
            return False

    """This function updates the mazelist by erasing the 'M' string at the
    current position and writing it at the next position. It also sets the
    current position equal to the next position to start the next move
    from here."""
    def update_macgyver(self, next_pos):
        self.mazelist[self.current_pos[0]][self.current_pos[1]] = '#'
        self.current_pos = next_pos
        self.mazelist[next_pos[0]][next_pos[1]] = 'M'
