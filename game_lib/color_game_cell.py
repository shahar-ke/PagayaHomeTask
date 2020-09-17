import random

from colorama import Back

from game_lib.game_color import GameColor


class ColorGameCell:
    COLOR_MAP = {
        GameColor.RED: Back.RED,
        GameColor.BLUE: Back.BLUE,
        GameColor.YELLOW: Back.YELLOW,
        GameColor.GREEN: Back.GREEN
    }

    def __init__(self, raw, col):
        self.raw = raw
        self.col = col
        self.color: GameColor = random.choice(list(GameColor))

    def __str__(self):
        return self.COLOR_MAP[self.color]
