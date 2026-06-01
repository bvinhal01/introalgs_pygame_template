# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

CobraRun

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Bernardo Vinhal De Carvalho Teixeira

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> jogo de coleta de itens / Snake;

## 4. Descrição geral do jogo

A proposta é um terminal simples, com o controle total do usuário, onde a cobra vai ficando cada vez maior, a cada objeto que o jogador passa por cima (comido prla cobra);
Direcionais para norte, sul, leste e oeste.
A grande questão é que a cobra fica maior a cada item ingerido, permitindo o aumento significativo da dificuldade.

## 5. Objetivo do jogador

- O objetivo principal é coletar o maior número possível de itens e sobreviver pelo maior tempo possível;

## 6. Regras principais

- Regra 1: O jogador começa com 3 vidas.
- Regra 2: Cada objeto ingerido aumenta em tamanho 1 o personagem.
- Regra 3: Cada colisão com obstáculo remove 1 vida.
- Regra 3: A partida termina quando as vidas chegam a zero.
- Regra 4 O jogador vence se alcançar 100 pontos.

## 7. Condição de vitória

Condição de vitória:

> Atingir determinada pontuação e sobreviver até o tempo acabar;

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Descrição:

> Uma cobra controlado pelas setas do teclado.

## Obstáculos, inimigos ou desafios

Descrição:

> Obstáculos estão no proprio tamanho do personagem.

## Itens, alvos ou objetos de interação

Descrição:

> > Frutas aparecem na tela e aumentam a pontuação quando coletadas.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

## 10. Controles previstos

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Seta para cima: mover para cima
- Tecla/comando: Seta para cima: mover para cima
- Tecla/comando: Seta para baixo: mover para baixo
- Tecla/comando: Seta para esquerda: mover para esquerda
- Tecla/comando: Seta para direita: mover para direita
- Tecla/comando: Espaço: realizar ação
- Tecla/comando: ESC: sair do jogo

## 11. Organização inicial do código

Organização planejada:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Recursos previstos:

Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Dificuldades previstas:

- Dificuldade 1: movimentação do jogador;
- Dificuldade 2: colisão entre objetos;
- Dificuldade 3: controle de tempo;
- Dificuldade 4: organização do código;
- Dificuldade 5: testes;
- Dificuldade 6: exibição de textos na tela.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Escopo mínimo:

>> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.


## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Melhorias possíveis:

- Melhoria 1: tela inicial;
- Melhoria 2: sons;
- Melhoria 3: animações;
- Melhoria 4: diferentes personagens;
- Melhoria 5: menu de pausa.