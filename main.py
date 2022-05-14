import sys, pygame
from world import Level,debug


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((896, 896))
        pygame.display.set_caption("The Mage of The Berry")
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

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.world.player.finished = 1

            self.screen.blit(self.world.background_image, (0, 0))
            self.world.run()
            self.screen.blit(pygame.transform.rotate(self.screen, self.world.rotated_angle), (0, 0))

            debug("Score is: " + str(self.world.score))

            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()

# nejake zmeny...