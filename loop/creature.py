from random import uniform, randrange, random

import pygame

from entity.creature import Creature
from loop.surface import SurfaceLoop

color_about_to_die = (200, 200, 225)
color_alive = (255, 255, 215)
color_background = (10, 10, 40)
color_grid = (30, 30, 60)
die_age = 20

class CreatureLoop:
    def __init__(self, dimx, dimy, surfaceLoop: SurfaceLoop):
        self.__dimy = dimy
        self.__dimx = dimx
        self.cellsize = 9
        self.__surfaceLoop = surfaceLoop
        self.creatures = [
            Creature(randrange(dimx),randrange(dimy)) for _ in range(int(uniform(15, 30.0)))
        ]
        
    def move(self, last_move):
        movex = randrange(-1, 2)
        movey = randrange(-1, 2)
        if movex == last_move[0] or movey == last_move[1]:
            return movex, movey
        return last_move
    
    def new_child(self, posx, posy):
        child = Creature(posx, posy)
        child.age = 1
        self.creatures.append(child)
        
    def loop(self):
        for creature in self.creatures:
            posx, posy = creature.get_pos()
            movex, movey = self.move(creature.get_last_move())
            new_posx = posx + movex
            new_posy = posy + movey
            if new_posx < 0 or new_posx >= self.__dimx:
                new_posx = posx
                movex = 0
            if new_posy < 0 or new_posy >= self.__dimy:
                new_posy = posy
                movey = 0
            new_cell = self.__surfaceLoop.cells[new_posx][new_posy]
            old_cell = self.__surfaceLoop.cells[posx][posy]
            
            if new_cell.is_tree():
                if not new_cell.chop_wood():
                    continue
            old_cell.make_poo()
            if new_cell.has_food():
                if creature.age > 19:
                    creature.age -= 1
            for c in self.creatures:
                pos = c.get_pos()
                if new_posx == pos[0] and new_posy == pos[1]:
                    if c.can_fuck() and creature.can_fuck():
                        self.new_child(new_posx, new_posy)
            creature.move(movex, movey)
            if creature.age > 20:
                self.creatures.remove(creature)
            

    def draw(self):
        for creature in self.creatures:
            pygame.draw.rect(self.__surfaceLoop.get_surface(), creature.color(), creature.data())    