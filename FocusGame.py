# Author: Dustin Ramsey 
# Date: 11/27/2020
# Description:



class FocusGame:
    ''' '''
    def __init__(self, player, color):
        self._Player = (player, color)
        self._reserve = {self._Player[0][0]:['R', 'R', 'R','R'],self._Player[1][0]:['G','G', 'G']}
        self._captured = {self._Player[0][0]:['G','G'],self._Player[1][0]:[]}
        self._gameboard = [] #contains row, column, set of color stack
        self._count = 1
        add_color1 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35]
        add_color2 = [0,1,4,5,8,9,12,13,16,17,20,21,24,25,28,29,32,33]

        for i in range(6):
            for x in range(6):
                self._gameboard.append([(i,x)])
        self._half = [i.append([self._Player[1][1]]) for j, i in enumerate(self._gameboard) if j in add_color1]
        self._final = [i.append([self._Player[0][1]]) for j, i in enumerate(self._gameboard) if j in add_color2]
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
                return False
            if self.get_player_color(player) is self.check_piece(start):
                if (start[0] == end[0] and pieces == abs(start[1] - end[1])) or\
                        ((start[1] == end[1]) and pieces == abs(start[0] - end[0])):
                    for num1 in range(len(self._gameboard)):
                        if end == self._gameboard[num1][0]:
                            self._gameboard[num1][1].extend(self.move_helper(start, pieces))
                            self._count += 1
                            if len(self._gameboard[num1][1]) > 5:
                                self.more_than_five(player, end)
                            if self.show_captured(player) > 5:
                                return str(player) + " Wins"
                    for num2 in range(len(self._gameboard)):
                        if start == self._gameboard[num2][0]:
                            for i in range(pieces):
                                del self._gameboard[num2][1][-1]
        except:
            return False
        else:
            return 'successfully moved'

    def win(self, player):
        '''
        Method that takes a player's name and checks for whether a player has 5 pieces in captured
        and declares a winnerif so.
        '''
        if self.show_captured(player) > 5:
            return str(player) + " Wins"

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
                        self._reserve[player].append(self._gameboard[num1][1][0])
                        self._gameboard[num1][1].pop(0)
                    else:
                        self._captured[player].append(self._gameboard[num1][1][0])
                        self._gameboard[num1][1].pop(0)

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
                    stack_start.extend(self._gameboard[num][1][-i])
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
        Takes a player as a parameter and shows how many pieces they have in reserve
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
        the reserve at that location. Uses more than five method if stacks become too large and
        checks for winner as well.
        '''
        color = self.get_player_color(player)
        try:
            if player in self._reserve.keys() and len(self._reserve[player]) > 0:
                for num in range(len(self._gameboard)):
                    if location == self._gameboard[num][0]:
                        self._reserve[player].pop(0) and self._gameboard[num][1].append(color)
                    if len(self._gameboard[num][1]) > 5:
                        self.more_than_five(player, location)
                    if self.show_captured(player) > 5:
                        return str(player) + " Wins"
        except:
            return False
        else:
            return 'successfully moved'

    def get_gameboard(self):
        '''
        Returns the current state of the gameboard
        '''
        return self._gameboard








game = FocusGame(('PlayerA', 'R'), ('PlayerB','G'))
print(game.get_gameboard())

print(game.show_reserve('PlayerA'))
print(game.reserved_move('PlayerB', (0,0))) # Returns message "No pieces in reserve"
print(game.reserved_move('PlayerA', (0,0)))
print(game.reserved_move('PlayerA', (0,0)))
print(game.reserved_move('PlayerA', (0,0)))
print(game.reserved_move('PlayerA', (0,0)))
print(game.reserved_move('PlayerA', (0,0)))
print(game.get_gameboard())
print(game.check_piece((0,0)))
print(game.move_piece('PlayerA',(0,0), (0,1), 3)) #Returns message "successfully moved"
print(game.get_gameboard())
print(game.more_than_five(("PlayerA"),(0,0)))
print(game.get_gameboard())
print(game.show_captured('PlayerA'))