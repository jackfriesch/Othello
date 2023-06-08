# Author: John Friesch
# GitHub username: frieschj
# Date: 6/5/2023
# Description: Othello game with two classes: Player and Othello. Allows two players to make moves, flipping
# appropriate pieces, calculating valid moves, and checking for a winner.

class Player:
    """Represents a player in an Othello game with a name and piece color"""
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_color(self):
        """Returns the color of a Player object."""
        return self._color

    def get_name(self):
        """Returns the name of a Player object"""
        return self._name


class Othello:
    """Represents a game of Othello. Initializes board, initializes each player's starting available moves, and
    initializes the count of each piece to zero (to be calculated if game ends). Allows players to make moves,
    flipping the appropriate pieces. Calculates each player's available moves after each turn. If a player makes a
    move that ends the game, returns the winner and the number of pieces each player has on the final board. Allows
    user to print the board at any point in the game."""
    def __init__(self):
        self._player_list = []
        self._board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]
        self._valid_w_moves = [(3, 5), (4, 6), (5, 3), (6, 4)]
        self._valid_b_moves = [(3, 4), (4, 3), (5, 6), (6, 5)]
        self._white_pieces = 0
        self._black_pieces = 0

    def create_player(self, player_name, color):
        """Creates a Player object and appends them to the list of players in the Othello class."""
        self._player_list.append(Player(player_name, color))

    def play_game(self, color, piece_position):
        """Checks if a move is valid, if so, calls make_move to make the move. If not valid, returns 'Invalid move' and
        prints the available valid moves for that piece color."""
        # return_winner() not called directly by play_game(). play_game() calls make_move(), which calls flip(),
        # which calls recalc_valid_moves(), which calls return_winner() if the game is ended. So return_winner() is
        # called if a player makes a winning move using play_game(), just not directly by this method.
        if color.lower() == "white":
            if piece_position in self._valid_w_moves:
                return self.make_move(color, piece_position)
            else:
                print(f"Here are the valid moves: {self._valid_w_moves}")
                return "Invalid move"
        if color.lower() == "black":
            if piece_position in self._valid_b_moves:
                return self.make_move(color, piece_position)
            else:
                print(f"Here are the valid moves {self._valid_b_moves}")
                return "Invalid move"

    def make_move(self, color, piece_position):
        """Places a piece of the given color at the given position and calls the flip method"""
        if color.lower() == "white":
            self._board[piece_position[0]][piece_position[1]] = "O"
            return self.flip(color, piece_position)
        if color.lower() == "black":
            self._board[piece_position[0]][piece_position[1]] = "X"
            return self.flip(color, piece_position)

    def flip(self, color, piece_position):
        """Checks which opponent pieces are to be flipped as the result of the made move. Calls flip_pieces."""
        row = piece_position[0]
        column = piece_position[1]
        to_flip = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if color.lower() == "white":
            for rshift, cshift in directions:
                possible_flip = []
                count = 0
                for multiplier in range(1, 9):
                    if 0 < row + (rshift * multiplier) < 9 and 0 < column + (cshift * multiplier) < 9:
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == ".":
                            break
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "X":
                            possible_flip.append((row + (rshift * multiplier), column + (cshift * multiplier)))
                            count += 1
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "O":
                            if count >= 1:
                                for coords in possible_flip:
                                    to_flip.append(coords)
                                break
                            else:
                                break
        if color.lower() == "black":
            for rshift, cshift in directions:
                possible_flip = []
                count = 0
                for multiplier in range(1, 9):
                    if 0 < row + (rshift * multiplier) < 9 and 0 < column + (cshift * multiplier) < 9:
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == ".":
                            break
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "O":
                            possible_flip.append((row + (rshift * multiplier), column + (cshift * multiplier)))
                            count += 1
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "X":
                            if count >= 1:
                                for coords in possible_flip:
                                    to_flip.append(coords)
                                break
                            else:
                                break
        if color.lower() == "white":
            for coords in to_flip:
                self._board[coords[0]][coords[1]] = "O"
        if color.lower() == "black":
            for coords in to_flip:
                self._board[coords[0]][coords[1]] = "X"
        return self.recalc_valid_moves()

    def recalc_valid_moves(self):
        """Clears the list of valid moves and recalculates the valid moves based on the current state of the board. If
        the current move ended the game, the lists of valid moves will be empty for each Player, and calls return_winner
        method. If not the end of the game, returns the current state of the board."""
        self._valid_w_moves = []
        self._valid_b_moves = []
        white_pieces = []
        black_pieces = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for row in range(0, 9):
            for col in range(0, len(self._board[row])):
                if self._board[row][col] == "O":
                    white_pieces.append((row, col))
        for row in range(0, 9):
            for col in range(0, len(self._board[row])):
                if self._board[row][col] == "X":
                    black_pieces.append((row, col))
        for piece in white_pieces:
            row = piece[0]
            column = piece[1]
            for rshift, cshift in directions:
                count = 0
                space_count = 0
                for multiplier in range(1, 9):
                    if 0 < row + (rshift * multiplier) < 9 and 0 < column + (cshift * multiplier) < 9:
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "X":
                            count += 1
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == ".":
                            if count >= 1:
                                self._valid_w_moves.append((row + (rshift * multiplier),
                                                            column + (cshift * multiplier)))
                                space_count += 1
                            else:
                                break
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "." \
                                and space_count >= 1:
                            break
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "O":
                            break
        for piece in black_pieces:
            row = piece[0]
            column = piece[1]
            for rshift, cshift in directions:
                count = 0
                space_count = 0
                for multiplier in range(1, 9):
                    if 0 < row + (rshift * multiplier) < 9 and 0 < column + (cshift * multiplier) < 9:
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "O":
                            count += 1
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == ".":
                            if count >= 1:
                                self._valid_b_moves.append((row + (rshift * multiplier),
                                                            column + (cshift * multiplier)))
                                space_count += 1
                            else:
                                break
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "." \
                                and space_count >= 1:
                            break
                        if self._board[row + (rshift * multiplier)][column + (cshift * multiplier)] == "X":
                            break
        self._valid_w_moves = list(set(self._valid_w_moves))
        self._valid_b_moves = list(set(self._valid_b_moves))
        self._valid_w_moves.sort()
        self._valid_b_moves.sort()
        if len(self._valid_w_moves) == 0 and len(self._valid_b_moves) == 0:
            for row in self._board:
                for element in row:
                    if element == "O":
                        self._white_pieces += 1
                    if element == "X":
                        self._black_pieces += 1
            print(f"Game is ended white piece: {self._white_pieces} black piece: {self._black_pieces}")
            return self.return_winner()
        return self._board

    def return_available_positions(self, color):
        """Returns the sorted list of the valid moves for the given color."""
        if color.lower() == "white":
            return self._valid_w_moves
        if color.lower() == "black":
            return self._valid_b_moves

    def print_board(self):
        """Prints the current state of the game board."""
        for row in self._board:
            print(" ".join(map(str, row)))

    def return_winner(self):
        """Once the game has ended (both player's valid move lists are empty), counts the number of each piece on the
        board. Whichever color has more pieces on the board wins. Returns 'Winner is white/black player: [name of
        white player/black player]'"""
        if self._player_list[0].get_color().lower() == "white":
            white_name = self._player_list[0].get_name()
            black_name = self._player_list[1].get_name()
        else:
            black_name = self._player_list[0].get_name()
            white_name = self._player_list[1].get_name()
        if self._white_pieces > self._black_pieces:
            return "Winner is white player: " + white_name
        if self._white_pieces < self._black_pieces:
            return "Winner is black player: " + black_name
        if self._white_pieces == self._black_pieces:
            return "It's a tie"
