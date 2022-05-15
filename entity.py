import pygame
from map import *


def round_to_multiply(x, base):
    return base * round(x / base)


class Box(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites, playerSprites, berrySprites, finishSprites, entitySprites):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("graphics/box.png").convert_alpha(), (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.direction.y = 1

        self.obstacleSprites = obstacleSprites
        self.playerSprites = playerSprites
        self.berrySprites = berrySprites
        self.finishSprites = finishSprites
        self.entitySprites = entitySprites

        self.posX, self.posY = pos

    def input(self):
        pass

    def move(self, speed):
        self.rect.y += self.direction.y * speed
        self.collisions(True)
        self.rect.x += self.direction.x * speed
        self.collisions()

    def collisions(self, vertical = False):
        for sprite in self.obstacleSprites:
            if sprite.rect.colliderect(self.rect):
                if vertical:
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                else:
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        for sprite in self.playerSprites:
            if sprite.rect.colliderect(self.rect):
                if vertical:
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                else:
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        for sprite in self.entitySprites:
            if sprite.rect.colliderect(self.rect) and sprite.rect != self.rect:
                if vertical:
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                else:
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

    def update(self):
        self.input()
        self.move(self.speed)


class Blueberry(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("graphics/blueberry.png").convert_alpha(), (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)

