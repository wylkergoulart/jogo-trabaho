import pygame

class Button:
    def __init__(self, texto, x, y, largura, altura, cor_normal, cor_hover):
        self.texto = texto
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor_normal = cor_normal
        self.cor_hover = cor_hover
        self.reto = pygame.Rect(x, y, largura, altura)

        # Configuração da fonte
        self.fonte = pygame.font.SysFont("Arial", 30)
        self.texto_renderizado = self.fonte.render(self.texto, True, (255, 255, 255))
        self.texto_rect = self.texto_renderizado.get_rect(center=self.reto.center)

    def desenhar(self, tela):
        # Desenha o botão na tela
        posicao_mouse = pygame.mouse.get_pos()
        if self.reto.collidepoint(posicao_mouse):
            pygame.draw.rect(tela, self.cor_hover, self.reto)
        else:
            pygame.draw.rect(tela, self.cor_normal, self.reto)

        # Desenha o texto no botão
        tela.blit(self.texto_renderizado, self.texto_rect)

    def is_clicked(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.reto.collidepoint(evento.pos):
                return True
        return False
