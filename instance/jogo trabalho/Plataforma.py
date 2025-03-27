import pygame

class Plataforma:
    def __init__(self, x, y, largura, altura):
        self.rect = pygame.Rect(x, y, largura, altura)

    def desenhar(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Verde, diferente do fundo branco