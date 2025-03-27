import pygame

class Coletavel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 20
        self.altura = 20
        self.ativo = True
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, screen):
        if self.ativo:
            pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Verde
