# Author: Dustin Ramsey 
# Date: 12/17/2020
# Description:

from .constants import *
import pygame as pg

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.reserve = False

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_reserve(self):
        self.reserve = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pg.draw.circle(win, LIGHT_GREY, (self.x, self.y), radius + self.OUTLINE)
        pg.draw.circle(win, self.color, (self.x, self.y), radius)

    def __repr__(self):
        '''
        object representation
        '''
        return str(self.color)