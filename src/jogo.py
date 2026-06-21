import math
import random
import sys
from dataclasses import dataclass

import pygame

from src.config import (
    ALTURA_TELA,
    AMARELO,
    AZUL,
    BRANCO,
    CAMINHO_RECORDE,
    CINZA,
    CINZA_CLARO,
    FPS,
    LARGURA_TELA,
    MARGEM_ARENA,
    PRETO,
    ROSA,
    ROXO,
    TITULO_JOGO,
    VERDE,
    VERDE_ESCURO,
    VERMELHO,
)
from src.dados import carregar_recorde, salvar_recorde
from src.funcoes import (
    atualizar_tamanho_alvo,
    calcular_pontos,
    calcular_velocidade,
    colidiu_circulos,
    esta_dentro_da_arena,
)


RAIO_CABECA = 15
RAIO_CORPO = 13
VELOCIDADE_BASE = 4.2
COMIDA_TOTAL = 34
OBSTACULO_TOTAL = 7


@dataclass
class Comida:
    posicao: pygame.Vector2
    raio: int
    valor: int
    cor: tuple


@dataclass
class Obstaculo:
    posicao: pygame.Vector2
    raio: int


def criar_texto(fonte, texto, cor):
    """Cria uma superficie de texto com antialias para HUD e menus."""
    return fonte.render(texto, True, cor)


def sortear_posicao(raio):
    """Sorteia um ponto dentro da arena respeitando o raio do objeto."""
    return pygame.Vector2(
        random.randint(MARGEM_ARENA + raio, LARGURA_TELA - MARGEM_ARENA - raio),
        random.randint(MARGEM_ARENA + raio, ALTURA_TELA - MARGEM_ARENA - raio),
    )


def criar_obstaculos():
    """Cria pedras fixas que funcionam como perigo adicional na arena."""
    obstaculos = []
    for _ in range(OBSTACULO_TOTAL):
        raio = random.randint(18, 30)
        obstaculos.append(Obstaculo(sortear_posicao(raio), raio))
    return obstaculos


def criar_comida(cobra, obstaculos):
    """Gera comida longe da cobra e dos obstaculos."""
    cores = [AMARELO, AZUL, ROSA, ROXO, VERDE]
    for _ in range(120):
        raio = random.randint(5, 9)
        posicao = sortear_posicao(raio)

        perto_da_cobra = any(
            colidiu_circulos(posicao, raio + 24, ponto, RAIO_CABECA)
            for ponto in cobra[:18]
        )
        perto_de_obstaculo = any(
            colidiu_circulos(posicao, raio + 8, obstaculo.posicao, obstaculo.raio)
            for obstaculo in obstaculos
        )

        if not perto_da_cobra and not perto_de_obstaculo:
            return Comida(posicao, raio, raio, random.choice(cores))

    return Comida(sortear_posicao(7), 7, 7, AMARELO)


def manter_trilha(cobra, tamanho_alvo):
    """Mantem o corpo no comprimento desejado removendo a cauda excedente."""
    while len(cobra) > tamanho_alvo:
        cobra.pop()


def direcao_por_teclado(teclas, direcao_atual):
    """Converte WASD/setas em um vetor de direcao suave."""
    eixo_x = 0
    eixo_y = 0

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        eixo_x -= 1
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        eixo_x += 1
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        eixo_y -= 1
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        eixo_y += 1

    nova_direcao = pygame.Vector2(eixo_x, eixo_y)
    if nova_direcao.length_squared() == 0:
        return direcao_atual

    return nova_direcao.normalize()


