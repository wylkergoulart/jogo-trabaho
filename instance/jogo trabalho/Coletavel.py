import pygame

class Coletavel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))  # Cor do coletável (vermelho)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ativo = True

    def desenhar(self, tela):
        if self.ativo:
            tela.blit(self.image, self.rect)
