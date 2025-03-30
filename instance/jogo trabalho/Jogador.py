import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('./assets/jogador.png')  # Imagem padrão (direita)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 0.8
        self.pulos_restantes = 2  # Permite um pulo normal + um pulo extra

    def update(self, plataformas):
        # Aplicar gravidade
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        # Verificar colisão vertical
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.velocidade_y > 0 and self.rect.bottom > plataforma.rect.top:
                    self.rect.bottom = plataforma.rect.top
                    self.velocidade_y = 0
                    self.pulos_restantes = 2  # Reseta os pulos ao tocar o chão
                elif self.velocidade_y < 0 and self.rect.top < plataforma.rect.bottom:
                    self.rect.top = plataforma.rect.bottom
                    self.velocidade_y = 0

        # Aplicar movimento horizontal
        self.rect.x += self.velocidade_x

        # Verificar colisão lateral
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                if self.velocidade_x > 0:
                    self.rect.right = plataforma.rect.left
                elif self.velocidade_x < 0:
                    self.rect.left = plataforma.rect.right

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

    def mover(self, dx):
        self.velocidade_x = dx

    def pular(self):
        if self.pulos_restantes > 0:
            self.velocidade_y = -15
            self.pulos_restantes -= 1  # Gasta um pulo
