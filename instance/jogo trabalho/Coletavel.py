import pygame

class Coletavel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 20
        self.altura = 20
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.ativo = True  # Inicialmente ativo

    def desenhar(self, screen):
        if self.ativo:
            pygame.draw.circle(screen, (0, 255, 255), self.rect.center, self.largura // 2)  # Desenha em ciano
