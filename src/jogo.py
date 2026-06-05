import pygame
import random

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


def criar_comida(cobra):
    """Cria comida em posição aleatória (não sobrepondo a cobra)."""
    while True:
        x = (random.randint(0, (LARGURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
        y = (random.randint(0, (ALTURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
        
        # Garante que comida não nasce sobre a cobra
        if [x, y] not in cobra:
            return [x, y]


def criar_obstaculo():
    """Cria um obstáculo em posição aleatória."""
    x = (random.randint(0, (LARGURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
    y = (random.randint(0, (ALTURA_TELA // TAMANHO_QUADRADO) - 1)) * TAMANHO_QUADRADO
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
    """Verifica se a cobra colidiu com algum obstáculo."""
    cabeca = cobra[0]
    return cabeca in obstaculos


def desenhar_jogo(tela, cobra, comida, obstaculos, pontos, recorde, vidas, tempo_restante):
    """Desenha todos os elementos do jogo na tela."""
    tela.fill(CINZA)
    
    # Desenha a cobra
    for i, segmento in enumerate(cobra):
        if i == 0:  # Cabeça em verde mais claro
            cor = (0, 200, 0)
        else:  # Corpo em verde
            cor = VERDE
        pygame.draw.rect(tela, cor, (segmento[0], segmento[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    
    # Desenha a comida
    pygame.draw.rect(tela, VERMELHO, (comida[0], comida[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    
    # Desenha os obstáculos
    for obstaculo in obstaculos:
        pygame.draw.rect(tela, AMARELO, (obstaculo[0], obstaculo[1], TAMANHO_QUADRADO, TAMANHO_QUADRADO))
    
    # Desenha informações na tela
    fonte = pygame.font.Font(None, 36)
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, PRETO)
    texto_recorde = fonte.render(f"Recorde: {recorde}", True, PRETO)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, PRETO)
    texto_tempo = fonte.render(f"Tempo: {formatar_tempo(tempo_restante)}", True, PRETO)
    
    tela.blit(texto_pontos, (10, 10))
    tela.blit(texto_recorde, (10, 50))
    tela.blit(texto_vidas, (LARGURA_TELA - 200, 10))
    tela.blit(texto_tempo, (LARGURA_TELA - 200, 50))
    
    pygame.display.flip()


def executar_jogo():
    """Executa o loop principal do jogo da cobrinha."""
    pygame.init()
    
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    
    relogio = pygame.time.Clock()
    rodando = True
    
    # Inicializa o estado do jogo
    cobra = criar_cobra_inicial()
    comida = criar_comida(cobra)
    obstaculos = [criar_obstaculo() for _ in range(3)]  # 3 obstáculos iniciais
    
    direcao = "RIGHT"  # Direção inicial
    direcao_proxima = "RIGHT"
    
    pontos = 0
    vidas = VIDAS_INICIAIS
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_restante = TEMPO_JOGO
    tempo_ultimo_tick = pygame.time.get_ticks()
    
    velocidade_cobra = 10  # Frames entre movimentos
    contador_movimento = 0
    
    # Loop principal
    while rodando:
        relogio.tick(FPS)
        tempo_atual = pygame.time.get_ticks()
        
        # Atualiza tempo
        tempo_decorrido = (tempo_atual - tempo_ultimo_tick) / 1000
        tempo_restante -= tempo_decorrido
        tempo_ultimo_tick = tempo_atual
        
        # Processa eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != "DOWN":
                    direcao_proxima = "UP"
                elif evento.key == pygame.K_DOWN and direcao != "UP":
                    direcao_proxima = "DOWN"
                elif evento.key == pygame.K_LEFT and direcao != "RIGHT":
                    direcao_proxima = "LEFT"
                elif evento.key == pygame.K_RIGHT and direcao != "LEFT":
                    direcao_proxima = "RIGHT"
        
        # Atualiza movimento da cobra
        contador_movimento += 1
        if contador_movimento >= velocidade_cobra:
            direcao = direcao_proxima
            cobra = atualizar_cobra(cobra, direcao)
            contador_movimento = 0
            
            # Verificação de colisão com a própria cobra
            if verificar_colisao_cobra(cobra):
                vidas = tomar_dano(vidas, 1)
                if jogador_perdeu(vidas):
                    rodando = False
                else:
                    # Reinicia a cobra
                    cobra = criar_cobra_inicial()
                    direcao = "RIGHT"
                    direcao_proxima = "RIGHT"
            
            # Verificação de colisão com as paredes
            if verificar_colisao_paredes(cobra):
                vidas = tomar_dano(vidas, 1)
                if jogador_perdeu(vidas):
                    rodando = False
                else:
                    # Reinicia a cobra
                    cobra = criar_cobra_inicial()
                    direcao = "RIGHT"
                    direcao_proxima = "RIGHT"
            
            # Verificação de colisão com comida
            if verificar_colisao_comida(cobra, comida):
                pontos = calcular_pontos(pontos, 10)
                cobra.append(cobra[-1])  # Cresce a cobra
                comida = criar_comida(cobra)
                
                # A cada certa quantidade de pontos, adiciona obstáculo
                if pontos % 50 == 0 and len(obstaculos) < 5:
                    obstaculos.append(criar_obstaculo())
            
            # Verificação de colisão com obstáculos
            if verificar_colisao_obstaculo(cobra, obstaculos):
                vidas = tomar_dano(vidas, 1)
                if jogador_perdeu(vidas):
                    rodando = False
                else:
                    # Reinicia a cobra
                    cobra = criar_cobra_inicial()
                    direcao = "RIGHT"
                    direcao_proxima = "RIGHT"
        
        # Verifica tempo limite
        if tempo_restante <= 0:
            rodando = False
        
        # Atualiza recorde
        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)
        
        # Desenha o jogo
        desenhar_jogo(tela, cobra, comida, obstaculos, pontos, recorde, vidas, int(tempo_restante))
    
    pygame.quit()