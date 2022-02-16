from random import random


class Entity:
    def __init__(self):
        self._base_factor: float = random()
        self.__threshold: float = 0.99
        self._base_factor = random()

    def die(self):
        self._base_factor = 0.0

    def is_alive(self):
        return self._base_factor > self.__threshold

    def factor(self):
        return self._base_factor
