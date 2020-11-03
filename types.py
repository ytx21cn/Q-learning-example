from typing import Tuple, Dict, Union

Coordinate = Tuple[int, int]
Value = Union[float, None]
GridDict = Dict[Coordinate, float]


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
