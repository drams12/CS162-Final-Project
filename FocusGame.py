# Author: Dustin Ramsey 
# Date: 11/21/2020
# Description:

class FocusGame:
    def __init__(self, player, color):
        self._Player = (player, color)

        self._gameboard = []
        add_color1 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35]
        add_color2 = [0,1,4,5,8,9,12,13,16,17,20,21,24,25,28,29,32,33]

        for i in range(6):
            for x in range(6):
                self._gameboard.append([x,i])
        self._half = [i.append([self._Player[1][1]]) for j, i in enumerate(self._gameboard) if j in add_color1]
        self._final = [i.append([self._Player[0][1]]) for j, i in enumerate(self._gameboard) if j in add_color2]

        print(self._gameboard)

    def move_piece(self, player, start, end, pieces):
        '''
        Takes the player making the move, a tuple representing the starting location, another tuple representing the
        target location, and an integer representing the number of pieces that are being moved as parameters.

        An error is return in the event that it is not the player's turn, the locations are invalid, or the number
        of pieces being moved are invalid.

        If the resulting number of pieces is greater than 5 the bottom piece(s) is captured if it belongs to the
        opponent or if the player's piece it is placed in reserve.

        Returns successfully moved if move successful and winning message if player makes winning move.
        '''


    def show_pieces(self, position):
        '''
        Takes a position on the board and returns a list showing pieces at that location
        '''


    def show_reserve(self, player):
        '''
        Takes a player as a parameter and shows how many pices they have in resesrve
        '''


    def show_captured(self, player):
        '''
        Takes a player name as a parameter and shows the number of pieces that player has captured
        '''


    def reserved_move(self, player, location):
        '''
        Takes the player name and a location on the board as parameters and places the piece from
        the reserve at that location.
        '''













game = FocusGame(('PlayerA', 'R'), ('PlayerB','G'))
# game.move_piece('PlayerA',(0,0), (0,1), 1)  #Returns message "successfully moved"
# game.show_pieces((0,1)) #Returns ['R','R']
# game.show_captured('PlayerA') # Returns 0
# game.reserved_move('PlayerA', (0,0)) # Returns message "No pieces in reserve"
# game.show_reserve('PlayerA') # Returns 0