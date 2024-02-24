import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 32
        height = 32
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/food.webp").convert_alpha()
        self.rect.x = random.randrange(100, 1800)
        self.rect.y = random.random() * 100
        self.speed = random.randrange(1, 3)

    def gravity(self):
        if 1024-256 > self.rect.y:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
