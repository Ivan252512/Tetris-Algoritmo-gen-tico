from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import tetris
from PIL import Image, ImageFilter
import screenshot
from operator import itemgetter

import play
import time
import copy


# load model
block_model = load_model('image/block_mnist.h5py')

O = lambda inv_cell_pos : tetris.O(inv_cell_pos)
I = lambda inv_cell_pos : tetris.I(inv_cell_pos)
Z = lambda inv_cell_pos : tetris.Z(inv_cell_pos)
S = lambda inv_cell_pos : tetris.S(inv_cell_pos)
L = lambda inv_cell_pos : tetris.L(inv_cell_pos)
J = lambda inv_cell_pos : tetris.J(inv_cell_pos)
T = lambda inv_cell_pos : tetris.T(inv_cell_pos)



def get_prediction(path_image):
    im = [plt.imread(path_image)]
    X = np.array(im, dtype=np.uint8)
    return block_model.predict(X)


def get_block_type(prediction):
    tipos = [I, J, L, O, S, T, Z]
    predicciones = []
    for i in range(len(prediction[0])):
        predicciones.append([prediction[0][i], tipos[i]])
    
    for i in predicciones:
        a = i
        for j in predicciones:
            if float(j[0])>=float(a[0]):
                a = j
    print(a)
    return a[1]


def block_representative_pixels(block_pos1d, imagen):
    all_board_block_pos2d = []
    for p in block_pos1d:
        block_pos2dx = []
        for i in range(7):
            block_pos2dy = []
            for j in range(7):
                block_pos2dy.append([im for im in imagen[p[1]+(i-4)][p[0]+(j-4)]])
            block_pos2dx.append(block_pos2dy)
        all_board_block_pos2d.append(block_pos2dx)      
    return np.array(all_board_block_pos2d)

def image_to_board(image):  
    width = int(263/10)
    length = int(485/19)

    posx = 0
    posy = 0

    block_pos = []

    while posx+width<=263:
        posx += width - 1
        while posy+length<=485:
            posy += length -1
            block_pos.append([posx-int(width/2), posy-int(length/2)])
        posy = 0

    image_array = block_representative_pixels(block_pos, np.array(image))

    conty = 0
    contx = 0
    board = np.zeros((20, 10))
    for i in image_array:
        if np.average(i)>90:
            board[conty][contx] = 2
        conty+=1
        if conty>19:
            conty = 0
            contx+=1
        if contx>9:
            contx = 0

    return tetris.Tetris(preload_board=board)

def crop_block(image_path, new_size, save_path, contour=True):
    image = Image.open(image_path)
    im = image.crop(new_size)
    if contour:
        im = im.filter(ImageFilter.CONTOUR)
    im.save(save_path)
    return im


while True:
    screenshot.screenshot(5)

    crop_board = crop_block("image/realtime_screenshot/screenshot.png", (821, 200, 1084, 685), "image/realtime_screenshot/board/screenshot.png",contour=False)
    crop_block("image/realtime_screenshot/screenshot.png", (1175, 235, 1275, 335), "image/realtime_screenshot/block/screenshot.png")

    tetris_board = image_to_board(crop_board)
    block = get_block_type(get_prediction("image/realtime_screenshot/block/screenshot.png"))(np.array([1, 5])) 



    moves = tetris_board.valid_moves
    rotates = tetris_board.valid_rotates


    score = tetris_board.moment_score()

    for i in rotates:
        for j in moves:
            tetris_board_copy = copy.copy(tetris_board)
            block_copy = copy.copy(block)
            play.move(tetris_board_copy, block_copy, j, i)

            print(tetris_board_copy.moment_score())

    while tetris_board.move_down(block):
        pass

