from random import randint
from time import sleep
import os

def clear():
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear') 

class Board:

    def __init__(self, width = 70, height = 20, thresh = 65):
        self.threshold = thresh
        self.width = width
        self.height = height
        self.gameBoard = [[1 if randint(1,100) > self.threshold else 0 for  i in range(self.width)]
                                              for j in range(self.height)]

    def __str__(self):
        st = ''
        for i in range(self.height):
            for j in range(self.width):
                st += '#' if self.gameBoard[i][j] else '_'
            st += '\n'
        return st

    def update(self):
        self.gameBoard = Board.nextState(self.gameBoard)

    def setBoard(self,board):
        self.gameBoard = board
        self.width = len(board[0])
        self.height = len(board)

    @staticmethod
    def neighbourCount(board,r,c):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (0 <= i+r < len(board)) and (0 <= j+c < len(board[0])) and not(i == 0 and j == 0):
                    if board[i+r][j+c] == 1:
                        count+=1
        return count

    @staticmethod
    def nextState(board):
        newBoard = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                temp = Board.neighbourCount(board,i,j)
                if temp < 2 or temp > 3:
                    newBoard[i][j] = 0
                elif temp == 3:
                    newBoard[i][j] = 1
                else:
                    newBoard[i][j] = board[i][j]
        return newBoard

def test(ans,exp):
    for i in range(len(exp)):
        for j in range(len(exp[0])):
            if ans[i][j] != exp[i][j]:
                return False
    return True


life = Board(10,10)
#life.setBoard([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
while 1:
    clear()
    print(life)
    life.update()
    sleep(0.25)
x = input('Press Enter to exit')
