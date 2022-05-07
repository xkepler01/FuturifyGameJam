import pygame

class Level:
    def __init__(self):

        #display surface
        self.displaySurface = pygame.display.get_surface()

        self.visibleSprites = pygame.sprite.Group()
        self.obstaclesSprites = pygame.sprite.Group()

    def run(self):
        #update what you see
        pass