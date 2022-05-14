import math

import pygame
from map import *


def round_to_multiply(x, base):
    return base * round(x / base)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites, entitySprites, berrySprites, finishSprites):
        super().__init__(groups)
        self.playerSize = (99 * 0.52, 106 * 0.52)
        self.front = pygame.transform.scale(pygame.image.load("graphics/player/front.png").convert_alpha(), self.playerSize)
        self.back = pygame.transform.scale(pygame.image.load("graphics/player/back.png").convert_alpha(), self.playerSize)
        self.right = pygame.transform.scale(pygame.image.load("graphics/player/right.png").convert_alpha(), self.playerSize)
        self.left = pygame.transform.scale(pygame.image.load("graphics/player/left.png").convert_alpha(), self.playerSize)
        self.image = self.front
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacleSprites = obstacleSprites
        self.entitySprites = entitySprites
        self.berrySprites = berrySprites
        self.finishSprites = finishSprites

        self.rotate_angle = 0
        self.rotate_radians = 0

        self.moving = 0

        self.bonusPoint = 0
        self.finished = 0
        self.score = 0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.moving == 0:
            self.direction.x = math.cos(self.rotate_radians)
            self.direction.y = math.sin(self.rotate_radians)
            self.moving = 1
            self.image = pygame.transform.rotate(self.right, -self.rotate_angle)
        elif keys[pygame.K_a] and self.moving == 0:
            self.direction.x = -math.cos(self.rotate_radians)
            self.direction.y = -math.sin(self.rotate_radians)
            self.moving = 1
            self.image = pygame.transform.rotate(self.left, -self.rotate_angle)
        elif keys[pygame.K_w] and self.moving == 0:
            self.direction.x = math.sin(self.rotate_radians)
            self.direction.y = -math.cos(self.rotate_radians)
            self.moving = 1
            self.image = pygame.transform.rotate(self.back, -self.rotate_angle)
        elif keys[pygame.K_s] and self.moving == 0:
            self.direction.x = -math.sin(self.rotate_radians)
            self.direction.y = math.cos(self.rotate_radians)
            self.moving = 1
            self.image = pygame.transform.rotate(self.front, -self.rotate_angle)
        else:
            self.direction.x = 0
            self.direction.y = 0
            self.moving = 0

    def move(self, speed):
        self.rect.center += self.direction * speed

        self.rect.x += self.direction.x * speed
        self.collisions('horizontal')
        self.rect.y += self.direction.y * speed
        self.collisions('vertical')
        self.collisions('other')

    def rotate(self, angle):
        self.rotate_angle += angle
        self.rotate_angle %= 360
        self.rotate_radians = self.rotate_angle * math.pi / 180
        self.image = pygame.transform.rotate(self.image, -angle)

    def collisions(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
            for sprite in self.entitySprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

            for sprite in self.entitySprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

        for sprite in self.berrySprites:
            if sprite.rect.colliderect(self.rect):
                self.berrySprites.empty()
                self.bonusPoint = 1
                self.score += 3

        for sprite in self.finishSprites:
            if sprite.rect.colliderect(self.rect):
                self.finished = 1

    def update(self):
        self.input()
        self.move(self.speed)