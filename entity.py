import pygame
from map import *


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
        self.entitiySprites = entitySprites

        self.posX, self.posY = pos

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            self.rect.x, self.rect.y = self.rect.y - (self.rect.y % 64), (896 - 64 - self.rect.x) - (896 - 64 - self.rect.x) % 64
        if keys[pygame.K_e] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]:
            self.rect.x, self.rect.y = 896 - 64 - self.rect.y - (896 - 64 - self.rect.y) % 64, self.rect.x - (self.rect.x % 64)

    def move(self, speed):
        self.rect.y += self.direction.y * speed
        self.collisions()

    def collisions(self):
        for sprite in self.obstacleSprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top

        for sprite in self.playerSprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top

        for sprite in self.berrySprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top

        for sprite in self.entitiySprites:
            if sprite.rect.colliderect(self.rect) and not sprite.rect.collidepoint(self.posX + TILESIZE - 1, self.posX + TILESIZE - 1):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top

    def update(self):
        self.input()
        self.move(self.speed)


class Blueberry(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("graphics/blueberry.png").convert_alpha(), (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)

