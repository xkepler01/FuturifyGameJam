import pygame, sys
from debug import debug
from map import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):

        self.displaySurface = pygame.display.get_surface()

        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.mapSprites = pygame.sprite.Group()

        self.visibleMap = MAP
        self.createMap()

        self.ePressed = 0

    def createMap(self):
        for rowIndex, row in enumerate(self.visibleMap):
            print(row)
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "x":
                    Tile((x, y), [self.mapSprites, self.obstacleSprites])
                if column == "p":
                    self.player = Player((x, y), [self.playerSprites], self.obstacleSprites)

    def rotateMap(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                 if event.key == pygame.K_e:
                    self.visibleMap = [[self.visibleMap[j][i] for j in range(len(self.visibleMap))] for i in range(len(self.visibleMap[0]))]
                    print(self.visibleMap)



    def run(self):
        self.mapSprites.draw(self.displaySurface)
        self.mapSprites.update()
        self.playerSprites.draw(self.displaySurface)
        self.playerSprites.update()
        debug(self.player.direction)
        #debug(self.player.rect.y)
        self.rotateMap()
        self.mapSprites.empty()
        self.createMap()


