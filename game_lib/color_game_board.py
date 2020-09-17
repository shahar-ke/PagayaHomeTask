from typing import Tuple, List, Set

from game_lib.color_game_cell import ColorGameCell
from game_lib.game_color import GameColor


class ColorGameBoard:
    DIMENSIONS_LIMIT = 3

    def __init__(self, dimensions: int, entry_point: Tuple[int, int]):
        assert dimensions >= self.DIMENSIONS_LIMIT, f"please set dimensions larger than {self.DIMENSIONS_LIMIT}"
        for entry_item in entry_point:
            assert entry_item >= 0 < dimensions, 'entry point outside of dimensions'
        self.cells: List[List[ColorGameCell]] = [[ColorGameCell(raw, col) for col in range(dimensions)]
                                                 for raw in range(dimensions)]
        self.entry_point = entry_point
        self.dimensions = dimensions

    def win(self) -> bool:
        base_color = self._get_entry_cell().color
        for raw in range(len(self.cells)):
            for col in range(len(self.cells[raw])):
                if base_color != self.cells[raw][col].color:
                    return False
        return True

    def make_move(self, move_color: GameColor):
        entry_cell = self._get_entry_cell()
        if entry_cell.color == move_color:
            return
        entry_color = entry_cell.color
        stack: List[Tuple[int, int]] = [(entry_cell.raw, entry_cell.col)]
        visited: Set[ColorGameCell] = set()
        while stack:
            cur_raw, cur_col = stack.pop()
            if cur_raw < 0 or cur_raw >= self.dimensions or cur_col < 0 or cur_col >= self.dimensions:
                continue
            cur_cell = self.cells[cur_raw][cur_col]
            if cur_cell in visited:
                continue
            visited.add(cur_cell)
            if cur_cell.color != entry_color:
                continue
            cur_cell.color = move_color
            stack.extend(
                [(cur_raw - 1, cur_col), (cur_raw + 1, cur_col), (cur_raw, cur_col - 1), (cur_raw, cur_col + 1)])

    def _get_entry_cell(self) -> ColorGameCell:
        return self.cells[self.entry_point[0]][self.entry_point[1]]
