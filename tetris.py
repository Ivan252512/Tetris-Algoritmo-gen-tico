import numpy as np

class Block:
    def __init__(self):
        self.form = np.zeros((1,1))
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        raise NotImplementedError

class O(Block):
    def __init__(self):
        self.form = np.ones((2, 2))

    def rotate(self):
        pass

class I(Block):
    def __init__(self):
        self.form = np.ones((1, 4))
        self.invariant_point = np.array([0, 2])

    def rotate(self):
        self.form = np.ones((4, 1))
        self.invariant_point = np.array([2, 0])

class Z(Block):
    def __init__(self):
        Z = np.ones((3, 3))
        Z[1][0] = 0
        Z[0][2] = 0
        Z[2] = np.zeros((1,3))
        self.form = Z

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class S(Block):
    def __init__(self):
        S = np.ones((3, 3))
        S[0][0] = 0
        S[1][2] = 0
        S[2] = np.zeros((1,3))
        self.form = S

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class L(Block):
    def __init__(self):
        L = np.ones((3, 3))
        L[0][0] = 0
        L[0][1] = 0
        L[2] = np.zeros((1,3))
        self.form = L

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class J(Block):
    def __init__(self):
        J = np.ones((3, 3))
        J[0][1] = 0
        J[0][2] = 0
        L[2] = np.zeros((1,3))
        self.form = J

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class T(Block):
    def __init__(self):
        T = np.ones((3, 3))
        T[0][0] = 0
        T[0][2] = 0
        T[2] = np.zeros((1,3))
        self.form = T

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))


class Tetris:
    def __init__(self, length=19+3, width=10):
        self.board = np.zeros((length, width))

    def put_block(self):
        for i in self.board:
            for j in i:
                if j==1:
                    j=2

    def block_position_on_board(self, block, invariant_point_board_pos):
        blockcell_board_pos = (lambda board_pos, block_cell_pos, invariant_cell_pos : 
                                board_pos - (block_cell_pos - invariant_cell_pos))

        all_cell_pos = np.zeros(block.form.shape)

        for i in block:
            for j in i:
                all_cell_pos.append(blockcell_board_pos())


    def validate_move(self, block, pos):
        pass

    def natural_move_down(self, block, pos):
        pass

    def run_game(self, block, pos_x0=6):
        for i in self.board:
            for k in block:
                pass
                