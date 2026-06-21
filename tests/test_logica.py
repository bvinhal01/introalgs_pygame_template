from src.funcoes import (
    atualizar_tamanho_alvo,
    calcular_distancia_quadrada,
    calcular_pontos,
    calcular_velocidade,
    colidiu_circulos,
    esta_dentro_da_arena,
    jogador_perdeu,
    limitar_valor,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_distancia_quadrada():
    """Deve calcular distancia ao quadrado sem usar raiz."""
    assert calcular_distancia_quadrada((0, 0), (3, 4)) == 25


def test_colidiu_circulos_quando_raios_encostam():
    """Deve detectar colisao entre circulos."""
    assert colidiu_circulos((0, 0), 5, (8, 0), 3) is True


def test_nao_colidiu_circulos_distantes():
    """Nao deve detectar colisao quando os circulos estao afastados."""
    assert colidiu_circulos((0, 0), 4, (20, 0), 4) is False


def test_esta_dentro_da_arena():
    """Deve validar se o jogador esta dentro dos limites jogaveis."""
    assert esta_dentro_da_arena((50, 50), 10, 100, 100, 20) is True
    assert esta_dentro_da_arena((25, 50), 10, 100, 100, 20) is False


def test_atualizar_tamanho_alvo():
    """Cada comida deve aumentar o comprimento alvo da cobra."""
    assert atualizar_tamanho_alvo(80, 7) == 94


def test_calcular_velocidade_com_limite_de_bonus():
    """A velocidade aumenta com pontos, mas tem limite de bonus."""
    assert calcular_velocidade(4, 0) == 4
    assert calcular_velocidade(4, 160) == 6
    assert calcular_velocidade(4, 999) == 9
