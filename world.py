import pygame
from map import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        #display surface
        self.displaySurface = pygame.display.get_surface()

        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()

        self.createMap()

    def createMap(self):
        for rowIndex, row in enumerate(MAP):
             for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "x":
                    Tile((x, y), [self.visibleSprites, self.obstacleSprites])
                if column == "p":
                    self.player = Player((x, y), [self.visibleSprites], self.obstacleSprites)

    def run(self):
        #update what you see
        self.visibleSprites.draw(self.displaySurface)
        self.visibleSprites.update()
        debug(self.player.direction)