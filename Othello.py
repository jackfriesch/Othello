# Author: John Friesch
# GitHub username: frieschj
# Date: 
# Description:

class Player:
    def __init__(self, name, color):
        self._name = name
        self._color = color


class Othello:
    def __init__(self):
        self._player_list = []
        self._board = [
                        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                        ["*", ".", ".", ".", ".", ".", ".", ".", "." "*"],
                        ["*", ".", ".", ".", ".", ".", ".", ".", "." "*"],
                        ["*", ".", ".", ".", ".", ".", ".", ".", "." "*"],
                        ["*", ".", ".", ".", "O", "X", ".", ".", "." "*"],
                        ["*", ".", ".", ".", "X", "O", ".", ".", "." "*"],
                        ["*", ".", ".", ".", ".", ".", ".", ".", "." "*"],
                        ["*", ".", ".", ".", ".", ".", ".", ".", "." "*"],
                        ["*", ".", ".", ".", ".", ".", ".", ".", "." "*"],
                        ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
                    ]
        self._valid_w_moves = [(3, 5), (4, 6), (5, 3), (6, 4)]
        self._valid_b_moves = [(3, 4), (4, 3), (5, 6), (6, 5)]

    def create_player(self, player_name, color):
        self._player_list.append(Player(player_name, color))

    def play_game(self, color, piece_position):
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
        if color.lower() == "white":
            self._board[piece_position[0]][piece_position[1]] = "O"
            return self.flip(color, piece_position)
        if color.lower() == "black":
            self._board[piece_position[0]][piece_position[1]] = "X"
            return self.flip(color, piece_position)

    def flip(self, color, piece_position):
        row = piece_position[0]
        column = piece_position[1]
        to_flip = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if color.lower() == "white":
            for x, y in directions:
                possible_flip = []
                count = 0
                for multiplier in range(1, 10):
                    if 0 < row+x*multiplier < 9 and 0 < column+y*multiplier < 9:
                        if self._board[row+x*multiplier][column+y*multiplier] == "X":
                            possible_flip.append((row+x*multiplier, column+y*multiplier))
                            count += 1
                        if self._board[row+x*multiplier][column+y*multiplier] == "O" and count >= 1:
                            for coords in possible_flip:
                                to_flip.append(coords)
            return self.flip_pieces(color, to_flip)
        if color.lower() == "black":
            for x, y in directions:
                possible_flip = []
                count = 0
                for multiplier in range(1, 10):
                    if 0 < row + x * multiplier < 9 and 0 < column + y * multiplier < 9:
                        if self._board[row+x*multiplier][column+y*multiplier] == "O":
                            possible_flip.append((row+x*multiplier, column+y*multiplier))
                            count += 1
                        if self._board[row+x*multiplier][column+y*multiplier] == "X" and count >= 1:
                            for coords in possible_flip:
                                to_flip.append(coords)
            return self.flip_pieces(color, to_flip)

    def flip_pieces(self, color, flip):
        if color.lower() == "white":
            for coords in flip:
                self._board[coords[0]][coords[1]] = "O"
        if color.lower() == "black":
            for coords in flip:
                self._board[coords[0]][coords[1]] = "X"
        return self.recalc_valid_moves()

    def recalc_valid_moves(self):
        self._valid_w_moves = []
        self._valid_b_moves = []
        white_pieces = []
        black_pieces = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for row in range(len(self._board)):
            if "O" in self._board[row]:
                white_pieces.append((row, self._board[row].index("O")))
        for row in range(len(self._board)):
            if "X" in self._board[row]:
                black_pieces.append((row, self._board[row].index("X")))
        for piece in white_pieces:
            row = piece[0]
            column = piece[1]
            for x, y in directions:
                count = 0
                space_count = 0
                for multiplier in range(1, 10):
                    if 0 < row + x * multiplier < 9 and 0 < column + y * multiplier < 9:
                        if self._board[row+x*multiplier][column+y*multiplier] == "X":
                            count += 1
                        if self._board[row+x*multiplier][column+y*multiplier] == "." and count >= 1:
                            self._valid_w_moves.append((row + x * multiplier, column + y * multiplier))
                            space_count += 1
                        if self._board[row+x*multiplier][column+y*multiplier] == "." and space_count >= 1:
                            break
                        if self._board[row + x * multiplier][column + y * multiplier] == "O":
                            break
        for piece in black_pieces:
            row = piece[0]
            column = piece[1]
            for x, y in directions:
                count = 0
                space_count = 0
                for multiplier in range(1, 10):
                    if 0 < row + x * multiplier < 9 and 0 < column + y * multiplier < 9:
                        if self._board[row + x * multiplier][column + y * multiplier] == "O":
                            count += 1
                        if self._board[row + x * multiplier][column + y * multiplier] == "." and count >= 1:
                            self._valid_b_moves.append((row + x * multiplier, column + y * multiplier))
                            space_count += 1
                        if self._board[row+x*multiplier][column+y*multiplier] == "." and space_count >= 1:
                            break
                        if self._board[row+x*multiplier][column+y*multiplier] == "X":
                            break
        self._valid_w_moves = list(set(self._valid_w_moves))
        self._valid_b_moves = list(set(self._valid_b_moves))
        if len(self._valid_w_moves) == 0 and len(self._valid_b_moves) == 0:
            return self.return_winner()
        return self._board

    def return_available_positions(self, color):
        if color.lower() == "white":
            self._valid_w_moves.sort()
            return self._valid_w_moves
        if color.lower() == "black":
            self._valid_b_moves.sort()
            return self._valid_b_moves

    def print_board(self):
        for row in self._board:
            print(" ".join(map(str, row)))

    def return_winner(self):
        white_count = 0
        black_count = 0
        if self._player_list[0].get_color().lower() == "white":
            white_name = self._player_list[0].get_name()
            black_name = self._player_list[1].get_name()
        else:
            black_name = self._player_list[0].get_name()
            white_name = self._player_list[1].get_name()
        for row in self._board:
            for element in row:
                if element == "O":
                    white_count += 1
                if element == "X":
                    black_count += 1
        if white_count > black_count:
            return "Winner is white player: " + white_name
        if white_count < black_count:
            return "Winner is white player: " + black_name
        if white_count == black_count:
            return "It's a tie!"