def desenhar_grade(tela):
    """Desenha o fundo quadriculado da arena."""
    tela.fill(PRETO)
    arena = pygame.Rect(
        MARGEM_ARENA,
        MARGEM_ARENA,
        LARGURA_TELA - MARGEM_ARENA * 2,
        ALTURA_TELA - MARGEM_ARENA * 2,
    )
    pygame.draw.rect(tela, CINZA, arena, border_radius=12)
    pygame.draw.rect(tela, CINZA_CLARO, arena, width=2, border_radius=12)

    for x in range(MARGEM_ARENA, LARGURA_TELA - MARGEM_ARENA, 40):
        pygame.draw.line(
            tela,
            (39, 47, 65),
            (x, MARGEM_ARENA),
            (x, ALTURA_TELA - MARGEM_ARENA),
        )
    for y in range(MARGEM_ARENA, ALTURA_TELA - MARGEM_ARENA, 40):
        pygame.draw.line(
            tela,
            (39, 47, 65),
            (MARGEM_ARENA, y),
            (LARGURA_TELA - MARGEM_ARENA, y),
        )


def desenhar_cobra(tela, cobra, direcao):
    """Desenha a cobra com corpo circular, brilho e olhos."""
    for indice, ponto in enumerate(reversed(cobra)):
        progresso = indice / max(len(cobra), 1)
        raio = max(7, int(RAIO_CORPO - progresso * 3))
        cor = VERDE if indice % 2 == 0 else VERDE_ESCURO
        pygame.draw.circle(tela, (8, 18, 14), ponto, raio + 3)
        pygame.draw.circle(tela, cor, ponto, raio)

    cabeca = cobra[0]
    pygame.draw.circle(tela, (7, 21, 16), cabeca, RAIO_CABECA + 5)
    pygame.draw.circle(tela, VERDE, cabeca, RAIO_CABECA)

    # Os olhos seguem a direcao do movimento para dar leitura visual ao jogador.
    perpendicular = pygame.Vector2(-direcao.y, direcao.x)
    for lado in (-1, 1):
        olho = cabeca + direcao * 8 + perpendicular * lado * 6
        pygame.draw.circle(tela, BRANCO, olho, 4)
        pygame.draw.circle(tela, PRETO, olho + direcao * 1.5, 2)


