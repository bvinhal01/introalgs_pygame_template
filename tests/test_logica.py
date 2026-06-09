import sys
import os

# Adiciona o diretório raiz ao path para importar módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, tomar_dano, formatar_tempo
from src.jogo import (
    criar_cobra_inicial, 
    criar_comida, 
    atualizar_cobra,
    verificar_colisao_cobra,
    verificar_colisao_paredes,
    verificar_colisao_comida,
    verificar_colisao_obstaculo,
)
from src.config import TAMANHO_QUADRADO, LARGURA_TELA, ALTURA_TELA


# ===== Testes de Pontuação =====
def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15
    assert calcular_pontos(0, 10) == 10
    assert calcular_pontos(100, 0) == 100


def test_calcular_pontos_grandes_numeros():
    """Deve funcionar com números grandes."""
    assert calcular_pontos(1000000, 500000) == 1500000


# ===== Testes de Vidas =====
def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Não deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False
    assert jogador_perdeu(1) is False


def test_jogador_perdeu_com_vidas_negativas():
    """Deve indicar derrota quando vidas são negativas."""
    assert jogador_perdeu(-1) is True


def test_tomar_dano():
    """Deve reduzir a vida corretamente."""
    assert tomar_dano(3, 1) == 2
    assert tomar_dano(5, 2) == 3
    assert tomar_dano(1, 1) == 0


# ===== Testes de Limites =====
def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite mínimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite máximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele já estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


# ===== Testes de Tempo =====
def test_formatar_tempo_segundos():
    """Deve formatar segundos corretamente."""
    assert formatar_tempo(0) == "00:00"
    assert formatar_tempo(30) == "00:30"
    assert formatar_tempo(60) == "01:00"
    assert formatar_tempo(90) == "01:30"
    assert formatar_tempo(120) == "02:00"


def test_formatar_tempo_grande():
    """Deve formatar tempos maiores corretamente."""
    assert formatar_tempo(300) == "05:00"
    assert formatar_tempo(3661) == "61:01"


# ===== Testes de Criação da Cobra =====
def test_criar_cobra_inicial():
    """Deve criar uma cobra com 3 segmentos."""
    cobra = criar_cobra_inicial()
    assert len(cobra) == 3
    
    # Verifica que os segmentos estão alinhados
    assert cobra[0][1] == cobra[1][1]  # Mesma linha Y
    assert cobra[0][1] == cobra[2][1]  # Mesma linha Y
    
    # Verifica espaçamento (cada segmento deve estar a uma célula de distância)
    assert cobra[0][0] - cobra[1][0] == TAMANHO_QUADRADO
    assert cobra[1][0] - cobra[2][0] == TAMANHO_QUADRADO


def test_criar_cobra_inicial_posicao():
    """A cobra deve ser criada aproximadamente no centro."""
    cobra = criar_cobra_inicial()
    # Verifica que a cabeça está dentro da tela
    assert 0 <= cobra[0][0] < LARGURA_TELA
    assert 0 <= cobra[0][1] < ALTURA_TELA


# ===== Testes de Comida =====
def test_criar_comida():
    """Deve criar comida fora da cobra."""
    cobra = criar_cobra_inicial()
    comida = criar_comida(cobra)
    
    # Verifica que a comida não está sobre a cobra
    assert comida not in cobra
    
    # Verifica que a comida está dentro da tela
    assert 0 <= comida[0] < LARGURA_TELA
    assert 0 <= comida[1] < ALTURA_TELA


def test_criar_comida_com_obstaculos():
    """Deve criar comida evitando cobra e obstáculos."""
    cobra = criar_cobra_inicial()
    obstaculos = [[100, 100], [200, 200]]
    comida = criar_comida(cobra, obstaculos)
    
    assert comida not in cobra
    assert comida not in obstaculos


# ===== Testes de Movimento =====
def test_atualizar_cobra_direita():
    """Cobra deve mover para a direita."""
    cobra = [[100, 100], [80, 100], [60, 100]]
    cobra_atualizada = atualizar_cobra(cobra, "RIGHT")
    
    # Verifica que a cabeça se moveu para direita
    assert cobra_atualizada[0][0] == 100 + TAMANHO_QUADRADO
    assert cobra_atualizada[0][1] == 100


