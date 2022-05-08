import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/player/right.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 6

        self.obstacleSprites = obstacleSprites

        self.moving = 0

    def texture(self):
        if self.direction.x < 0:
            self.image = pygame.image.load("graphics/player/left.png")
        elif self.direction.x > 0:
            self.image = pygame.image.load("graphics/player/right.png")

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and self.moving == 0:
            self.direction.x = 1
            self.moving = 1
        elif keys[pygame.K_a] and self.moving == 0:
            self.direction.x = -1
            self.moving = 1
        elif keys[pygame.K_w] and self.moving == 0:
            self.direction.y = -1
            self.moving = 1
        elif keys[pygame.K_s] and self.moving == 0:
            self.direction.y = 1
            self.moving = 1
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
        #self.counter += 1
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
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                #    self.onGround = 1
                #elif self.counter == 50:
                #    self.onGround = 0
                #    self.counter = 0
                #    self.jump = 10


    def update(self):
        self.input()
        self.move(self.speed)
        self.texture()

