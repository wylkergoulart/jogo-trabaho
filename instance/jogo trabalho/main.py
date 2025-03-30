import pygame
from Button import Button
from Jogador import Jogador
from Plataforma import Plataforma
from Inimigo import Inimigo
from Coletavel import Coletavel
from Objetivo import Objetivo

# Configurações do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Inicializando o Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Caminho da estrela")
clock = pygame.time.Clock()

# Carregando as imagens de fundo
fundomenu = pygame.image.load('./assets/fundomenu.png')
fundofase = pygame.image.load('./assets/fundofase.png')

# Ajusta a imagem do fundo do menu para o tamanho da tela
fundomenu = pygame.transform.scale(fundomenu, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Função para carregar as fases
def carregar_fase(indice):
    global plataformas, inimigos, coletaveis, objetivo, jogador
    fase = fases[indice]
    plataformas = fase["plataformas"]
    inimigos = fase["inimigos"]
    coletaveis = fase["coletaveis"]
    objetivo = fase["objetivo"]

    jogador.x = plataformas[0].rect.x + (plataformas[0].rect.width - jogador.rect.width) // 2  # Centralizando o jogador
    jogador.y = plataformas[0].rect.y - jogador.rect.height  # Colocando o jogador na plataforma


# Configuração das fases
fase_atual = 0
fases = [
    {
        "plataformas": [
            Plataforma(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50, None),  # Plataforma verde
            Plataforma(150, 350, 48, 48, './assets/plataforma1.png'),
            Plataforma(198, 350, 48, 48, './assets/plataforma1.png'),
            Plataforma(246, 350, 48, 48, './assets/plataforma1.png'),
            Plataforma(400, 250, 48, 48, './assets/plataforma1.png'),
            Plataforma(448, 250, 48, 48, './assets/plataforma1.png'),
            Plataforma(496, 250, 48, 48, './assets/plataforma1.png'),
            Plataforma(650, 150, 48, 48, './assets/plataforma1.png'),
            Plataforma(698, 150, 48, 48, './assets/plataforma1.png'),
            Plataforma(746, 150, 48, 48, './assets/plataforma1.png')
        ],
        "inimigos": [Inimigo(300, 460, (250, 450), None)],
        "coletaveis": [Coletavel(200, 380), Coletavel(500, 280)],
        "objetivo": Objetivo(700, 150, './assets/estrela.png', tamanho=(30, 30)),
        "posicao_inicial": (100, 100)
    },
]

# Variável de estado
estado = "menu"

# Criando o jogador
jogador = Jogador(100, 100)

# Criando os botões do menu
play_button = Button("Jogar", 300, 200, 200, 50, GRAY, DARK_GRAY)
exit_button = Button("Sair", 300, 300, 200, 50, GRAY, DARK_GRAY)

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        # Lógica do menu
        if estado == "menu":
            if play_button.is_clicked(event):
                carregar_fase(fase_atual)
                estado = "jogo"
            if exit_button.is_clicked(event):
                rodando = False

        # Lógica do jogo
        elif estado == "jogo":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogador.pular()

    # Executa a lógica dependendo do estado
    if estado == "menu":
        screen.fill(WHITE)
        screen.blit(fundomenu, (0, 0))  # Adiciona o fundo redimensionado do menu
        play_button.desenhar(screen)
        exit_button.desenhar(screen)

    elif estado == "jogo":
        screen.blit(fundofase, (0, 0))  # Adiciona o fundo da fase
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador.mover(-5)
            jogador.image = pygame.image.load('./assets/run2.png')  # Imagem para o lado esquerdo
        elif teclas[pygame.K_RIGHT]:
            jogador.mover(5)
            jogador.image = pygame.image.load('./assets/jogador.png')  # Imagem para o lado direito
        else:
            jogador.mover(0)

        # Limitar movimento para não ultrapassar os limites da tela
        if jogador.rect.left < 0:
            jogador.rect.left = 0  # Impede que o jogador saia pela esquerda
        if jogador.rect.right > SCREEN_WIDTH:
            jogador.rect.right = SCREEN_WIDTH  # Impede que o jogador saia pela direita

        # Atualiza os objetos
        jogador.update(plataformas)
        objetivo.update()  # Faz a estrela flutuar
        for inimigo in inimigos:
            inimigo.update()

        # Verifica colisão do jogador com inimigos
        for inimigo in inimigos:
            if jogador.rect.colliderect(inimigo.rect):
                jogador.rect.x, jogador.rect.y = fases[fase_atual]["posicao_inicial"]
                jogador.velocidade_x = 0
                jogador.velocidade_y = 0
                break

        # Verifica coleta de itens
        for coletavel in coletaveis:
            if coletavel.ativo and jogador.rect.colliderect(coletavel.rect):
                coletavel.ativo = False

        # Verifica se o jogador toca o objetivo
        if jogador.rect.colliderect(objetivo.rect):
            print("Você venceu a fase!")
            fase_atual += 1
            if fase_atual < len(fases):
                carregar_fase(fase_atual)
            else:
                print("Você concluiu o jogo! Parabéns!")
                rodando = False

        # Desenha os elementos na tela
        for plataforma in plataformas:
            plataforma.desenhar(screen)
        for inimigo in inimigos:
            inimigo.desenhar(screen)
        for coletavel in coletaveis:
            coletavel.desenhar(screen)

        objetivo.desenhar(screen)
        jogador.desenhar(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
