import numpy as np
import threading
import time

class Block:
    def __init__(self):
        self.form = np.zeros((1,1))

    def rotate(self):
        raise NotImplementedError

class O(Block):
    def __init__(self):
        self.form = np.ones((2, 2))
        self.invariant_point = np.array([0, 0])

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
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class S(Block):
    def __init__(self):
        S = np.ones((3, 3))
        S[0][0] = 0
        S[1][2] = 0
        S[2] = np.zeros((1,3))
        self.form = S
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class L(Block):
    def __init__(self):
        L = np.ones((3, 3))
        L[0][0] = 0
        L[0][1] = 0
        L[2] = np.zeros((1,3))
        self.form = L
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class J(Block):
    def __init__(self):
        J = np.ones((3, 3))
        J[0][1] = 0
        J[0][2] = 0
        J[2] = np.zeros((1,3))
        self.form = J
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class T(Block):
    def __init__(self):
        T = np.ones((3, 3))
        T[0][0] = 0
        T[0][2] = 0
        T[2] = np.zeros((1,3))
        self.form = T
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))


class Tetris:
    def __init__(self, length=19+3+1, width=10+2):
        board = np.zeros((length, width))
        for i in board:
            i[0]=3
            i[len(i)-1] = 3
        board[len(board)-1] = np.array([4 for i in range(width)])
        self.board = board
        self.valid_moves = np.array([[0,0], [0,-1], [1, 0], [-1, 0]])

    def block_position_on_board(self, block, invariant_point_board_pos):
        all_cell_pos = np.zeros(block.form.shape, dtype=object)

        len_x = len(block.form)
        len_y = len(block.form[0])

        for i in range(len_x):
            for j in range(len_y):
                x, y = (np.array(invariant_point_board_pos) + 
                       (np.array([i, j]) - np.array(block.invariant_point)))

                if block.form[i][j]!=0 and self.board[x][y]==3:
                    all_cell_pos[i][j] = np.array([x, y, int(block.form[i][j])])

                #Condición para garantizar movimientos validos
                if block.form[i][j]!=0 and (self.board[x][y]==2 or self.board[x][y]==4):
                    return np.array([-1,-1])
            
                all_cell_pos[i][j] = np.array([x, y, int(block.form[i][j])])

        return all_cell_pos

    def move_block(self, block, invariant_cell_block_position):
        all_cell_pos = self.block_position_on_board(block, invariant_cell_block_position)

        if np.array_equal(all_cell_pos, np.array([0,-1])):
            pass

        if np.array_equal(all_cell_pos, np.array([-1,-1])):
            self.set_block()
            self.clean_to_next_position()
            print(self.board)
            return 
            
        else:
            self.clean_to_next_position()
            self.update_board(all_cell_pos)
            print(self.board)
            self.move_block(block, invariant_cell_block_position + np.array([1, 1]))

    def clean_to_next_position(self):
        len_i, len_j = self.board.shape
        for i in range(len_i):
            for j in range(len_j):
                if self.board[i][j] == 1:
                    self.board[i][j] = 0

    def update_board(self, all_cell_pos):
        for i in all_cell_pos:
            for j in i:
                if self.board[j[0]][j[1]] == 0:
                    self.board[j[0]][j[1]] = j[2]
    
    def set_block(self):
        len_i, len_j = self.board.shape
        for i in range(len_i):
            for j in range(len_j):
                if self.board[i][j] == 1:
                    self.board[i][j] = 2


