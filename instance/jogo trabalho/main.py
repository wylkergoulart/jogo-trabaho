import pygame
from Jogador import Jogador
from Plataforma import Plataforma
from Inimigo import Inimigo
from Coletavel import Coletavel
from Objetivo import Objetivo

# Inicializa o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meu Jogo de Plataforma 2D")

# Define algumas cores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Controla o FPS do jogo
FPS = 60
clock = pygame.time.Clock()


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
        SCREEN_WIDTH // 2 - loading_text.get_width() // 2,
        SCREEN_HEIGHT // 2 - loading_text.get_height() // 2
    ))
    pygame.display.flip()
    pygame.time.wait(2000)  # Espera 2 segundos


# Criando os botões do menu
play_button = Button("Jogar", 300, 200, 200, 50, GRAY, DARK_GRAY)
exit_button = Button("Sair", 300, 300, 200, 50, GRAY, DARK_GRAY)


# Função para carregar a fase
def carregar_fase(indice):
    global plataformas, inimigos, coletaveis, objetivo, jogador
    fase = fases[indice]
    plataformas = fase["plataformas"]
    inimigos = fase["inimigos"]
    coletaveis = fase["coletaveis"]
    objetivo = fase["objetivo"]
    jogador.x, jogador.y = fase["posicao_inicial"]


# Cria uma instância do jogador (Agora a imagem será carregada automaticamente)
jogador = Jogador(100, 100)

# Configuração das fases
fase_atual = 0
fases = [
    {
        "plataformas": [
            Plataforma(0, 500, 800, 100, './assets/plataforma1.png'),  # Plataforma base
            Plataforma(200, 400, 200, 20, './assets/plataforma1.png'),  # Plataforma intermediária
            Plataforma(500, 300, 150, 20, './assets/plataforma1.png')  # Nova plataforma
        ],
        "inimigos": [Inimigo(300, 460, (250, 450))],
        "coletaveis": [Coletavel(300, 380)],
        "objetivo": Objetivo(700, 250, './assets/estrela.png'),  # Objetivo da fase
        "posicao_inicial": (100, 100)  # Ponto de partida do jogador
    },
    {
        "plataformas": [Plataforma(0, 500, 800, 100, './assets/plataforma1.png'),
                        Plataforma(150, 350, 150, 20, './assets/plataforma1.png'),
                        Plataforma(400, 250, 150, 20, './assets/plataforma1.png')],
        "inimigos": [Inimigo(200, 460, (150, 350)), Inimigo(450, 460, (400, 550))],
        "coletaveis": [Coletavel(200, 330), Coletavel(450, 230)],
        "objetivo": Objetivo(700, 200, './assets/estrela.png'),
        "posicao_inicial": (50, 100)
    },
    {
        "plataformas": [Plataforma(0, 500, 800, 100, './assets/plataforma1.png'),
                        Plataforma(100, 400, 100, 20, './assets/plataforma1.png'),
                        Plataforma(300, 300, 100, 20, './assets/plataforma1.png'),
                        Plataforma(500, 200, 100, 20, './assets/plataforma1.png')],
        "inimigos": [Inimigo(150, 460, (100, 200), vx=3), Inimigo(350, 460, (300, 400), vx=3),
                     Inimigo(550, 460, (500, 600), vx=3)],
        "coletaveis": [Coletavel(150, 380), Coletavel(350, 280), Coletavel(550, 180)],
        "objetivo": Objetivo(700, 150, './assets/estrela.png'),
        "posicao_inicial": (50, 100)
    }
]

# Variável de estado (começa no menu)
estado = "menu"

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        # Lógica do menu
        if estado == "menu":
            if play_button.is_clicked(event):
                show_loading_screen()  # Mostra a tela de carregamento
                carregar_fase(fase_atual)  # Carrega a primeira fase
                estado = "jogo"  # Muda para o estado do jogo
            if exit_button.is_clicked(event):
                rodando = False

        # Lógica do jogo
        elif estado == "jogo":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogador.pular()

    # Executa a lógica dependendo do estado
    if estado == "menu":
        screen.fill(WHITE)  # Fundo branco
        play_button.draw(screen)
        exit_button.draw(screen)

    elif estado == "jogo":
        # Movimenta o jogador para a esquerda e direita
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador.mover(-5, jogador.velocidade_y)  # Move para a esquerda
        elif teclas[pygame.K_RIGHT]:
            jogador.mover(5, jogador.velocidade_y)  # Move para a direita
        else:
            jogador.velocidade_x = 0  # Reseta a velocidade horizontal

        # Atualiza o jogador e verifica colisão com as plataformas
        jogador.update(plataformas)

        # Atualiza os inimigos e verifica colisões
        for inimigo in inimigos:
            inimigo.update()
            if jogador.rect.colliderect(inimigo.rect):
                # Reinicia a fase ao colidir com o inimigo
                jogador.rect.x, jogador.rect.y = fases[fase_atual]["posicao_inicial"]
                jogador.velocidade_x = 0
                jogador.velocidade_y = 0
                break

        # Verifica coleta de itens
        for coletavel in coletaveis:
            if coletavel.ativo and jogador.rect.colliderect(coletavel.rect):
                coletavel.ativo = False

        # Verifica se chegou ao objetivo
        if jogador.rect.colliderect(objetivo.rect):
            print("Você venceu a fase!")

            # Aumenta a fase
            fase_atual += 1

            # Verifica se há mais fases
            if fase_atual < len(fases):
                carregar_fase(fase_atual)  # Carrega a próxima fase
            else:
                print("Você concluiu o jogo! Parabéns!")  # Mensagem de fim de jogo
                rodando = False  # Termina o jogo

        # Desenha os elementos na tela
        screen.fill(WHITE)
        for plataforma in plataformas:
            plataforma.desenhar(screen)
        for inimigo in inimigos:
            inimigo.desenhar(screen)
        for coletavel in coletaveis:
            coletavel.desenhar(screen)
        objetivo.desenhar(screen)
        jogador.desenhar(screen)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
