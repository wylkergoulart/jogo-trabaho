import pygame
from main import jogador, clock, fases, carregar_fase, screen, WHITE, FPS

# Inicializando as variáveis que faltam
fase_atual = 0
plataformas = []
inimigos = []
coletaveis = []
objetivo = None

# Função para carregar a fase atual
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
    if teclas[pygame.K_RIGHT]:
        jogador.mover(5, jogador.velocidade_y)   # Move para a direita enquanto mantém a velocidade y do pulo

    # Atualiza o jogador e verifica colisão com as plataformas
    jogador.update(plataformas)

    # Atualiza os inimigos e verifica colisões
    for inimigo in inimigos:
        inimigo.update()
        if jogador.rect.colliderect(inimigo.rect):
            jogador.rect.x, jogador.rect.y = fases[fase_atual]["posicao_inicial"]

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

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
