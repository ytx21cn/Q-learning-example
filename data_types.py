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
        self.rewards: GridDict = {}
        self.utilities: GridDict = {}
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
        self.utilities[coord] = reward
        return reward

    def __get_adjacent_coord(self, coord: Coordinate,
                             direction: Direction) -> Coordinate:
        """
        Get adjacent coordinate.
        Bounce back to current coordinate if there is no actual grid at the adjacent direction.
        :param coord: Original coordinate.
        :param direction: One direction to adjacent grid.
        :return: Adjacent grid, or current grid if adjacent grid does not exist.
        """
        if direction == Direction.UP:
            adj_coord = (coord[0], coord[1] - 1)
        elif direction == Direction.DOWN:
            adj_coord = (coord[0], coord[1] + 1)
        elif direction == Direction.LEFT:
            adj_coord = (coord[0] - 1, coord[1])
        else:
            adj_coord = (coord[0] + 1, coord[1])

        if adj_coord not in self.rewards:
            return coord
        else:
            return adj_coord

    def get_adjacent_reward(self, coord: Coordinate,
                            direction: Direction) -> float:
        adj_coord = self.__get_adjacent_coord(coord, direction)
        reward = self.rewards.get(adj_coord, 0)
        return reward

    def get_adjacent_utility(self, coord: Coordinate,
                             direction: Direction) -> float:
        adj_coord = self.__get_adjacent_coord(coord, direction)
        utility = self.utilities.get(adj_coord, 0)
        return utility

    def set_start(self, coord: Coordinate) -> Coordinate:
        self.__start = coord
        return coord

    @property
    def start(self) -> Coordinate:
        return self.__start

    def add_terminal(self, coord: Coordinate) -> CoordSet:
        assert coord in self.rewards
        self.__terminals.add(coord)
        return self.__terminals

    @property
    def terminals(self) -> CoordSet:
        return self.__terminals
