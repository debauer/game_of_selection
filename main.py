import pygame

from config.config import Config
from loop.creature import CreatureLoop
from loop.surface import SurfaceLoop

pygame.init()
pygame.display.set_caption("pla")


def main():
    surfaceLoop = SurfaceLoop(Config.dimension)
    creatureLoop = CreatureLoop(Config.dimension, surfaceLoop)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_q:
                pygame.quit()
                return

        surfaceLoop.loop()
        creatureLoop.loop()
        surfaceLoop.draw()
        creatureLoop.draw()
        clock.tick(25)
        pygame.display.update()


if __name__ == "__main__":
    main()
