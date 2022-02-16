from random import randrange

from config.config import Config
from entity.entity import Entity
from util.types import Position


class Creature(Entity):
    def __init__(self, pos: Position) -> None:
        self.__position = pos
        self.__cellsize = Config.cellsize
        self.__last_move = Position(0, 0)
        self.__speed: float = 5.0
        self.age = float(randrange(13))
        Entity.__init__(self)

    def color(self):
        a = self.age * 10
        if a > 255:
            a = 255
        return (a, 0, 0)

    def move(self, movx, movy):
        self.age += Config.creature_age_rate
        self.__position = Position(self.__position.x + movx, self.__position.y + movy)
        self.__last_move = Position(movx, movy)

    def is_hungy(self):
        return self.age > Config.creature_get_hungry

    def get_last_move(self) -> Position:
        return self.__last_move

    def can_fuck(self) -> bool:
        return self.age > 18.0

    def get_pos(self) -> Position:
        return Position(self.__position.x, self.__position.y)

    def data(self):
        return (
            self.__position.x * self.__cellsize,
            self.__position.y * self.__cellsize,
            self.__cellsize - 1,
            self.__cellsize - 1,
        )
