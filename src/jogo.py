import pygame
import random
import sys

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TAMANHO_QUADRADO,
    TITULO_JOGO,
    CINZA,
    VERDE,
    VERMELHO,
    LARANAJA,
    AMARELO,
    BRANCO,
    PRETO,
    CAMINHO_RECORDE,
    TEMPO_JOGO,
    VIDAS_INICIAIS,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    tomar_dano,
    formatar_tempo,
)
from src.sprites import criar_quadrado
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking,
)


def criar_cobra_inicial():
    """Cria a cobra inicial no centro da tela."""
    x_inicio = (LARGURA_TELA // (2 * TAMANHO_QUADRADO)) * TAMANHO_QUADRADO
    y_inicio = (ALTURA_TELA // (2 * TAMANHO_QUADRADO)) * TAMANHO_QUADRADO
    
    # Cobra começa com 3 segmentos
    cobra = [
        [x_inicio, y_inicio],
        [x_inicio - TAMANHO_QUADRADO, y_inicio],
        [x_inicio - 2 * TAMANHO_QUADRADO, y_inicio],
    ]
    return cobra


def criar_comida(cobra, obstaculos=None):
    """Cria comida em posição aleatória (não sobrepondo a cobra ou obstáculos)."""
    if obstaculos is None:
        obstaculos = []
    
    while True:
        x = (random.randint(0, (LARGURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
        y = (random.randint(0, (ALTURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
        
        # Garante que comida não nasce sobre a cobra ou obstáculos
        if [x, y] not in cobra and [x, y] not in obstaculos:
            return [x, y]


def criar_obstaculo(cobra, obstaculos_existentes=None):
    """Cria um obstáculo em posição aleatória."""
    if obstaculos_existentes is None:
        obstaculos_existentes = []
    
    while True:
        x = (random.randint(0, (LARGURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
        y = (random.randint(0, (ALTURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
        
        # Garante que obstáculo não nasce sobre cobra ou outro obstáculo
        if [x, y] not in cobra and [x, y] not in obstaculos_existentes:
            return [x, y]


def atualizar_cobra(cobra, direcao):
    """Atualiza a posição da cobra conforme a direção."""
    cabeca_x, cabeca_y = cobra[0]
    
    # Move a cabeça conforme a direção
    if direcao == "UP":
        cabeca_y -= TAMANHO_QUADRADO
    elif direcao == "DOWN":
        cabeca_y += TAMANHO_QUADRADO
    elif direcao == "LEFT":
        cabeca_x -= TAMANHO_QUADRADO
    elif direcao == "RIGHT":
        cabeca_x += TAMANHO_QUADRADO
    
    # Adiciona novo segmento na cabeça
    cobra.insert(0, [cabeca_x, cabeca_y])
    
    # Remove o último segmento (exceto quando comer)
    cobra.pop()
    
    return cobra


def verificar_colisao_cobra(cobra):
    """Verifica se a cobra colidiu com ela mesma."""
    cabeca = cobra[0]
    return cabeca in cobra[1:]


def verificar_colisao_paredes(cobra):
    """Verifica se a cobra colidiu com as bordas."""
    cabeca_x, cabeca_y = cobra[0]
    return cabeca_x < 0 or cabeca_x >= LARGURA_TELA or cabeca_y < 0 or cabeca_y >= ALTURA_TELA


def verificar_colisao_comida(cobra, comida):
    """Verifica se a cobra comeu a comida."""
    return cobra[0] == comida


def verificar_colisao_obstaculo(cobra, obstaculos):
    """Verifica se a cobra colidiu com um obstáculo."""
    return cobra[0] in obstaculos


def desenhar_jogo(tela, cobra, comida, obstaculos, pontos, vidas, tempo, recorde):
    """Desenha todos os elementos do jogo na tela."""
    # Preenche o fundo
    tela.fill(PRETO)
    
    # Desenha a cobra
    for segmento in cobra:
        rect = pygame.Rect(segmento[0], segmento[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO)
        pygame.draw.rect(tela, VERDE, rect)
        pygame.draw.rect(tela, BRANCO, rect, 1)  # Borda
    
    # Desenha a comida
    rect_comida = pygame.Rect(comida[0], comida[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO)
    pygame.draw.rect(tela, AMARELO, rect_comida)
    
    # Desenha os obstáculos
    for obstaculo in obstaculos:
        rect_obs = pygame.Rect(obstaculo[0], obstaculo[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO)
        pygame.draw.rect(tela, VERMELHO, rect_obs)
    
    # Desenha HUD (informações de jogo)
    desenhar_hud(tela, pontos, vidas, tempo, recorde)
    
    # Atualiza a tela
    pygame.display.flip()


def desenhar_hud(tela, pontos, vidas, tempo, recorde):
    """Desenha as informações de HUD (pontos, vidas, tempo, recorde)."""
    fonte = pygame.font.Font(None, 24)
    
    # Texto de pontos
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))
    
    # Texto de vidas
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, BRANCO)
    tela.blit(texto_vidas, (10, 40))
    
    # Texto de tempo
    tempo_formatado = formatar_tempo(tempo)
    texto_tempo = fonte.render(f"Tempo: {tempo_formatado}", True, BRANCO)
    tela.blit(texto_tempo, (LARGURA_TELA - 150, 10))
    
    # Texto de recorde
    texto_recorde = fonte.render(f"Recorde: {recorde}", True, AMARELO)
    tela.blit(texto_recorde, (LARGURA_TELA - 150, 40))


def desenhar_tela_fim(tela, pontos, vidas_finais, tempo_final, vitoria=False):
    """Desenha a tela de fim de jogo."""
    tela.fill(PRETO)
    
    fonte_titulo = pygame.font.Font(None, 48)
    fonte_texto = pygame.font.Font(None, 32)
    fonte_pequena = pygame.font.Font(None, 24)
    
    if vitoria:
        titulo = fonte_titulo.render("VOCE VENCEU!", True, VERDE)
    else:
        titulo = fonte_titulo.render("GAME OVER", True, VERMELHO)
    
    texto_pontos = fonte_texto.render(f"Pontos: {pontos}", True, BRANCO)
    texto_tempo = fonte_texto.render(f"Tempo: {formatar_tempo(tempo_final)}", True, BRANCO)
    texto_restart = fonte_pequena.render("Pressione R para recomecar ou Q para sair", True, CINZA)
    
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 100))
    tela.blit(texto_pontos, (LARGURA_TELA // 2 - texto_pontos.get_width() // 2, 200))
    tela.blit(texto_tempo, (LARGURA_TELA // 2 - texto_tempo.get_width() // 2, 280))
    tela.blit(texto_restart, (LARGURA_TELA // 2 - texto_restart.get_width() // 2, 400))
    
    pygame.display.flip()


def executar_jogo():
    """Função principal que executa o loop do jogo."""
    pygame.init()
    
    # Configurações da janela
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    clock = pygame.time.Clock()
    
    # Estado do jogo
    rodando = True
    em_jogo = True
    
    while rodando:
        # Inicializa estado do jogo
        cobra = criar_cobra_inicial()
        comida = criar_comida(cobra)
        obstaculos = []
        
        pontos = 0
        vidas = VIDAS_INICIAIS
        tempo_restante = TEMPO_JOGO
        recorde = carregar_recorde(CAMINHO_RECORDE)
        
        direcao = "RIGHT"
        proxima_direcao = "RIGHT"
        
        contador_frames = 0
        contador_tempo = 0
        contador_obstaculo = 0
        
        em_jogo = True
        
        while em_jogo and rodando:
            # Controla FPS
            clock.tick(FPS)
            contador_frames += 1
            contador_tempo += 1
            contador_obstaculo += 1
            
            # Atualiza tempo a cada segundo (FPS vezes)
            if contador_tempo >= FPS:
                tempo_restante -= 1
                contador_tempo = 0
            
            # Criação de obstáculos (a cada 5 segundos)
            if contador_obstaculo >= FPS * 5 and len(obstaculos) < 5:
                novo_obstaculo = criar_obstaculo(cobra, obstaculos)
                obstaculos.append(novo_obstaculo)
                contador_obstaculo = 0
            
            # Trata eventos (entrada do usuário)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    em_jogo = False
                
                elif evento.type == pygame.KEYDOWN:
                    # Mudança de direção
                    if evento.key == pygame.K_UP and direcao != "DOWN":
                        proxima_direcao = "UP"
                    elif evento.key == pygame.K_DOWN and direcao != "UP":
                        proxima_direcao = "DOWN"
                    elif evento.key == pygame.K_LEFT and direcao != "RIGHT":
                        proxima_direcao = "LEFT"
                    elif evento.key == pygame.K_RIGHT and direcao != "LEFT":
                        proxima_direcao = "RIGHT"
            
            # Atualiza cobra a cada 10 frames (movimento mais lento)
            if contador_frames >= 10:
                direcao = proxima_direcao
                cobra = atualizar_cobra(cobra, direcao)
                contador_frames = 0
                
                # Verifica colisão com comida
                if verificar_colisao_comida(cobra, comida):
                    # Cobra cresce
                    cobra.insert(0, cobra[0].copy())
                    comida = criar_comida(cobra, obstaculos)
                    pontos = calcular_pontos(pontos, 10)
                
                # Verifica colisão com obstáculo
                if verificar_colisao_obstaculo(cobra, obstaculos):
                    vidas = tomar_dano(vidas, 1)
                    cobra = criar_cobra_inicial()
                    comida = criar_comida(cobra, obstaculos)
                
                # Verifica colisão com ela mesma
                if verificar_colisao_cobra(cobra):
                    vidas = tomar_dano(vidas, 1)
                    cobra = criar_cobra_inicial()
                    comida = criar_comida(cobra, obstaculos)
                
                # Verifica colisão com paredes
                if verificar_colisao_paredes(cobra):
                    vidas = tomar_dano(vidas, 1)
                    cobra = criar_cobra_inicial()
                    comida = criar_comida(cobra, obstaculos)
            
            # Verifica fim de jogo
            if jogador_perdeu(vidas):
                em_jogo = False
                vitoria = False
            
            # Verifica vitória (tempo acabou)
            if tempo_restante <= 0:
                em_jogo = False
                vitoria = True
            
            # Desenha o jogo
            desenhar_jogo(tela, cobra, comida, obstaculos, pontos, vidas, tempo_restante, recorde)
        
        # Se ainda está rodando, mostra tela de fim
        if rodando:
            # Atualiza recorde se necessário
            if pontos > recorde:
                salvar_recorde(CAMINHO_RECORDE, pontos)
                recorde = pontos
            
            # Salva no ranking
            ranking = carregar_ranking("data/ranking.txt")
            ranking.append({"pontos": pontos, "tempo": TEMPO_JOGO - tempo_restante})
            ranking.sort(key=lambda x: x["pontos"], reverse=True)
            ranking = ranking[:10]  # Mantém apenas os 10 melhores
            salvar_ranking("data/ranking.txt", ranking)
            
            # Tela de fim de jogo
            esperando_input = True
            while esperando_input and rodando:
                desenhar_tela_fim(tela, pontos, vidas, TEMPO_JOGO - tempo_restante, vitoria)
                
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        rodando = False
                        esperando_input = False
                    elif evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            esperando_input = False
                        elif evento.key == pygame.K_q:
                            rodando = False
                            esperando_input = False
                
                clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


def verificar_colisao_comida(cobra, comida):
    """Verifica se a cobra comeu a comida."""
    return cobra[0] == comida


def verificar_colisao_obstaculo(cobra, obstaculos):
    """Verifica se a cobra colidiu com algum obstáculo."""
    cabeca = cobra[0]
    return cabeca in obstaculos