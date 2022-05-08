import pygame, sys
from debug import debug
from map import *
from tile import *
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
        self.createPlayer()

        self.ePressed = 0

    def createMap(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "x":
                    Tile((x, y), [self.mapSprites, self.obstacleSprites])
                if column == "o":
                    Finish((x, y), [self.mapSprites])

    def createPlayer(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "p":
                    self.player = Player((x, y), [self.playerSprites], self.obstacleSprites)

    def rotateMap(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print('x')
                if event.key == pygame.K_e:
                    self.visibleMap = [[self.visibleMap[j][i] for i in range(len(self.visibleMap))] for j in range(len(self.visibleMap[0]) - 1, -1, -1)]
                    print(self.visibleMap)
                if event.key == pygame.K_q:
                    self.visibleMap = [[self.visibleMap[j][i] for j in range(len(self.visibleMap[0]) - 1, -1, -1)] for i in range(len(self.visibleMap))]

    def run(self):
        self.mapSprites.draw(self.displaySurface)
        self.mapSprites.update()
        self.playerSprites.draw(self.displaySurface)
        self.playerSprites.update()
        debug(self.player.direction)
        # debug(self.player.rect.y)
        self.rotateMap()
        self.mapSprites.empty()
        self.obstacleSprites.empty()
        self.createMap()
