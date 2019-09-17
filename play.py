import tetris
import random
import time
import numpy as np

O = lambda inv_cell_pos : tetris.O(inv_cell_pos)
I = lambda inv_cell_pos : tetris.I(inv_cell_pos)
Z = lambda inv_cell_pos : tetris.Z(inv_cell_pos)
S = lambda inv_cell_pos : tetris.S(inv_cell_pos)
L = lambda inv_cell_pos : tetris.L(inv_cell_pos)
J = lambda inv_cell_pos : tetris.J(inv_cell_pos)
T = lambda inv_cell_pos : tetris.T(inv_cell_pos)


blocks = [O, I, Z, S, L, J, T]

def randomBlock(blocks_letter, inv_cell_pos):
    rand = random.randint(0, len(blocks_letter)-1)
    return blocks_letter[rand](inv_cell_pos)

def move(tetris_board, block, moves, rotates):
    for i in range(rotates):
        block.rotate()
        
    for i in moves:
        tetris_board.move(block, i)





