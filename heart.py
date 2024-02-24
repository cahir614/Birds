import pygame


class Heart():
    def __init__(self, x, y):
        super().__init__()
        width = 32
        height = 32
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/heart.png").convert_alpha()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface, x, y):
        self.rect.center = (x, y)
        surface.blit(self.image, self.rect)
