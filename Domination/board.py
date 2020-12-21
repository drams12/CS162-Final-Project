# Author: Dustin Ramsey 
# Date: 12/17/2020
# Description: represents the domination board game. Handles rendering itself and
# piece movement and capture.

import pygame as pg
from .constants import *
from .piece import *

class Board:
    '''
    Creates the playing board class that renders the board and handles pieces movement
    '''
    def __init__(self):
        self.board = []
        self.red_captured = self.blue_captured = 0
        self.red_reserve = self.blue_reserve = 0
        self.create_board()
        self.selected = None

    def draw_squares(self, win):
        '''
        draws checkerboard pattern
        '''
        win.fill(LIGHT_GREY)
        for row in range(ROWS):
            for col in range(row % 2, COLUMNS, 2):
                pg.draw.rect(win, MAHOGANY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        for row in range(ROWS):
            for col in range((row + 1) % 2, COLUMNS, 2):
                pg.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        '''
        Places the player's pieces in the correct spots on the board
        '''
        col_evens = [0, 1, 4, 5]
        col_odds = [2,3]
        row_evens =[0, 2, 4]
        row_odds = [1, 3, 5]

        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
                if col in col_evens and row in row_evens:
                    self.board[row].append(Piece(row, col, BLUE))
                elif col in col_odds and row in row_evens:
                    self.board[row].append(Piece(row, col, RED))
                elif col in col_odds and row in row_odds:
                    self.board[row].append(Piece(row, col, BLUE))
                else:
                    self.board[row].append(Piece(row, col, RED))


    def draw(self, win):
        '''
        draws the checkerboard pattern and the pieces on the board
        '''
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLUMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        if piece.color == self.turn:
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def get_valid_moves(self, piece):
        moves = {}
        # left = piece.col - 1
        # right = piece.col + 1
        # up = piece.row - 1
        # down = piece.row + 1
        row = piece.row
        col = piece.col
        pieces = 0
        for piece in (row, col):
            pieces += piece


        moves.update(self.move_left(row, col))
        moves.update(self.move_right(row, col))
        moves.update(self.move_up(col, row))
        moves.update(self.move_down(col, row))
        return moves

    def move_left(self, row, col):
        moves = {}
        pieces = 0
        for piece in (row, col):
            pieces += piece
            if col < 0 or col > 5:
                 return moves
            if pieces == 0:
                return moves
            else:
                moves.update(self.move_left(row, col - pieces))
                pieces -= 1


    def move_right(self, row, col):
        moves = {}
        pieces = 0
        for piece in (row, col):
            pieces += piece
            if col > 5 or col < 0:
                return moves
            if pieces == 0:
                return moves
            else:
                moves.update(self.move_right(row, col + pieces))
                pieces -= 1

    def move_up(self, col, row):
        moves = {}
        pieces = 0
        for piece in (row, col):
            pieces += piece
            if row < 0 or row > 5:
                return moves
            if pieces == 0:
                return moves
            else:
                moves.update(self.move_up(col, row - pieces))
                pieces -= 1

    def move_down(self, col, row):
        moves = {}
        pieces = 0
        for piece in (row, col):
            pieces += piece
            if row > 5 or row < 0:
                return moves
            if pieces == 0:
                return moves
            else:
                moves.update(self.move_down(col, row + pieces))
                pieces -= 1
