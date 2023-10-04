import numpy as np

class Environment:

    def __init__(self):
        # Create a 9x9 matrix with all elements as 0
        self.board = np.zeros((9, 9), dtype=int)
    
    def set(self,value,row,col):
        # update the value at row, col location
        self.board[row-1][col-1] = value

    def render_board(self):

        print()
        # Print the Sudoku board
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=' ')
                if (j + 1) % 3 == 0 and j < 8:
                    print("|", end=' ')
            print()
            if (i + 1) % 3 == 0 and i < 8:
                print("-" * 21)
        print()

# e = Environment()
# e.set(5,1,1)
# e.set(9,4,6)
# e.set(7,9,1)
# e.set(3,5,5)
# e.render_board()