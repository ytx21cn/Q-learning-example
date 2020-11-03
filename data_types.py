from enum import IntEnum
from typing import Tuple, Dict, Set

Coordinate = Tuple[int, int]
CoordSet = Set[Coordinate]
GridDict = Dict[Coordinate, float]


class Direction(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class DataTable:
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__rewards: GridDict = {}
        self.__utilities: GridDict = {}
        self.__start: Coordinate = (0, 0)
        self.__terminals: CoordSet = set()

    @property
    def gamma(self):
        return 1.0

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def rewards(self) -> GridDict:
        return self.__rewards

    @property
    def utilities(self) -> GridDict:
        return self.__utilities

    def add_reward(self, coord: Coordinate,
                   reward: float) -> float:
        """
        Add reward data.
        Also set for utility data for that coordinate to 0.
        :param coord: coordinate to add to the grid.
        :param reward: reward value.
        :return: reward value.
        """
        self.rewards[coord] = reward
        self.utilities[coord] = 0
        return reward

    def get_adjacent_reward(self, coord: Coordinate,
                            direction: Direction) -> float:
        if direction == Direction.UP:
            adj_coord = (coord[0], coord[1] - 1)
        elif direction == Direction.DOWN:
            adj_coord = (coord[0], coord[1] + 1)
        elif direction == Direction.LEFT:
            adj_coord = (coord[0] - 1, coord[1])
        else:
            adj_coord = (coord[0] + 1, coord[1])

        reward = self.__rewards.get(adj_coord)
        if reward is None:
            reward = self.__rewards.get(coord)
        if reward is None:
            reward = 0
        return reward

    def set_start(self, coord: Coordinate) -> Coordinate:
        self.__start = coord
        return coord

    @property
    def start(self) -> Coordinate:
        return self.__start

    def add_terminal(self, coord: Coordinate) -> CoordSet:
        assert coord in self.__rewards
        self.__terminals.add(coord)
        return self.__terminals

    @property
    def terminals(self) -> CoordSet:
        return self.__terminals
