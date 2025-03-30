import pygame
from main import jogador, play_button, exit_button, carregar_fase, fases, plataformas, inimigos, coletaveis, objetivo

# Configurações
FPS = 60
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# Estado inicial
estado = "menu"
fase_atual = 0
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
        play_button.draw(screen)
        exit_button.draw(screen)

    elif estado == "jogo":
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jogador.mover(-5)
        elif teclas[pygame.K_RIGHT]:
            jogador.mover(5)
        else:
            jogador.mover(0)

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
        screen.fill(WHITE)
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
