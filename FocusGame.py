# Author: Dustin Ramsey 
# Date: 11/27/2020
# Description: Program to play the game Focus/ Domination.
# Contains a class FocusGame that initializes the players with their color, dictionaries for reserved and
# captured pieces, a counter to keep track of the player's turn, and the gameboard.
#
# Methods include move_piece, show_pieces, show_reserve, show_capture, reserve_move, move_helper, more_than_five,
# get_player_color, check_piece, and get_gameboard. get_gameboard is just used for testing purposes to view the
# current state of the board.
#
#Rules for the Game:
# On a player’s turn they will make one move. They can either make a single move, a multiple move, or a reserve move.
#
# Single Move
# In a single move the player moves one of their playing pieces which is on a space by itself. This piece can be
# moved one space vertically or horizontally. The piece may never be moved diagonally. The piece can either be
# moved to an empty space, or a space with one or more playing pieces on it. If a piece is moved to a space with a
# stack of pieces on it, the piece that was just moved is placed on the top of the stack. A player can move their
# playing piece onto a stack containing their own pieces, pieces of other players, or both.
#
# Multiple Move
# In a multiple move a player can move a whole stack of pieces. A player may only move a stack if their pawn is on
# top of the stack. When a player wants to move a stack they choose how much of the stack that they want to move.
# They can either move the entire stack or take some pieces off the top of the stack and leave some of the playing
# pieces behind. The player will then be able to move the stack a number of spaces up to the height of the stack
# they are moving. They can move the stack vertically or horizontally but not diagonally. When moving a stack it will
# only impact the pieces on the space that that stack lands on and won’t impact the pieces on the spaces that the
# stack was moved through.

# Reserving and Capturing Pieces
# After moving your playing piece/stack you need to check the height of the stack that you moved the piece(s) to. If
# the new stack ever contains more than five pieces some of the pieces will be removed from the stack. Starting with
# the playing piece on the bottom of the stack, you will remove pieces until the stack only has five pieces remaining.
# The pieces that were removed from the board will either be captured or put into reserve. All pieces not belonging
# to the player who made the move are captured. These pieces are removed and won’t be used for the rest of the game.
# Pieces belonging to the player who made the move will be added to their reserve pile.

# Reserve Move
# If a player has playing pieces in reserve they can make a reserve move instead of a single or multiple move. To
# make a reserve move take one of your playing pieces in reserve and place it on any space on the gameboard. The
# reserve piece can be placed on an empty space, on a space containing one piece, or a space containing multiple
# pieces. Placing the reserve piece counts as your turn as you don’t get to move the piece you just added to the
# gameboard.

# End of the Game
# The first player who captures six pieces of the other player wins the game