def desenhar_comidas(tela, comidas, tempo):
    """Desenha alimentos com pulsacao simples, sem depender de imagens externas."""
    for comida in comidas:
        pulso = math.sin(tempo * 0.006 + comida.posicao.x) * 2
        pygame.draw.circle(tela, (12, 17, 26), comida.posicao, comida.raio + 5 + int(pulso))
        pygame.draw.circle(tela, comida.cor, comida.posicao, comida.raio + int(max(pulso, 0)))
        pygame.draw.circle(tela, BRANCO, comida.posicao, max(2, comida.raio // 3))


def desenhar_obstaculos(tela, obstaculos):
    """Desenha obstaculos que encerram a partida se a cabeca encostar."""
    for obstaculo in obstaculos:
        pygame.draw.circle(tela, (72, 80, 103), obstaculo.posicao, obstaculo.raio)
        pygame.draw.circle(tela, (34, 40, 55), obstaculo.posicao, obstaculo.raio, width=4)
        brilho = obstaculo.posicao + pygame.Vector2(-obstaculo.raio // 3, -obstaculo.raio // 3)
        pygame.draw.circle(tela, (113, 124, 153), brilho, max(4, obstaculo.raio // 4))


def desenhar_hud(tela, fonte, pontos, recorde, tamanho, pausado):
    """Mostra informacoes principais da partida."""
    textos = [
        f"Pontos: {pontos}",
        f"Recorde: {recorde}",
        f"Tamanho: {tamanho}",
        "Pausado" if pausado else "P: pausar",
    ]
    x = MARGEM_ARENA
    for texto in textos:
        superficie = criar_texto(fonte, texto, BRANCO)
        tela.blit(superficie, (x, 12))
        x += superficie.get_width() + 28


def mostrar_tela_mensagem(tela, relogio, fonte_titulo, fonte_texto, titulo, linhas, cor_titulo):
    """Exibe tela de inicio ou fim e aguarda uma escolha do jogador."""
    while True:
        relogio.tick(FPS)
        desenhar_grade(tela)

        titulo_render = criar_texto(fonte_titulo, titulo, cor_titulo)
        tela.blit(titulo_render, titulo_render.get_rect(center=(LARGURA_TELA // 2, 170)))

        for indice, linha in enumerate(linhas):
            cor = BRANCO if indice < len(linhas) - 1 else AMARELO
            texto = criar_texto(fonte_texto, linha, cor)
            tela.blit(texto, texto.get_rect(center=(LARGURA_TELA // 2, 260 + indice * 42)))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False


def executar_partida(tela, relogio, fonte_hud):
    """Executa uma partida completa e retorna a pontuacao final."""
    cobra = [pygame.Vector2(LARGURA_TELA // 2 - i * 5, ALTURA_TELA // 2) for i in range(28)]
    direcao = pygame.Vector2(1, 0)
    tamanho_alvo = 80
    pontos = 0
    pausado = False

    obstaculos = criar_obstaculos()
    comidas = [criar_comida(cobra, obstaculos) for _ in range(COMIDA_TOTAL)]
    recorde = carregar_recorde(CAMINHO_RECORDE)

    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return pontos
                if evento.key == pygame.K_p:
                    pausado = not pausado

        teclas = pygame.key.get_pressed()

        if not pausado:
            direcao = direcao_por_teclado(teclas, direcao)
            velocidade = calcular_velocidade(VELOCIDADE_BASE, pontos)
            nova_cabeca = cobra[0] + direcao * velocidade

            cobra.insert(0, nova_cabeca)
            manter_trilha(cobra, tamanho_alvo)

            if not esta_dentro_da_arena(nova_cabeca, RAIO_CABECA, LARGURA_TELA, ALTURA_TELA, MARGEM_ARENA):
                return pontos

            # Ignoramos os segmentos proximos da cabeca para nao punir curvas normais.
            for segmento in cobra[24:]:
                if colidiu_circulos(nova_cabeca, RAIO_CABECA - 3, segmento, RAIO_CORPO - 4):
                    return pontos

            for obstaculo in obstaculos:
                if colidiu_circulos(nova_cabeca, RAIO_CABECA, obstaculo.posicao, obstaculo.raio):
                    return pontos

            for comida in comidas[:]:
                if colidiu_circulos(nova_cabeca, RAIO_CABECA, comida.posicao, comida.raio):
                    pontos = calcular_pontos(pontos, comida.valor)
                    tamanho_alvo = atualizar_tamanho_alvo(tamanho_alvo, comida.valor)
                    comidas.remove(comida)
                    comidas.append(criar_comida(cobra, obstaculos))

                    if pontos > recorde:
                        recorde = pontos
                        salvar_recorde(CAMINHO_RECORDE, recorde)

        desenhar_grade(tela)
        desenhar_comidas(tela, comidas, pygame.time.get_ticks())
        desenhar_obstaculos(tela, obstaculos)
        desenhar_cobra(tela, cobra, direcao)
        desenhar_hud(tela, fonte_hud, pontos, recorde, len(cobra), pausado)
        pygame.display.flip()


def executar_jogo():
    """Inicializa Pygame, mostra menus e controla reinicio da partida."""
    pygame.init()
    pygame.display.set_caption(TITULO_JOGO)
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    relogio = pygame.time.Clock()

    fonte_titulo = pygame.font.SysFont("Arial", 58, bold=True)
    fonte_texto = pygame.font.SysFont("Arial", 26)
    fonte_hud = pygame.font.SysFont("Arial", 22, bold=True)

    iniciar = mostrar_tela_mensagem(
        tela,
        relogio,
        fonte_titulo,
        fonte_texto,
        "Snake Adventure",
        [
            "Colete orbes, cresca e sobreviva na arena.",
            "Use WASD ou setas para mover. P pausa. ESC encerra.",
            "Pressione ENTER para jogar.",
        ],
        VERDE,
    )

    while iniciar:
        pontuacao = executar_partida(tela, relogio, fonte_hud)
        recorde = carregar_recorde(CAMINHO_RECORDE)
        iniciar = mostrar_tela_mensagem(
            tela,
            relogio,
            fonte_titulo,
            fonte_texto,
            "Fim de jogo",
            [
                f"Pontuacao final: {pontuacao}",
                f"Recorde salvo: {recorde}",
                "ENTER joga de novo. ESC sai.",
            ],
            VERMELHO,
        )

    pygame.quit()
