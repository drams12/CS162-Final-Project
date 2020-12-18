# Author: Dustin Ramsey 
# Date: 12/17/2020
# Description: file to render the game

import pygame as pg
from Domination.constants import *
from Domination.board import *

FPS = 60

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Domination')


def main():
    run = True
    clock = pg.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        pg.display.update()

    pg.quit()

main()