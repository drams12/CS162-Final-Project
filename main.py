# Author: Dustin Ramsey 
# Date: 12/17/2020
# Description: file to render the game

import pygame as pg
from Domination.constants import *
from Domination.board import *
from Domination.constants import *
from Domination.game import *

FPS = 60

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Domination')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pg.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)



        game.update()

    pg.quit()

main()