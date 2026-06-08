# Jogo da Cobrinha - Pygame

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Bernardo Vinhal De Carvalho Teixeira

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> O jogo consiste em controlar uma cobra que deve coletar os itens no mapa e evitar obstáculos. O jogador ganha pontos ao coletar itens e perde vidas ao colidir com obstáculos. A partida termina quando o tempo acaba ou quando o jogador perde todas as vidas.

## Objetivo do jogador

> O objetivo é coletar a maior quantidade possível de itens antes que o tempo acabe, evitando colisões com os obstáculos.

## Requisitos

- Python 3.11+
- Pygame
- Pytest

## Regras do jogo

- O jogador se movimenta usando as setas do teclado.
- Cada item coletado aumenta a pontuação.
- Colidir com um obstáculo reduz a quantidade de vidas. ( max-3)

A partida termina quando:
- o jogador perde todas as vidas;
- o tempo acaba;
- a pontuação máxima é alcançada.

## Funcionalidades

- Sistema de pontuação
- Sistema de vidas
- Temporizador
- Obstáculos
- Crescimento da cobra
- Salvamento de recorde em arquivo

## Controles

- ↑ Mover para cima
- ↓ Mover para baixo
- ← Mover para esquerda
- → Mover para direita

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

