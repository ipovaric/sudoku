import numpy as np

class Environment:
    def __init__(self, board):
        self.board

    def render_board():
        # Create a 9x9 matrix with all elements as 0
        board = [[1 for _ in range(9)] for _ in range(9)]

        # Print the Sudoku board
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
                if (j + 1) % 3 == 0 and j < 8:
                    print("|", end=' ')
            print()
            if (i + 1) % 3 == 0 and i < 8:
                print("-" * 21)

e = Environment
e.render_board()