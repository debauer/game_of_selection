from random import randrange

from ursina import Entity

from config.config import Config
from util.types import Position


class Creature(Entity):
    def __init__(self) -> None:
        self.last_move = Position(0, 0, 0)
        self.speed: float = 5.0
        self.age = float(randrange(13))
        Entity.__init__(self)

    def color(self):
        a = self.age * 10
        if a > 255:
            a = 255
        return (a, 0, 0)

    def is_hungy(self):
        return self.age > Config.creature_get_hungry

    def get_last_move(self) -> Position:
        return self.__last_move

    def can_fuck(self) -> bool:
        return self.age > 18.0

    def data(self):
        return (
            self.__position.x * self.__cellsize,
            self.__position.y * self.__cellsize,
            self.__cellsize - 1,
            self.__cellsize - 1,
        )
