import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamanho do jogador
        self.image.fill((0, 0, 255))  # Cor azul
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.no_chao = False  # Flag para verificar se o jogador está no chão
        self.pulos = 0  # Contador de pulos

    def update(self, plataformas):
        self.velocidade_y += 1  # Simula a gravidade
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        # Colisão com plataformas
        self.no_chao = False  # Resetar no_chao a cada atualização
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma.rect):
                self.no_chao = True  # O jogador está no chão
                self.velocidade_y = 0  # Reseta a velocidade vertical ao colidir com a plataforma
                self.rect.y = plataforma.rect.top - self.rect.height  # Faz o jogador "subir" na plataforma
                break  # Evita múltiplas colisões

        # Impede que o jogador saia da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:  # Supondo que a largura da tela seja 800
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:  # Supondo que a altura da tela seja 600
            self.rect.bottom = 600

    def mover(self, dx, dy):
        self.velocidade_x = dx
        self.velocidade_y = dy

    def pular(self):
        if self.no_chao or self.pulos < 2:  # Permite um pulo duplo
            self.velocidade_y = -15  # Ajuste da força do pulo
            self.pulos += 1  # Incrementa o contador de pulos

    def desenhar(self, screen):
        screen.blit(self.image, self.rect)  # Desenha o jogador na tela
