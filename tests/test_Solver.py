import sys
sys.path.append(r"C:/Users/ipova/repos/sudoku")
from Environment import Environment

def generate_board1():
    e = Environment()
    e.set(5,1,1)
    e.set(9,4,6)
    e.set(7,9,1)
    e.set(3,5,5)
    e.render_board()

def test_board1():
    generate_board1()