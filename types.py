from enum import IntEnum
from typing import Tuple, Dict

Coordinate = Tuple[int, int]
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
