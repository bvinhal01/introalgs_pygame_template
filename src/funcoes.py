def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos a pontuacao atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantem um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposicao entre dois retangulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def calcular_distancia_quadrada(posicao_a, posicao_b):
    """Calcula distancia ao quadrado entre dois pontos 2D."""
    dx = posicao_a[0] - posicao_b[0]
    dy = posicao_a[1] - posicao_b[1]
    return (dx * dx) + (dy * dy)


def colidiu_circulos(posicao_a, raio_a, posicao_b, raio_b):
    """Retorna True quando dois circulos se encostam."""
    soma_raios = raio_a + raio_b
    return calcular_distancia_quadrada(posicao_a, posicao_b) <= soma_raios * soma_raios


def esta_dentro_da_arena(posicao, raio, largura, altura, margem):
    """Confere se um circulo ainda esta dentro dos limites jogaveis."""
    x, y = posicao
    return (
        margem + raio <= x <= largura - margem - raio
        and margem + raio <= y <= altura - margem - raio
    )


def atualizar_tamanho_alvo(tamanho_atual, comida_valor):
    """Aumenta o comprimento alvo da cobra apos coletar comida."""
    return tamanho_atual + (comida_valor * 2)


def calcular_velocidade(base, pontuacao):
    """Aumenta a velocidade aos poucos conforme a pontuacao cresce."""
    bonus = min(pontuacao // 80, 5)
    return base + bonus
