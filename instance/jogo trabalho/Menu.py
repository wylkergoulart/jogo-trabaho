import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu do Jogo")

# Cores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)


# Classe para os botões
class Button:
    def __init__(self, text, x, y, font_size, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(x, y, 0, 0)  # O retângulo é agora apenas para detecção de clique

    def draw(self, screen):
        # Cria a fonte e o texto
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        self.rect = text_rect  # Atualiza o retângulo para o tamanho do texto

        # Verifica se o mouse está sobre o botão
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            text_surface = font.render(self.text, True, self.hover_color)  # Aplica a cor de hover no texto

        # Desenha o texto na tela
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        # Verifica se o botão foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# Classe para o Menu
class Menu:
    def __init__(self):
        # Botões do menu
        self.play_button = Button("Jogar", 400, 250, 48, GRAY, DARK_GRAY)
        self.exit_button = Button("Sair", 400, 350, 48, GRAY, DARK_GRAY)

        # Fonte e título do jogo
        self.title_font = pygame.font.Font(None, 72)
        self.title_text = self.title_font.render("Caminho da Estrela", True, WHITE)
        self.title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))

    def draw(self):
        # Desenha o fundo
        screen.fill(BLACK)

        # Desenha o título
        screen.blit(self.title_text, self.title_rect)

        # Desenha os botões
        self.play_button.draw(screen)
        self.exit_button.draw(screen)

    def handle_events(self, event):
        # Lógica do menu
        if self.play_button.is_clicked(event):
            return False  # Mudar para a tela de jogo ou outro estado
        if self.exit_button.is_clicked(event):
            return False  # Fechar o jogo
        return True


# Loop principal
running = True
menu = Menu()

while running:
    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Chamando o método que lida com os eventos do menu
        running = menu.handle_events(event)

    # Desenha o menu
    menu.draw()

    pygame.display.flip()  # Atualiza a tela

pygame.quit()
sys.exit()
