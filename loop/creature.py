import time
from random import randrange, random, choice

import pygame

from config.config import Config
from entity.creature import Creature
from loop.surface import SurfaceLoop
from util.time import now
from util.types import Position, Dimension


class CreatureLoop:
    def __init__(self, dim: Dimension, surfaceLoop: SurfaceLoop):
        self.__dim = dim
        self.__surfaceLoop = surfaceLoop
        self.__killed = 0
        self.__new_born = 0
        self.__died = 0
        self.__last_print = now()
        self.creatures = [
            Creature(Position(randrange(dim.x), randrange(dim.y)))
            for _ in range(Config.creature_count)
        ]

    def move(self, last_move) -> Position:
        movex = randrange(-1, 2)
        movey = randrange(-1, 2)
        if movex == last_move[0] or movey == last_move[1]:
            return Position(movex, movey)
        return Position(0, 0)

    def new_child(self, pos: Position):
        child = Creature(pos)
        child.age = 1
        self.creatures.append(child)

    def print_stats(self):
        if (now() - self.__last_print).total_seconds() > 1:
            self.__last_print = now()
            print(len(self.creatures), self.__killed, self.__died, self.__new_born)
        
    def look_for_food(self, pos: Position):
        return Position(0,0)

    def loop(self):
        self.print_stats()
        for creature in self.creatures:
            move = self.move(creature.get_last_move())
            pos = creature.get_pos()
            if creature.is_hungy():
                move = self.look_for_food(pos)
                

            
            
            if move.x == 0 and move.y == 0:
                continue
            new_pos = Position(
                self.__dim.x-1 if pos.x + move.x < 0 else pos.x + move.x, 
                self.__dim.y-1 if pos.y + move.y < 0 else pos.y + move.y
            )
            new_pos = Position(
                0 if new_pos.x >= self.__dim.x else new_pos.x, 
                0 if new_pos.y >= self.__dim.y else new_pos.y
            )
            move = Position(new_pos.x-pos.x, new_pos.y-pos.y)
            # get cells
            new_cell = self.__surfaceLoop.cells[new_pos.x][new_pos.y]
            old_cell = self.__surfaceLoop.cells[pos.x][pos.y]

            if new_cell.is_tree() and not new_cell.chop_wood():
                # the new cell is a tree and if we cant chop it down, we cant move
                continue
                
            old_cell.make_poo()
            
            if new_cell.has_food():
                if creature.is_hungy():
                    creature.age -= 1
                    
            if creature.age > Config.creature_die_age:
                # creature is to old and dies
                self.creatures.remove(creature)
                self.__died += 1
                continue
                
            for c in self.creatures:
                pos = c.get_pos()
                if new_pos.x == pos.x and new_pos.y == pos.y:
                    # first we will know if they kill each other. 
                    if random() > 0.99:
                        try:
                            self.creatures.remove(choice([c, creature]))
                            self.__killed += 1
                        except:
                            pass
                        break
                    if c.can_fuck() and creature.can_fuck() and random() > 0.5:
                        self.new_child(Position(new_pos.x, new_pos.y))
                        self.__new_born += 1
                    else:
                        break
            creature.move(move.x, move.y)

    def draw(self):
        for creature in self.creatures:
            pygame.draw.rect(
                self.__surfaceLoop.get_surface(), creature.color(), creature.data()
            )
