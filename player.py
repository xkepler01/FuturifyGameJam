import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites, entitySprites):
        super().__init__(groups)
        self.front = pygame.image.load("graphics/player/front.png").convert_alpha()
        self.back = pygame.image.load("graphics/player/back.png").convert_alpha()
        self.right = pygame.image.load("graphics/player/right.png").convert_alpha()
        self.left = pygame.image.load("graphics/player/left.png").convert_alpha()
        self.image = self.front
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacleSprites = obstacleSprites
        self.entitySprites = entitySprites

        self.moving = 0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.moving == 0:
            self.direction.x = 1
            self.moving = 1
            self.image = self.right
        elif keys[pygame.K_a] and self.moving == 0:
            self.direction.x = -1
            self.moving = 1
            self.image = self.left
        elif keys[pygame.K_w] and self.moving == 0:
            self.direction.y = -1
            self.moving = 1
            self.image = self.back
        elif keys[pygame.K_s] and self.moving == 0:
            self.direction.y = 1
            self.moving = 1
            self.image = self.front
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

    def update(self):
        self.input()
        self.move(self.speed)

