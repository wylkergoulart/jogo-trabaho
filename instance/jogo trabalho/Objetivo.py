import pygame
import math

class Objetivo(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, tamanho=(30, 30)):
        super().__init__()
        self.image = pygame.image.load(imagem)
        self.image = pygame.transform.scale(self.image, tamanho)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.posicao_inicial = y  # Salva a posição original
        self.tempo = 0  # Controla a animação da flutuação

    def update(self):
        """Faz a estrela flutuar suavemente para cima e para baixo."""
        self.rect.y = self.posicao_inicial + math.sin(self.tempo) * 15  # Aumentei a amplitude
        self.tempo += 0.1  # Define a velocidade da flutuação

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
