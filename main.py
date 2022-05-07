import sys
import pygame
from world import Level

#xy
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("FuturifyGameJam")
        self.clock = pygame.time.Clock()

        self.world = Level()

    def run(self):
        while True:
            # process the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # update the gamestate
            self.screen.fill('gray')
            self.world.run()
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()


