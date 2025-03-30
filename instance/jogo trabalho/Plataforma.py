import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, imagem=None):
        super().__init__()
        if imagem:
            self.image = pygame.image.load(imagem)
        else:
            self.image = pygame.Surface((largura, altura))
            self.image.fill((0, 255, 0))  # Cor da plataforma
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
