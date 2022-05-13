import pygame, sys
from debug import debug
from map import *
from tile import *
from player import Player
from entity import Box
from entity import Blueberry
from time import sleep


class Level:
    def __init__(self):
        self.rotated_angle = 0
        self.displaySurface = pygame.display.get_surface()

        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.finishSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.mapSprites = pygame.sprite.Group()
        self.entitySprites = pygame.sprite.Group()
        self.berrySprites = pygame.sprite.Group()

        self.visibleMap = MAP

        self.createMap()
        self.createPlayer()
        self.createBox()
        self.createFinish()
        self.createBerry()

        self.rotated = 0
        self.background_image = pygame.image.load("graphics/background.png")

    def createMap(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "x":
                    Tile((x, y), [self.mapSprites, self.obstacleSprites])
                if column == "h":
                    Border((x, y), [self.obstacleSprites])

    def createFinish(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "f":
                    Finish((x, y), [self.finishSprites])

    def createPlayer(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "p":
                    self.player = Player((x, y), [self.playerSprites], self.obstacleSprites, self.entitySprites, self.berrySprites)

    def createBox(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "b":
                    Box((x, y), [self.entitySprites], self.obstacleSprites, self.playerSprites, self.berrySprites, self.finishSprites, self.entitySprites)

    def createBerry(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "s":
                    Blueberry((x, y), [self.berrySprites])

    def removeBerry(self):
        if self.player.bonusPoint == 1:
            print(1)
            for rowIndex, row in enumerate(self.visibleMap):
                for columnIndex, column in enumerate(row):
                    if column == "s":
                        row[columnIndex] = " "
                        self.player.bonusPoint = 0

    def rotateMap(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            self.visibleMap = list(map(list, zip(*self.visibleMap[::-1])))

            self.berrySprites.empty()
            self.createBerry()
            self.mapSprites.empty()
            self.obstacleSprites.empty()
            self.createMap()
            self.finishSprites.empty()
            self.createFinish()

            self.rotated = 1
            self.background_image = pygame.transform.rotate(self.background_image, -90)

        elif keys[pygame.K_q] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            self.visibleMap = list(map(list, zip(*self.visibleMap)))[::-1]

            self.berrySprites.empty()
            self.createBerry()
            self.mapSprites.empty()
            self.obstacleSprites.empty()
            self.createMap()
            self.finishSprites.empty()
            self.createFinish()

            self.rotated = 1
            self.background_image = pygame.transform.rotate(self.background_image, 90)

    def rotationDelay(self):
        if self.rotated == 1:
            sleep(0.2)
            self.rotated = 0

    def run(self):
        #debug(self.player.direction)
        #debug(self.player.rect.y)

        debug("Score is: " + str(self.player.score))

        self.mapSprites.draw(self.displaySurface)
        self.mapSprites.update()

        self.playerSprites.draw(self.displaySurface)
        self.playerSprites.update()

        self.finishSprites.draw(self.displaySurface)
        self.finishSprites.update()

        self.entitySprites.draw(self.displaySurface)
        self.entitySprites.update()

        self.berrySprites.draw(self.displaySurface)
        self.berrySprites.update()
        self.removeBerry()

        self.rotateMap()
        self.rotationDelay()

