# Author: Dustin Ramsey 
# Date: 12/17/2020
# Description: Handles the game. Turns, piece selection, move validation, etc.

import pygame as pg
from .constants import *
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pg.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        if self.selected and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pg.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + (SQUARE_SIZE // 2)), (row * SQUARE_SIZE + (SQUARE_SIZE // 2)), 15)

    def change_turn(self):
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE
