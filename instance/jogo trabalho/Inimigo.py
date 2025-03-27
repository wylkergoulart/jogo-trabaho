import pygame


class Inimigo:
    def __init__(self, x, y, limite, vx=2):
        self.x = x
        self.y = y
        self.limite_esquerdo, self.limite_direito = limite
        self.vx = vx
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def update(self):
        # Movimento do inimigo entre os limites
        self.x += self.vx
        if self.x <= self.limite_esquerdo or self.x >= self.limite_direito:
            self.vx *= -1  # Inverte a direção ao atingir os limites
        self.rect.x = self.x

    def desenhar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Desenha o inimigo em vermelho
