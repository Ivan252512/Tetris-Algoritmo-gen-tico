import numpy as np

class Block:
    def __init__(self, inv_cell_pos):
        self.inv_cell_pos = inv_cell_pos

    def rotate(self):
        raise NotImplementedError

class O(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        self.form = np.ones((2, 2))
        self.invariant_point = np.array([0, 0])

    def rotate(self):
        pass

class I(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        self.form = np.ones((1, 4))
        self.invariant_point = np.array([0, 2])

    def rotate(self):
        self.form = np.ones((4, 1))
        self.invariant_point = np.array([2, 0])

class Z(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        Z = np.ones((3, 3))
        Z[1][0] = 0
        Z[0][2] = 0
        Z[2] = np.zeros((1,3))
        self.form = Z
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class S(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        S = np.ones((3, 3))
        S[0][0] = 0
        S[1][2] = 0
        S[2] = np.zeros((1,3))
        self.form = S
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class L(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        L = np.ones((3, 3))
        L[0][0] = 0
        L[0][1] = 0
        L[2] = np.zeros((1,3))
        self.form = L
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class J(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        J = np.ones((3, 3))
        J[0][1] = 0
        J[0][2] = 0
        J[2] = np.zeros((1,3))
        self.form = J
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))

class T(Block):
    def __init__(self, inv_cell_pos):
        Block.__init__(self, inv_cell_pos)
        T = np.ones((3, 3))
        T[0][0] = 0
        T[0][2] = 0
        T[2] = np.zeros((1,3))
        self.form = T
        self.invariant_point = np.array([1, 1])

    def rotate(self):
        self.form = np.rot90(self.form, 1, (1,0))


class Tetris:
    def __init__(self, length=20+3+1, width=10+2, preload_board=np.zeros((1, 1))):
        board = np.zeros((length, width))
        for i in board:
            i[0]=5
            i[len(i)-1] = 3
        board[len(board)-1] = np.array([4 for i in range(width)])
        if not np.array_equal(np.zeros((1, 1)), preload_board):
            for i in range(len(preload_board[0])):
                for j in range(len(preload_board)):
                    board[j+3][i+1] = preload_board[j][i]
        self.board = board
        #self.valid_moves = np.array([[1, 0]])
        self.valid_moves = np.array([[0,0], [0,-1], [0, 1], [1, 0]])
        self.score = 0

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

    def valid_move(self, block, invariant_point_board_pos):
        len_x = len(block.form)
        len_y = len(block.form[0])

        for i in range(len_x):
            for j in range(len_y):
                x, y = (np.array(invariant_point_board_pos) + 
                        (np.array([i, j]) - np.array(block.invariant_point)))

                #Condición para garantizar movimientos validos
                if block.form[i][j]!=0 and (self.board[x][y]==2 or self.board[x][y]==4 or self.board[x][y]==5 or self.board[x][y]==3):
                    return False

        return True

    def block_position_on_board(self, block, invariant_point_board_pos):
        all_cell_pos = np.zeros(block.form.shape, dtype=object)

        len_x = len(block.form)
        len_y = len(block.form[0])

        for i in range(len_x):
            for j in range(len_y):
                x, y = (np.array(invariant_point_board_pos) + 
                        (np.array([i, j]) - np.array(block.invariant_point)))

                all_cell_pos[i][j] = np.array([x, y, int(block.form[i][j])])

        return all_cell_pos

    def move_down(self, block):
        block.inv_cell_pos = block.inv_cell_pos + np.array([1, 0])
        if not self.valid_move(block, block.inv_cell_pos):
            self.set_block()
            self.clean_to_next_position()
            return False
        self.block_position_on_board(block, block.inv_cell_pos)
        all_cell_pos = self.block_position_on_board(block, block.inv_cell_pos)
        self.clean_to_next_position()
        self.update_board(all_cell_pos)
        return True

    def move(self, block, move):
        block.inv_cell_pos = block.inv_cell_pos + move
        if not self.valid_move(block, block.inv_cell_pos):
            block.inv_cell_pos = block.inv_cell_pos - move
        self.block_position_on_board(block, block.inv_cell_pos)
        all_cell_pos = self.block_position_on_board(block, block.inv_cell_pos)
        self.clean_to_next_position()
        self.update_board(all_cell_pos)
    
    def game_over(self):
        for i in self.board[2]:
            if i==2:
                return True
        return False

    def update_score(self):
        len_i, len_j = self.board.shape
        for i in range(len_i):
            update = True
            for j in range(len_j):
                if self.board[i][j] != 2:
                    update = False
            if update:
                self.score += 10
                
    def destroy_row(self, row):
        if row==1:
            return
        for i in len(range(self.board[0])):
            self.board[row][i] = self.board[row-1][i]
        return self.destroy_row(row-1)