import pygame


class Plataforma:
    def __init__(self, x, y, largura, altura, imagem_path=None):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)

        # Se uma imagem for fornecida, carregue-a
        if imagem_path:
            self.imagem = pygame.image.load(imagem_path).convert_alpha()  # Carrega a imagem original
            self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))  # Redimensiona a imagem
        else:
            # Caso não tenha imagem, cria um retângulo colorido (padrão)
            self.imagem = None

    def desenhar(self, screen):
        if self.imagem:
            screen.blit(self.imagem, self.rect)  # Desenha a imagem da plataforma
        else:
            pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Desenha um retângulo verde se não houver imagem
