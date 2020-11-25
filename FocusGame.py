# Author: Dustin Ramsey 
# Date: 11/21/2020
# Description:


class Movement:
    def __init__(self):
        pass

    def correct_piece(self):
        '''
        Validates that the player has selected a valid piece, with the intent to be used as composition
         in the FocusGame class.
        '''

    def legal_move(self):
        '''Validates that the player is making a legal move, intended to be used in composition in '''


class FocusGame:
    def __init__(self, player, color):
        self._Player = (player, color)
        self._reserve = {self._Player[0][0]:['R'],self._Player[1][0]:['G']}
        self._captured = {self._Player[0][0]:[],self._Player[1][0]:[]}
        self._gameboard = [] #contains row, column, set of color stack

        add_color1 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35]
        add_color2 = [0,1,4,5,8,9,12,13,16,17,20,21,24,25,28,29,32,33]

        for i in range(6):
            for x in range(6):
                self._gameboard.append([(i,x)])
        self._half = [i.append([self._Player[1][1]]) for j, i in enumerate(self._gameboard) if j in add_color1]
        self._final = [i.append([self._Player[0][1]]) for j, i in enumerate(self._gameboard) if j in add_color2]
        # Gameboard setup completed
        print(self._gameboard)
        print(self._reserve)

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
        for x in range(len(self._gameboard)):
            if position == self._gameboard[x][0]:
                return self._gameboard[x][1]

    def show_reserve(self, player):
        '''
        Takes a player as a parameter and shows how many pices they have in resesrve
        '''
        if player in self._reserve:
            if self._reserve[player] is None:
                return 0
            else:
                return len(self._reserve[player])

    def show_captured(self, player):
        '''
        Takes a player name as a parameter and shows the number of pieces that player has captured
        '''
        if player in self._captured:
            if self._captured[player] is None:
                return 0
            else:
                return len(self._captured[player])


    def reserved_move(self, player, location):
        '''
        Takes the player name and a location on the board as parameters and places the piece from
        the reserve at that location.
        '''
        try:
            if player in self._reserve.keys() and len(self._reserve[player]) > 0:
                for x in range(len(self._gameboard)):
                    if location == self._gameboard[x][0]:
                        self._gameboard[x][1].append(self._Player[player][1]) and self._reserve[player].pop(1)

        except:
            return 'no pieces in reserve'











game = FocusGame(('PlayerA', 'R'), ('PlayerB','G'))
print(game.show_reserve('PlayerA'))
# game.move_piece('PlayerA',(0,0), (0,1), 1)  #Returns message "successfully moved"
print(game.show_pieces((0,1))) #Returns ['R','R']
# game.show_captured('PlayerA') # Returns 0
print(game.reserved_move('PlayerA', (0,0))) # Returns message "No pieces in reserve"
# game.show_reserve('PlayerA') # Returns 0