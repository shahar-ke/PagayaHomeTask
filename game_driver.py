from colorama import Fore, Style, Back

from game_lib.color_game_board import ColorGameBoard
from game_lib.game_color import GameColor


class ColorGameDriver:
    LEGAL_COLORS = {color.value for color in GameColor}

    def __init__(self, dimensions: int, turns: int):
        self.game_board = ColorGameBoard(dimensions=dimensions, entry_point=(0, 0))
        self.turns = turns

    def play(self):
        turns_left = self.turns
        while turns_left > 0 and not self.game_board.win():
            self.print_board()
            game_color: GameColor = self.get_next_color()
            self.game_board.make_move(game_color)
            turns_left -= 1
        self.print_board()
        if self.game_board.win():
            self.print_win(turns_left)
        else:
            self.print_lose()

    def get_next_color(self) -> GameColor:
        while (user_color := input(f'Pick your next color ({",".join(self.LEGAL_COLORS)})\n')) not in self.LEGAL_COLORS:
            print('That is not a supported color !')
        chosen_color = GameColor(user_color)
        return chosen_color

    def print_board(self):
        for raw in self.game_board.cells:
            cells_colored_raw = ' '.join([str(cell) for cell in raw]) + f' {Style.RESET_ALL}'
            print(cells_colored_raw)
        print()

    def print_win(self, turns_left: int):
        print(f'Congrats, you won within {self.turns - turns_left} moves')

    def print_lose(self):
        print(f'Game Over ! you did not finish within {self.turns} moves, try again ?')


def main():
    game_driver = ColorGameDriver(dimensions=18, turns=21)
    game_driver.play()


if __name__ == '__main__':
    main()
