import numpy as np

class Tetris:
    def __init__(self, length=19, width=10):
        self.board = np.zeros((length, width))

    def O(self):
        O = np.ones((2, 2))
        return O

    def I(self):
        I = np.ones((1, 4))
        return I

    def Z(self):
        Z = np.ones((2, 3))
        Z[1][0] = 0
        Z[0][2] = 0
        return Z

    def S(self):
        S = np.ones((2, 3))
        S[0][0] = 0
        S[1][2] = 0
        return S

    def L(self):
        L = np.ones((2, 3))
        L[0][0] = 0
        L[0][1] = 0
        return L

    def J(self):
        J = np.ones((2, 3))
        J[0][1] = 0
        J[0][2] = 0
        return J

    def T(self):
        T = np.ones((2, 3))
        T[0][0] = 0
        T[0][2] = 0
        return T

    def run_game(self, block, pos_x0=6, pos_y0=0):
        for i in self.board:
            print(i)