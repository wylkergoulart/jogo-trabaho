import pygame

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, limites_movimento, plataforma):
        super().__init__()
        self.image = pygame.image.load('./assets/inimigo.png')  # Carregando a imagem do inimigo
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajustando o tamanho da imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.limites_movimento = limites_movimento
        self.velocidade = 2
        self.direcao = 1
        self.plataforma = plataforma  # Armazenando a plataforma

    def update(self):
        # Movimento do inimigo dentro dos limites
        self.rect.x += self.velocidade * self.direcao
        if self.rect.left < self.limites_movimento[0] or self.rect.right > self.limites_movimento[1]:
            self.direcao *= -1  # Inverte a direção

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
