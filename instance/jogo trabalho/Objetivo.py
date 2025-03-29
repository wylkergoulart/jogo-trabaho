import pygame

class Objetivo:
    def __init__(self, x, y, imagem_path):
        self.x = x
        self.y = y
        self.imagem = pygame.image.load(imagem_path).convert_alpha()  # Carrega a imagem original
        # Reduz um pouco mais a imagem (ainda menor que a metade)
        self.imagem = pygame.transform.scale(self.imagem, (self.imagem.get_width() // 3, self.imagem.get_height() // 3))  # Escala para 1/3 do tamanho original
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y

    def desenhar(self, screen):
        screen.blit(self.imagem, self.rect)
