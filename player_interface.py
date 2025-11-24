import random
from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self):
        self.moves: list[tuple[int, int]] = []
        self.position: tuple[int, int] = (0, 0)
        self.path: list[tuple[int, int]] = [self.position]

    def make_move(self) -> tuple[int, int]:
        move: tuple[int, int] = random.choice(self.moves)
        self.position = (move[0] + self.position[0], move[1] + self.position[1])
        self.path.append(self.position)

        return self.position

    @abstractmethod
    def level_up(self) -> None:
        pass


class Pawn(Player):

    def __init__(self):
        super().__init__()
        self.moves: list[tuple[int, int]] = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self) -> None:
        self.moves.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
