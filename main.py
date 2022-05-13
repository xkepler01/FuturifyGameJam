import sys, pygame
from world import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((896, 896))
        pygame.display.set_caption("FuturifyGameJam")
        pygame.display.set_icon(pygame.image.load("graphics/icon.png"))
        self.clock = pygame.time.Clock()

        self.world = Level()

        pygame.mixer.music.load("sounds/music.mp3")
        pygame.mixer.music.play(-1)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.world.background_image, (0, 0))
            self.world.run()
            pygame.display.update()
            self.clock.tick(60)
            print(self.clock.get_fps())


if __name__ == "__main__":
    game = Game()
    game.run()

