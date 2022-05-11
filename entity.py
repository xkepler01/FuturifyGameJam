import pygame
from map import *

class Box(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites, playerSprites):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("graphics/box.png").convert_alpha(), (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.direction.y = 1

        self.obstacleSprites = obstacleSprites
        self.playerSprites = playerSprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x, self.rect.y = self.rect.y - (self.rect.y % 32), (640 - 32 - self.rect.x) - (640 - 32 - self.rect.x) % 32
        if keys[pygame.K_RIGHT]:
            self.rect.x, self.rect.y = 640 - 32 - self.rect.y - (640 - 32 - self.rect.y) % 32, self.rect.x - (self.rect.x % 32)

    def move(self, speed):
        self.rect.y += self.direction.y * speed
        self.collisions('vertical')

    def collisions(self, direction):
        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
            for sprite in self.playerSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)


class Blueberry(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load("graphics/blueberry.png").convert_alpha(), (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)

