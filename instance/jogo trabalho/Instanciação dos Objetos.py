# Criando o jogador
jogador = Jogador(100, 100)

# Criando plataformas
plataformas = [
    Plataforma(0, 500, 800, 100),  # Chão
    Plataforma(200, 400, 200, 20),
    Plataforma(500, 300, 200, 20),
]

# Criando inimigos
inimigos = [
    Inimigo(300, 460, (250, 450)),
]

# Criando coletáveis
coletaveis = [
    Coletavel(300, 380),
    Coletavel(600, 280),
]

# Criando o objetivo
objetivo = Objetivo(700, 250)