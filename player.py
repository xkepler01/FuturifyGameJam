import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites):
        super().__init__(groups)
        self.image = pygame.image.load("graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 4

        self.obstacleSprites = obstacleSprites

        self.onGround = 2
        self.counter = 0
        self.jump = 10

    def input(self):
        keys = pygame.key.get_pressed()

        if self.onGround == 1:
            self.direction.y = 0
        else:
            self.direction.y = 1
        if self.jump > 0:
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.jump -= 1

        if keys[pygame.K_d]:
            self.direction.x = 1
            #self.direction.y = 0
        elif keys[pygame.K_a]:
            self.direction.x = -1
            #self.direction.y = 0
        else:
            self.direction.x = 0

    def move(self, speed):
        self.rect.center += self.direction * speed

        self.rect.x += self.direction.x * speed
        self.collisions('horizontal')
        self.rect.y += self.direction.y * speed
        self.collisions('vertical')

    def collisions(self, direction):
        self.counter += 1
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
                    self.onGround = 1
                elif self.counter == 50:
                    self.onGround = 0
                    self.counter = 0
                    self.jump = 10


    def update(self):
        self.input()
        self.move(self.speed)

