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
        self.selected_piece = None
        self.red_captured = self.blue_captured = 0
        self.red_reserve = self.blue_reserve = 0
        self.create_board()

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