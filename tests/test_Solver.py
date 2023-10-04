import sys
sys.path.append(r"C:/Users/ipova/repos/sudoku")
from Environment import Environment

def generate_board1():
    e = Environment()
    # assign values, columns, and rows of example board
    values = [5,2,4,7,6,5,9,5,6,2,3,2,5,7,8,1,8,7,
              9,2,3,2,5,3,8,9,6,8,9,1,7,1,6,5,3,4]
    rows = [1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,
            5,5,5,6,6,6,6,6,7,7,7,7,8,8,8,8,9,9]
    cols = [3,4,1,5,7,8,2,5,6,7,4,5,7,8,9,1,2,3,
            7,8,9,1,2,3,5,6,3,4,5,8,2,3,5,9,6,7]
    # generate example board using a zipped loop
    for (value,row,col) in zip(values,rows,cols):
        e.set(value,row,col)
    e.render_board()

def test_board1():
    generate_board1()

test_board1()