import math

import pygame, sys
from debug import debug
from map import *
from tile import *
from player import Player
from entity import Box
from entity import Blueberry
from time import sleep
import random_map

class Level:
    def __init__(self):
        self.rotated_angle = 0
        self.rotation_animation = 0
        self.rotation_direction = 0
        self.displaySurface = pygame.display.get_surface()

        self.visibleSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.finishSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()
        self.mapSprites = pygame.sprite.Group()
        self.entitySprites = pygame.sprite.Group()
        self.berrySprites = pygame.sprite.Group()
        self.visibleMap = random_map.random_map(random_map.arrays)

        self.createMap()
        self.createPlayer()
        self.createBox()
        self.createFinish()
        self.createBerry()

        self.rotated = 0
        self.background_image = pygame.image.load("graphics/background.png")
        self.score = 0

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
                    self.player = Player((x, y), [self.playerSprites], self.obstacleSprites, self.entitySprites, self.berrySprites, self.finishSprites)

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
            for rowIndex, row in enumerate(self.visibleMap):
                for columnIndex, column in enumerate(row):
                    if column == "s":
                        row[columnIndex] = " "
                        self.player.bonusPoint = 0

    def rotateMap(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q] and not self.rotated:
            self.rotation_animation = -90
            self.rotation_direction = -1
            self.player.rotate(90)

            for entity in self.entitySprites:
                entity.direction.y, entity.direction.x = entity.direction.x, -entity.direction.y
                entity.image = pygame.transform.rotate(entity.image, -90)

            for berry in self.berrySprites:
                berry.image = pygame.transform.rotate(berry.image, -90)

            for finish in self.finishSprites:
                finish.image = pygame.transform.rotate(finish.image, -90)

            self.rotated = 1

        elif keys[pygame.K_e] and not self.rotated:
            self.rotation_animation = 90
            self.rotation_direction = 1
            self.player.rotate(-90)

            for entity in self.entitySprites:
                entity.direction.y, entity.direction.x = -entity.direction.x, entity.direction.y
                entity.image = pygame.transform.rotate(entity.image, 90)

            for berry in self.berrySprites:
                berry.image = pygame.transform.rotate(berry.image, 90)

            for finish in self.finishSprites:
                finish.image = pygame.transform.rotate(finish.image, 90)

            self.rotated = 1

    def getNewLevel(self):
        if self.player.finished == 1:
            self.score += self.player.score
            self.visibleMap = random_map.random_map(random_map.arrays)

            self.obstacleSprites.empty()
            self.mapSprites.empty()
            self.playerSprites.empty()
            self.entitySprites.empty()
            self.finishSprites.empty()
            self.berrySprites.empty()

            self.createMap()
            self.createPlayer()
            self.createBox()
            self.createFinish()
            self.createBerry()

            self.player.finished = 0
            self.rotated_angle = 0
            self.rotation_animation = 0
            self.rotation_direction = 0

    def run(self):
        #debug(self.player.direction)
        #debug(self.player.rect.y)

        self.mapSprites.draw(self.displaySurface)
        self.mapSprites.update()

        self.playerSprites.draw(self.displaySurface)
        self.playerSprites.update()

        self.finishSprites.draw(self.displaySurface)
        self.finishSprites.update()

        self.berrySprites.draw(self.displaySurface)
        self.berrySprites.update()

        self.entitySprites.draw(self.displaySurface)
        self.entitySprites.update()
        self.removeBerry()

        self.rotateMap()
        self.rotationAnimate()

        self.getNewLevel()

    def rotationAnimate(self):
        if self.rotated == 1:
            if self.rotation_animation != 0:
                self.rotated_angle -= self.rotation_direction * 2
                self.rotation_animation -= self.rotation_direction * 2
            else:
                self.rotated = 0
                self.rotation_direction = 0

