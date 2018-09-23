from random import randint

class Board:

    def __init__(self, thresh = 95, width = 70, height = 20):
        self.threshold = thresh
        self.width = width
        self.height = height
        self.gameBoard = [[1 if randint(1,100) > self.threshold else 0 for  i in range(self.width)]
                                              for j in range(self.height)]

    def __str__(self):
        st = ''
        for i in range(self.height):
            for j in range(self.width):
                st += '#' if self.gameBoard[i][j] else ' '
            st += '\n'
        return st

life = Board()
print(life)
