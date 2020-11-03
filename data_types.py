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
        self.__reward_data: GridDict = {}
        self.__utility_data: GridDict = {}
        self.__start: Coordinate = (0, 0)
        self.__terminals: CoordSet = set()

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def reward_data(self) -> GridDict:
        return self.__reward_data

    @property
    def utility_data(self) -> GridDict:
        return self.__utility_data

    def add_reward(self, coord: Coordinate,
                   reward: float) -> float:
        self.reward_data[coord] = reward
        return reward

    def set_start(self, coord: Coordinate) -> Coordinate:
        self.__start = coord
        return coord

    @property
    def start(self) -> Coordinate:
        return self.__start

    def add_terminal(self, coord: Coordinate) -> CoordSet:
        self.__terminals.add(coord)
        return self.__terminals

    @property
    def terminals(self) -> CoordSet:
        return self.__terminals
