
import pygame

from loop.creature import CreatureLoop
from loop.surface import SurfaceLoop

pygame.init()
pygame.display.set_caption("pla")


def main():
    surfaceLoop = SurfaceLoop(100, 100)
    creatureLoop = CreatureLoop(100, 100, surfaceLoop)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surfaceLoop.loop()
        creatureLoop.loop()
        surfaceLoop.draw()
        creatureLoop.draw()
        pygame.display.update()
        

if __name__ == "__main__":
    main()
