from random import randrange

from entity.entity import Entity


class Creature(Entity):
    def __init__(self, posx, posy, cellsize=9):
        self.__posy = posy
        self.__posx = posx
        self.__cellsize = cellsize
        self.__last_move = (0,0)
        self.age = float(randrange(13))
        Entity.__init__(self)
        
    def color(self):
        a = self.age * 10
        if a > 255:
            a = 255
        return (a, 0, 0)

    def move(self, movx, movy):
        self.age += 0.5
        self.__posy += movy
        self.__posx += movx
        self.__last_move = (movx,movy)
    
    def get_last_move(self):
        return self.__last_move

    def can_fuck(self):
        return self.age > 18.0

    def get_pos(self):
        return (self.__posx, self.__posy)
    
    def data(self):
        return (
            self.__posx * self.__cellsize,
            self.__posy * self.__cellsize,
            self.__cellsize - 1,
            self.__cellsize - 1,
        )