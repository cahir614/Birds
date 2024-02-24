import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        if self.color == (0, 0, 255):
            self.image = pygame.image.load("images/bird_blue_r.webp").convert_alpha()
            self.imageL = pygame.image.load("images/bird_blue_l.webp").convert_alpha()
        elif self.color == (255, 0, 0):
            self.image = pygame.image.load("images/bird_red_r.webp").convert_alpha()
            self.imageL = pygame.image.load("images/bird_red_l.webp").convert_alpha()
        self.flipped = False

    def moveRight(self, speed):
        if 1920-64 > self.rect.x:
            self.rect.x += speed
            self.flipped = False

    def moveLeft(self, speed):
        if 0 < self.rect.x:
            self.rect.x -= speed
            self.flipped = True

    def moveUp(self, speed):
        if 0 < self.rect.y:
            self.rect.y -= speed + 1

    def moveDown(self, speed):
        if 1024-64 > self.rect.y:
            self.rect.y += speed

    def gravity(self):
        if 1024-256 > self.rect.y:
            self.rect.y += 2

    def draw(self, surface):
        if self.flipped:
            surface.blit(self.imageL, self.rect)
        else:
            surface.blit(self.image, self.rect)
