import pygame, sys
from debug import debug
from map import *
from tile import *
from player import Player
from entity import  Box
from time import sleep


class Level:
    def __init__(self):

        self.displaySurface = pygame.display.get_surface()

        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.finishSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.mapSprites = pygame.sprite.Group()
        self.entitySprites = pygame.sprite.Group()

        self.visibleMap = MAP

        self.createMap()
        self.createFinish()
        self.createPlayer()
        self.createBox()

        self.rotated = 0

    def createMap(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "x":
                    Tile((x, y), [self.mapSprites, self.obstacleSprites])

    def createFinish(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "o":
                    Finish((x, y), [self.finishSprites])

    def createPlayer(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "p":
                    self.player = Player((x, y), [self.playerSprites], self.obstacleSprites, self.entitySprites)

    def playerMovement(self):
        keys = pygame.key.get_pressed()

        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):

                if keys[pygame.K_g]:
                    print(row)
                    break

                if column == "p" and keys[pygame.K_d]:
                    print(columnIndex)
                    print(rowIndex)
                    print(row)
                    playerX = columnIndex
                    playerY = self.visibleMap[rowIndex]
                    if playerY[playerX + 1] == " ":
                        del playerY[playerX]
                        playerY.insert(playerX + 1, "p")

                elif column == "p" and keys[pygame.K_a]:
                    print(columnIndex)
                    print(rowIndex)
                    print(row)
                    playerX = columnIndex
                    playerY = self.visibleMap[rowIndex]
                    if playerY[playerX - 1] == " ":
                        del playerY[playerX]
                        playerY.insert(playerX - 1, "p")

                elif column == "p" and keys[pygame.K_w]:
                    print(columnIndex)
                    print(rowIndex)
                    print(row)
                    playerX = columnIndex
                    playerY = self.visibleMap[rowIndex]
                    abovePlayer = self.visibleMap[rowIndex - 1]
                    if abovePlayer[playerX] == " ":
                        del abovePlayer[playerX]
                        del playerY[playerX]
                        playerY.insert(playerX, " ")
                        abovePlayer.insert(playerX, "p")

                elif column == "p" and keys[pygame.K_s]:
                    print(columnIndex)
                    print(rowIndex)
                    print(row)
                    playerX = columnIndex
                    playerY = self.visibleMap[rowIndex]
                    belowPlayer = self.visibleMap[rowIndex + 1]
                    if belowPlayer[playerX] == " ":
                        del belowPlayer[playerX]
                        del playerY[playerX]
                        playerY.insert(playerX, " ")
                        belowPlayer.insert(playerX, "p")


    def createBox(self):
        for rowIndex, row in enumerate(self.visibleMap):
            for columnIndex, column in enumerate(row):
                x = columnIndex * TILESIZE
                y = rowIndex * TILESIZE
                if column == "a":
                    Box((x, y), [self.entitySprites], self.obstacleSprites, self.playerSprites)

    def rotateMap(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.visibleMap = list(map(list, zip(*self.visibleMap[::-1])))
            self.rotated = 1
            print(self.visibleMap)
        elif keys[pygame.K_q]:
            self.visibleMap = list(map(list, zip(*self.visibleMap)))[::-1]
            self.rotated = 1

    def rotatedDelay(self):
        if self.rotated == 1:
            sleep(.2)
            self.rotated = 0

    def run(self):
        debug(self.player.direction)
        # debug(self.player.rect.y)

        self.mapSprites.draw(self.displaySurface)
        self.mapSprites.update()

        self.entitySprites.draw(self.displaySurface)
        self.entitySprites.update()

        self.playerSprites.draw(self.displaySurface)
        self.playerSprites.update()
        self.playerMovement()

        self.finishSprites.draw(self.displaySurface)
        self.finishSprites.update()

        self.rotateMap()
        self.rotatedDelay()

        self.mapSprites.empty()
        self.obstacleSprites.empty()
        self.createMap()

        self.playerSprites.empty()
        self.createPlayer()

        self.finishSprites.empty()
        self.createFinish()