def test_atualizar_cobra_esquerda():
    """Cobra deve mover para a esquerda."""
    cobra = [[100, 100], [120, 100], [140, 100]]
    cobra_atualizada = atualizar_cobra(cobra, "LEFT")
    
    assert cobra_atualizada[0][0] == 100 - TAMANHO_QUADRADO
    assert cobra_atualizada[0][1] == 100


def test_atualizar_cobra_cima():
    """Cobra deve mover para cima."""
    cobra = [[100, 100], [100, 120], [100, 140]]
    cobra_atualizada = atualizar_cobra(cobra, "UP")
    
    assert cobra_atualizada[0][0] == 100
    assert cobra_atualizada[0][1] == 100 - TAMANHO_QUADRADO


def test_atualizar_cobra_baixo():
    """Cobra deve mover para baixo."""
    cobra = [[100, 100], [100, 80], [100, 60]]
    cobra_atualizada = atualizar_cobra(cobra, "DOWN")
    
    assert cobra_atualizada[0][0] == 100
    assert cobra_atualizada[0][1] == 100 + TAMANHO_QUADRADO


def test_atualizar_cobra_comprimento():
    """Cobra não deve mudar de comprimento durante movimento."""
    cobra = criar_cobra_inicial()
    tamanho_original = len(cobra)
    
    cobra = atualizar_cobra(cobra, "RIGHT")
    assert len(cobra) == tamanho_original
    
    cobra = atualizar_cobra(cobra, "UP")
    assert len(cobra) == tamanho_original


# ===== Testes de Colisão =====
def test_verificar_colisao_cobra_sem_colisao():
    """Não deve detectar colisão quando cobra não colide com ela mesma."""
    cobra = criar_cobra_inicial()
    assert verificar_colisao_cobra(cobra) is False


def test_verificar_colisao_cobra_com_colisao():
    """Deve detectar colisão quando cobra colide com ela mesma."""
    cobra = [[100, 100], [80, 100], [60, 100], [80, 100]]  # Cabeça colidindo com corpo
    assert verificar_colisao_cobra(cobra) is True


def test_verificar_colisao_paredes_dentro():
    """Não deve detectar colisão quando cobra está dentro da tela."""
    cobra = [[100, 100], [80, 100], [60, 100]]
    assert verificar_colisao_paredes(cobra) is False


def test_verificar_colisao_paredes_esquerda():
    """Deve detectar colisão com parede esquerda."""
    cobra = [[-10, 100], [10, 100], [30, 100]]
    assert verificar_colisao_paredes(cobra) is True


def test_verificar_colisao_paredes_direita():
    """Deve detectar colisão com parede direita."""
    cobra = [[LARGURA_TELA + 10, 100], [LARGURA_TELA - 10, 100]]
    assert verificar_colisao_paredes(cobra) is True


def test_verificar_colisao_paredes_topo():
    """Deve detectar colisão com parede superior."""
    cobra = [[100, -10], [100, 10], [100, 30]]
    assert verificar_colisao_paredes(cobra) is True


def test_verificar_colisao_paredes_fundo():
    """Deve detectar colisão com parede inferior."""
    cobra = [[100, ALTURA_TELA + 10], [100, ALTURA_TELA - 10]]
    assert verificar_colisao_paredes(cobra) is True


def test_verificar_colisao_comida_sem_colisao():
    """Não deve detectar colisão com comida se cobra não a atingiu."""
    cobra = [[100, 100], [80, 100], [60, 100]]
    comida = [200, 200]
    assert verificar_colisao_comida(cobra, comida) is False


def test_verificar_colisao_comida_com_colisao():
    """Deve detectar colisão com comida quando cobra a atingiu."""
    cobra = [[100, 100], [80, 100], [60, 100]]
    comida = [100, 100]
    assert verificar_colisao_comida(cobra, comida) is True


def test_verificar_colisao_obstaculo_sem_colisao():
    """Não deve detectar colisão com obstáculo se cobra não o atingiu."""
    cobra = [[100, 100], [80, 100], [60, 100]]
    obstaculos = [[200, 200], [300, 300]]
    assert verificar_colisao_obstaculo(cobra, obstaculos) is False


def test_verificar_colisao_obstaculo_com_colisao():
    """Deve detectar colisão com obstáculo quando cobra o atingiu."""
    cobra = [[100, 100], [80, 100], [60, 100]]
    obstaculos = [[100, 100], [200, 200]]
    assert verificar_colisao_obstaculo(cobra, obstaculos) is True


if __name__ == "__main__":
    print("Executando testes...")
    # Para executar com pytest: pytest tests/test_logica.py -v
