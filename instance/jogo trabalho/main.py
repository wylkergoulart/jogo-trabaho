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

# Controla o FPS do jogo
FPS = 60
clock = pygame.time.Clock()

# Cria uma instância do jogador
jogador = Jogador(100, 100)

# Função para carregar a fase
def carregar_fase(indice):
    global plataformas, inimigos, coletaveis, objetivo
    fase = fases[indice]
    plataformas = fase["plataformas"]
    inimigos = fase["inimigos"]
    coletaveis = fase["coletaveis"]
    objetivo = fase["objetivo"]
    jogador.x, jogador.y = fase["posicao_inicial"]

fase_atual = 0

fases = [
    {
        "plataformas": [
            Plataforma(0, 500, 800, 100),         # Plataforma base
            Plataforma(200, 400, 200, 20),        # Plataforma intermediária
            Plataforma(500, 300, 150, 20)         # Nova plataforma
        ],
        "inimigos": [Inimigo(300, 460, (250, 450))],
        "coletaveis": [Coletavel(300, 380)],
        "objetivo": Objetivo(700, 250),          # Objetivo da fase
        "posicao_inicial": (100, 100)            # Ponto de partida do jogador
    },
    {
        "plataformas": [Plataforma(0, 500, 800, 100), Plataforma(150, 350, 150, 20), Plataforma(400, 250, 150, 20)],
        "inimigos": [Inimigo(200, 460, (150, 350)), Inimigo(450, 460, (400, 550))],
        "coletaveis": [Coletavel(200, 330), Coletavel(450, 230)],
        "objetivo": Objetivo(700, 200),
        "posicao_inicial": (50, 100)
    },
    {
        "plataformas": [Plataforma(0, 500, 800, 100), Plataforma(100, 400, 100, 20), Plataforma(300, 300, 100, 20), Plataforma(500, 200, 100, 20)],
        "inimigos": [Inimigo(150, 460, (100, 200), vx=3), Inimigo(350, 460, (300, 400), vx=3), Inimigo(550, 460, (500, 600), vx=3)],
        "coletaveis": [Coletavel(150, 380), Coletavel(350, 280), Coletavel(550, 180)],
        "objetivo": Objetivo(700, 150),
        "posicao_inicial": (50, 100)
    }
]

carregar_fase(fase_atual)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.pular()

    # Movimenta o jogador para a esquerda e direita
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador.mover(-5, jogador.velocidade_y)  # Move para a esquerda enquanto mantém a velocidade y do pulo
    elif teclas[pygame.K_RIGHT]:
        jogador.mover(5, jogador.velocidade_y)   # Move para a direita enquanto mantém a velocidade y do pulo
    else:
        jogador.velocidade_x = 0  # Reseta a velocidade horizontal quando não há movimento

    # Atualiza o jogador e verifica colisão com as plataformas
    jogador.update(plataformas)

    # Atualiza os inimigos e verifica colisões
    for inimigo in inimigos:
        inimigo.update()
        if jogador.rect.colliderect(inimigo.rect):
            # Reinicia a fase ao colidir com o inimigo
            jogador.rect.x, jogador.rect.y = fases[fase_atual]["posicao_inicial"]
            jogador.velocidade_x = 0  # Zera a velocidade horizontal ao reiniciar a fase
            jogador.velocidade_y = 0  # Zera a velocidade vertical ao reiniciar a fase
            break  # Para verificar se o jogador colidiu com o inimigo apenas uma vez

    # Verifica coleta de itens
    for coletavel in coletaveis:
        if coletavel.ativo and jogador.rect.colliderect(coletavel.rect):
            coletavel.ativo = False

    # Verifica se chegou ao objetivo
    if jogador.rect.colliderect(objetivo.rect):
        print("Você venceu a fase!")
        fase_atual += 1
        if fase_atual < len(fases):
            carregar_fase(fase_atual)
        else:
            print("Você concluiu o jogo! Parabéns!")
            rodando = False

    # Desenha os elementos na tela
    screen.fill(WHITE)
    for plataforma in plataformas:
        plataforma.desenhar(screen)
    for inimigo in inimigos:
        inimigo.desenhar(screen)
    for coletavel in coletaveis:
        coletavel.desenhar(screen)
    objetivo.desenhar(screen)

    # Desenha o jogador
    jogador.desenhar(screen)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
