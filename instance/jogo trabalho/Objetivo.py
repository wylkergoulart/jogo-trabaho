import pygame

class Objetivo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 30
        self.altura = 50
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.rect)  # Amarelo