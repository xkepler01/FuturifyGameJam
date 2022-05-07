import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacleSprites = obstacleSprites
    def input(self):
        keys = pygame.key.get_pressed()
        isJump = False
        v = 1
        m = 1

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if isJump == False:
            if keys[pygame.K_w]:
                isJump = True

        if isJump:
            F = (1 / 2) * m * (v ** 2)
            self.direction.y -= F
            v = v - 1
            if v < 0:
                m = -1
            if v == -2:
                isJump = False
                v = 5
                m = 1

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

        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top



    def update(self):
        self.input()
        self.move(self.speed)
