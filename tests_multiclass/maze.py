class Maze:

    def __init__(self):
        pass

    def get_list(self):
        self.list = ['oui', 'non', 45]
        return self.list

    def display(self):
        print('JE DISPLAY INCROYABLE')
        a = Maze.get_list(Maze)
        print(a)
