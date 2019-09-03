import numpy as np

class Block:
    def __init__(self):
        self.form = np.zeros((1,1))

    def left_rotate(self):
        raise NotImplementedError
    
    def right_rotate(self):
        raise NotImplementedError

class O(Block):
    def __init__(self):
        self.form = np.ones((2, 2))

    def left_rotate(self):
        pass
    
    def right_rotate(self):
        pass

class Z(Block):
    def __init__(self):
        Z = np.ones((2, 3))
        Z[1][0] = 0
        Z[0][2] = 0
        self.form = Z

    def left_rotate(self):
        raise NotImplementedError
    
    def right_rotate(self):
        raise NotImplementedError

class S(Block):
    def __init__(self):
        S = np.ones((2, 3))
        S[0][0] = 0
        S[1][2] = 0
        self.form = S

    def left_rotate(self):
        raise NotImplementedError
    
    def right_rotate(self):
        raise NotImplementedError

class L(Block):
    def __init__(self):
        L = np.ones((2, 3))
        L[0][0] = 0
        L[0][1] = 0
        self.form = L

    def left_rotate(self):
        raise NotImplementedError
    
    def right_rotate(self):
        raise NotImplementedError

class J(Block):
    def __init__(self):
        J = np.ones((2, 3))
        J[0][1] = 0
        J[0][2] = 0
        self.form = J

    def left_rotate(self):
        raise NotImplementedError
    
    def right_rotate(self):
        raise NotImplementedError

class T(Block):
    def __init__(self):
        T = np.ones((2, 3))
        T[0][0] = 0
        T[0][2] = 0
        self.form = T

    def left_rotate(self):
        raise NotImplementedError
    
    def right_rotate(self):
        raise NotImplementedError

class Tetris:
    def __init__(self, length=19, width=10):
        self.board = np.zeros((length, width))

    def put_block(self):
        for i in self.board:
            for j in i:
                if j==1:
                    j=2

    def validate_move(self, block, pos_x, pos_y):
        for i in block:
            for j in i:
                if self.board[pos_x][pos_y]!=2:
                    pass

    def natural_move_down(self, block, pos_x0, pos_y0):
        pass

    def run_game(self, block, pos_x0=6, pos_y0=0):
        for i in self.board:
            for k in block:
                pass
                