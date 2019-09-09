import tetris
import piezas

t = tetris.Tetris()

piezas = [piezas.O, piezas.I, piezas.Z, piezas.S, piezas.L, piezas.J, piezas.T]

for i in piezas:
    t.move_block(i, [1, 5])