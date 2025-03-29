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
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        # Verifica se o mouse está sobre o botão
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)  # Cor de hover
        else:
            pygame.draw.rect(screen, self.color, self.rect)  # Cor normal

        # Desenha o texto do botão
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        # Verifica se o botão foi clicado
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


# Função para a tela de carregamento
def show_loading_screen():
    loading_font = pygame.font.Font(None, 50)
    loading_text = loading_font.render("Carregando...", True, BLACK)
    screen.fill(WHITE)
    screen.blit(loading_text, (
    SCREEN_WIDTH // 2 - loading_text.get_width() // 2, SCREEN_HEIGHT // 2 - loading_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Espera 2 segundos


# Criando os botões
play_button = Button("Jogar", 300, 200, 200, 50, GRAY, DARK_GRAY)
exit_button = Button("Sair", 300, 300, 200, 50, GRAY, DARK_GRAY)

# Loop principal
running = True
while running:
    screen.fill(WHITE)  # Fundo branco

    # Processa eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if play_button.is_clicked(event):
            show_loading_screen()  # Mostra a tela de carregamento
            print("Aqui você pode adicionar a lógica do jogo")
        if exit_button.is_clicked(event):
            running = False

    # Desenha os botões
    play_button.draw(screen)
    exit_button.draw(screen)

    pygame.display.flip()  # Atualiza a tela

pygame.quit()
sys.exit()