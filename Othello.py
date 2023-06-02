# Author: John Friesch
# GitHub username: frieschj
# Date: 
# Description:

class Player:
    def __init__(self, name, color):
        self._name = name
        self._color = color

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name


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
        self._valid_w_moves = [(5, 3), (3, 5), (4, 6), (6, 4)]
        self._valid_b_moves = [(4, 3), (3, 4), (6, 5), (5, 6)]

    def create_player(self, player_name, color):
        self._player_list.append(Player(player_name, color))

    def make_move(self, color, piece_position):
        if color.lower() == "white":
            move_made = piece_position
            self._board[piece_position[0]][piece_position[1]] = "O"
            return self.flip_up(color, piece_position, [], 0, move_made)
        if color.lower() == "black":
            move_made = piece_position
            self._board[piece_position[0]][piece_position[1]] = "X"
            return self.flip_up(color, piece_position, [], 0, move_made)

    def flip_up(self, color, piece_position, up_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0] - 1][piece_position[1]] == "X":
                count += 1
                up_list.append((piece_position[0] - 1, piece_position[1]))
                return self.flip_up(color, (piece_position[0] - 1, piece_position[1]), up_list, count, move_made)
            if self._board[piece_position[0] - 1][piece_position[1]] == "O" and count >= 1:
                for coords in up_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_down(color, move_made, [], 0, move_made)
            else:
                return self.flip_down(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0] - 1][piece_position[1]] == "O":
                count += 1
                up_list.append((piece_position[0] - 1, piece_position[1]))
                return self.flip_up(color, (piece_position[0] - 1, piece_position[1]), up_list, count, move_made)
            if self._board[piece_position[0] - 1][piece_position[1]] == "X" and count >= 1:
                for coords in up_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_down(color, move_made, [], 0, move_made)
            else:
                return self.flip_down(color, move_made, [], 0, move_made)

    def flip_down(self, color, piece_position, down_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0] + 1][piece_position[1]] == "X":
                count += 1
                down_list.append((piece_position[0] + 1, piece_position[1]))
                return self.flip_down(color, (piece_position[0] + 1, piece_position[1]), down_list, count, move_made)
            if self._board[piece_position[0] + 1][piece_position[1]] == "O" and count >= 1:
                for coords in down_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_right(color, move_made, [], 0, move_made)
            else:
                return self.flip_right(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0] + 1][piece_position[1]] == "O":
                count += 1
                down_list.append((piece_position[0] + 1, piece_position[1]))
                return self.flip_down(color, (piece_position[0] + 1, piece_position[1]), down_list, count, move_made)
            if self._board[piece_position[0] + 1][piece_position[1]] == "X" and count >= 1:
                for coords in down_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_right(color, move_made, [], 0, move_made)
            else:
                return self.flip_right(color, move_made, [], 0, move_made)

    def flip_right(self, color, piece_position, right_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0]][piece_position[1] + 1] == "X":
                count += 1
                right_list.append((piece_position[0], piece_position[1] + 1))
                return self.flip_right(color, (piece_position[0], piece_position[1] + 1), right_list, count, move_made)
            if self._board[piece_position[0]][piece_position[1] + 1] == "O" and count >= 1:
                for coords in right_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_left(color, move_made, [], 0, move_made)
            else:
                return self.flip_left(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0]][piece_position[1] + 1] == "O":
                count += 1
                right_list.append((piece_position[0], piece_position[1] + 1))
                return self.flip_right(color, (piece_position[0], piece_position[1] + 1), right_list, count, move_made)
            if self._board[piece_position[0]][piece_position[1] + 1] == "X" and count >= 1:
                for coords in right_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_left(color, move_made, [], 0, move_made)
            else:
                return self.flip_left(color, move_made, [], 0, move_made)

    def flip_left(self, color, piece_position, left_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0]][piece_position[1] - 1] == "X":
                count += 1
                left_list.append((piece_position[0], piece_position[1] - 1))
                return self.flip_left(color, (piece_position[0], piece_position[1] - 1), left_list, count, move_made)
            if self._board[piece_position[0]][piece_position[1] - 1] == "O" and count >= 1:
                for coords in left_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_upleft(color, move_made, [], 0, move_made)
            else:
                return self.flip_upleft(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0]][piece_position[1] - 1] == "O":
                count += 1
                left_list.append((piece_position[0], piece_position[1] - 1))
                return self.flip_left(color, (piece_position[0], piece_position[1] - 1), left_list, count, move_made)
            if self._board[piece_position[0]][piece_position[1] - 1] == "X" and count >= 1:
                for coords in left_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_upleft(color, move_made, [], 0, move_made)
            else:
                return self.flip_upleft(color, move_made, [], 0, move_made)

    def flip_upleft(self, color, piece_position, upleft_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0] - 1][piece_position[1] - 1] == "X":
                count += 1
                upleft_list.append((piece_position[0] - 1, piece_position[1] - 1))
                return self.flip_upleft(color, (piece_position[0] - 1, piece_position[1] - 1), upleft_list, count,
                                        move_made)
            if self._board[piece_position[0] - 1][piece_position[1] - 1] == "O" and count >= 1:
                for coords in upleft_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_upright(color, move_made, [], 0, move_made)
            else:
                return self.flip_upright(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0] - 1][piece_position[1] - 1] == "O":
                count += 1
                upleft_list.append((piece_position[0] - 1, piece_position[1] - 1))
                return self.flip_upleft(color, (piece_position[0] - 1, piece_position[1] - 1), upleft_list, count,
                                        move_made)
            if self._board[piece_position[0] - 1][piece_position[1] - 1] == "X" and count >= 1:
                for coords in upleft_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_upright(color, move_made, [], 0, move_made)
            else:
                return self.flip_upright(color, move_made, [], 0, move_made)

    def flip_upright(self, color, piece_position, upright_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0] - 1][piece_position[1] + 1] == "X":
                count += 1
                upright_list.append((piece_position[0] - 1, piece_position[1] + 1))
                return self.flip_upright(color, (piece_position[0] - 1, piece_position[1] + 1), upright_list, count,
                                         move_made)
            if self._board[piece_position[0] - 1][piece_position[1] + 1] == "O" and count >= 1:
                for coords in upright_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_downright(color, move_made, [], 0, move_made)
            else:
                return self.flip_downright(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0] - 1][piece_position[1] + 1] == "O":
                count += 1
                upright_list.append((piece_position[0] - 1, piece_position[1] + 1))
                return self.flip_upright(color, (piece_position[0] - 1, piece_position[1] + 1), upright_list, count,
                                         move_made)
            if self._board[piece_position[0] - 1][piece_position[1] + 1] == "X" and count >= 1:
                for coords in upright_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_downright(color, move_made, [], 0, move_made)
            else:
                return self.flip_downright(color, move_made, [], 0, move_made)

    def flip_downright(self, color, piece_position, downright_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0] + 1][piece_position[1] + 1] == "X":
                count += 1
                downright_list.append((piece_position[0] + 1, piece_position[1] + 1))
                return self.flip_downright(color, (piece_position[0] + 1, piece_position[1] + 1), downright_list, count,
                                           move_made)
            if self._board[piece_position[0] + 1][piece_position[1] + 1] == "O" and count >= 1:
                for coords in downright_list:
                    self._board[coords[0]][coords[1]] = "O"
                return self.flip_downleft(color, move_made, [], 0, move_made)
            else:
                return self.flip_downleft(color, move_made, [], 0, move_made)
        if color.lower() == "black":
            if self._board[piece_position[0] + 1][piece_position[1] + 1] == "O":
                count += 1
                downright_list.append((piece_position[0] + 1, piece_position[1] + 1))
                return self.flip_downright(color, (piece_position[0] + 1, piece_position[1] + 1), downright_list, count,
                                           move_made)
            if self._board[piece_position[0] + 1][piece_position[1] + 1] == "X" and count >= 1:
                for coords in downright_list:
                    self._board[coords[0]][coords[1]] = "X"
                return self.flip_downleft(color, move_made, [], 0, move_made)
            else:
                return self.flip_downleft(color, move_made, [], 0, move_made)

    def flip_downleft(self, color, piece_position, downleft_list, count, move_made):
        if color.lower() == "white":
            if self._board[piece_position[0] + 1][piece_position[1] - 1] == "X":
                count += 1
                downleft_list.append((piece_position[0] + 1, piece_position[1] - 1))
                return self.flip_downleft(color, (piece_position[0] + 1, piece_position[1] - 1), downleft_list, count,
                                          move_made)
            if self._board[piece_position[0] + 1][piece_position[1] - 1] == "O" and count >= 1:
                for coords in downleft_list:
                    self._board[coords[0]][coords[1]] = "O"
        if color.lower() == "black":
            if self._board[piece_position[0] + 1][piece_position[1] - 1] == "O":
                count += 1
                downleft_list.append((piece_position[0] + 1, piece_position[1] - 1))
                return self.flip_downleft(color, (piece_position[0] + 1, piece_position[1] - 1), downleft_list, count,
                                          move_made)
            if self._board[piece_position[0] + 1][piece_position[1] - 1] == "X" and count >= 1:
                for coords in downleft_list:
                    self._board[coords[0]][coords[1]] = "X"
        return self._board

    def play_game(self, color, piece_position):
        if color.lower() == "white":
            if piece_position in self._valid_w_moves:
                return self.make_move(color, piece_position)
            else:
                print(f"Invalid move. Here are the valid moves: {self._valid_w_moves}")
        if color.lower() == "black":
            if piece_position in self._valid_b_moves:
                return self.make_move(color, piece_position)
            else:
                print(f"Invalid move. Here are the valid moves: {self._valid_b_moves}")

    def return_available_positions(self, color):
        if color.lower() == "white":
            self._valid_w_moves.sort()
            return self._valid_w_moves
        if color.lower() == "black":
            self._valid_b_moves.sort()
            return self._valid_b_moves

    def print_board(self):
        for row in self._board:
            for column in row:
                print(column, " ", end="")
            print("")

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
                if element == "O ":
                    white_count += 1
                if element == "X ":
                    black_count += 1
        if white_count > black_count:
            return "Winner is white player: " + white_name
        if white_count < black_count:
            return "Winner is white player: " + black_name

