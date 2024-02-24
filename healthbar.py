import pygame


class Healthbar():
    def __init__(self):
        super().__init__()

    def draw(self, surface, redu):
        pygame.draw.rect(surface, (0, 0, 0), [20+896, 20, 800, 50])
        pygame.draw.rect(surface, (255, 105, 97), [30+redu+896, 30, 780-redu, 30])