class FocusGame:
    ''' '''
    def __init__(self, player, color):
        self._Player = (player, color)
        self._reserve = {self._Player[0][0]:['R', 'R', 'R','R'],self._Player[1][0]:['G','G', 'G']}
        self._captured = {self._Player[0][0]:['G','G'],self._Player[1][0]:[]}
        self._gameboard = [] #contains list of lists in format:  [(row, column), [color stack]]
        self._count = 1
        add_color1 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35]
        add_color2 = [0,1,4,5,8,9,12,13,16,17,20,21,24,25,28,29,32,33]

        for i in range(6):
            for x in range(6):
                self._gameboard.append([(i,x)])
        self._half = [i.append([self._Player[1][1]]) for j, i in enumerate(self._gameboard) if j in add_color1]
                    # adds the second player's color to the board for indices in list
        self._final = [i.append([self._Player[0][1]]) for j, i in enumerate(self._gameboard) if j in add_color2]
                    # adds the first player's color to the board for indices in list
                    # Gameboard setup completed

    def move_piece(self, player, start, end, pieces):
        '''
        Takes the player making the move, a tuple representing the starting location, another tuple representing the
        target location, and an integer representing the number of pieces that are being moved as parameters.

        An error is return in the event that it is not the player's turn, the locations are invalid, or the number
        of pieces being moved are invalid.

        If the resulting number of pieces is greater than 5, the bottom piece(s) is captured if it belongs to the
        opponent or if the player's piece, it is placed in reserve.

        Returns successfully moved if move successful and winning message if player makes winning move.
        '''
        try:
            if (self._count % 2 == 0 and player == self._Player[0][0]) or (self._count % 2 != 0 and player == self._Player[1][0]):
                return False        # if the count doesn't match then it is not that player's turn
            if self.get_player_color(player) is self.check_piece(start):                # verify player dominates starting location
                if (start[0] == end[0] and pieces == abs(start[1] - end[1])) or\
                        ((start[1] == end[1]) and pieces == abs(start[0] - end[0])):    # makes sure that pieces can only be played in straight line and number of pieces is correct for distance
                    for num1 in range(len(self._gameboard)):
                        if end == self._gameboard[num1][0]:
                            self._gameboard[num1][1].extend(self.move_helper(start, pieces))    # adds moved pieces to new location
                            self._count += 1
                            if len(self._gameboard[num1][1]) > 5:
                                self.more_than_five(player, end)                            # check for stack too large
                            if self.show_captured(player) > 5:
                                return str(player) + " Wins"                                # check for win
                            else:
                                return 'successfully moved'
                    for num2 in range(len(self._gameboard)):
                        if start == self._gameboard[num2][0]:
                            for i in range(pieces):
                                del self._gameboard[num2][1][-1]                            # remove moved pieces from start
        except:
            return False

    def more_than_five(self, player, end):
        '''
        Takes as a parameter the player and the ending location of their move. This method
        checks to see if the ending location has surpassed the 5 piece limit. If so it pops
        off bottom pieces and places pieces in reserve or captured depending on the player.
        '''
        color = self.get_player_color(player)
        for num1 in range(len(self._gameboard)):
            if end == self._gameboard[num1][0]:
                while len(self._gameboard[num1][1]) > 5:
                    if self._gameboard[num1][1][0] == color:
                        self._reserve[player].append(self._gameboard[num1][1][0])           # put piece in reserve if color matches
                        self._gameboard[num1][1].pop(0)                                     # remove bottom piece
                    else:
                        self._captured[player].append(self._gameboard[num1][1][0])          # else put piece in captured
                        self._gameboard[num1][1].pop(0)                                     #remove bottom piece

    def move_helper(self, start, pieces):
        '''
        Method that takes the player, a starting and ending position, and the number of pieces as parameters. It
        is used to move pieces and make alterations to the sets containing them on the gameboard. It will be used in
        the main move_piece method
        '''
        stack_start = []
        for num in range(len(self._gameboard)):
            if start == self._gameboard[num][0]:
                i = 0
                while i < pieces:
                    stack_start.extend(self._gameboard[num][1][-i]) # places the specified number of pieces from the top into a new list
                    i += 1
                return stack_start

    def get_player_color(self, player):
        '''
        Method that returns the color assigned to the given player
        '''
        for num in range(len(self._Player)):
            if player in self._Player[num]:
                return self._Player[num][1]

    def check_piece(self, position):
        '''
        Takes a position on the board and returns the top piece in order to check if the player dominates it
        '''
        for num in range(len(self._gameboard)):
            if position == self._gameboard[num][0]:
                return self._gameboard[num][1][-1]

    def show_pieces(self, position):
        '''
        Takes a position on the board and returns a list showing pieces at that location
        '''
        for num in range(len(self._gameboard)):
            if position == self._gameboard[num][0]:
                return self._gameboard[num][1]

    def show_reserve(self, player):
        '''
        Takes a player as a parameter and returns an integer representing how many pieces they have in reserve
        '''
        if player in self._reserve:
            if self._reserve[player] is None:
                return 0
            else:
                return len(self._reserve[player])

    def show_captured(self, player):
        '''
        Takes a player name as a parameter and returns an integer representing how many pieces that
        player has captured.
        '''
        if player in self._captured:
            if self._captured[player] is None:
                return 0
            else:
                return len(self._captured[player])


    def reserved_move(self, player, location):
        '''
        Takes the player name and a location on the board as parameters and places the piece from
        the reserve at that location. Uses more than five method if stacks become too large and
        checks for winner as well.
        '''
        color = self.get_player_color(player)
        try:
            if player in self._reserve.keys() and len(self._reserve[player]) > 0:
                for num in range(len(self._gameboard)):
                    if location == self._gameboard[num][0]:
                        self._reserve[player].pop(0) and self._gameboard[num][1].append(color)  # take piece from reserve and place on board
                    if len(self._gameboard[num][1]) > 5:
                        self.more_than_five(player, location)           # check for stack too large
                    if self.show_captured(player) > 5:
                        return str(player) + " Wins"                    # check for win
        except:
            return False
        else:
            return 'successfully moved'

    def get_gameboard(self):
        '''
        Returns the current state of the gameboard
        '''
        return self._gameboard







#
# game = FocusGame(('PlayerA', 'R'), ('PlayerB','G'))
# print(game.get_gameboard())
#
# print(game.show_reserve('PlayerA'))
# print(game.reserved_move('PlayerB', (0,0))) # Returns message "No pieces in reserve"
# print(game.reserved_move('PlayerA', (0,0)))
# print(game.reserved_move('PlayerA', (0,0)))
# print(game.reserved_move('PlayerA', (0,0)))
# print(game.reserved_move('PlayerA', (0,0)))
# print(game.reserved_move('PlayerA', (0,0)))
# print(game.get_gameboard())
# print(game.check_piece((0,0)))
# print(game.move_piece('PlayerA',(0,0), (0,1), 1)) #Returns message "successfully moved"
# print(game.get_gameboard())
# print(game.more_than_five(("PlayerA"),(0,0)))
# print(game.get_gameboard())
# print(game.show_captured('PlayerA'))